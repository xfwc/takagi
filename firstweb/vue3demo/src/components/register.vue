<template>
    <div class="register">
        <div class="register_div">
            <h1>欢迎你的加入</h1>
            <el-form class="register_form" :model="ruleForm" :rules="rules" ref="ruleForm" label-position="left" >
                <el-form-item  label="用户名:" prop="user">
                    <el-input v-model="ruleForm.user" type="text"/>
                </el-form-item>
                <el-form-item  label="手机号:" prop="phone">
                    <el-input v-model="ruleForm.phone" type="text" />
                </el-form-item>
                <el-form-item label="密码:" prop="password">
                    <el-input v-model="ruleForm.password" type="password"/>
                </el-form-item>
                <el-form-item label="确认密码:" prop="checkPass">
                    <el-input v-model="ruleForm.checkPass" type="password" />
                </el-form-item>
                <el-button type="primary" round @click="register">立即注册</el-button>
            </el-form>
        </div>
    </div>
</template>

<script>
    import {requestRegister} from "../api/api";
    export default {
        name: "register",
        data() {
            const Check = (rule, value, callback) => {
                if (value) {
                    if (value == this.ruleForm.password)
                        callback()
                    else{
                        callback(new Error('两次输入的密码不同'))
                    }
                } else {
                    callback(new Error('请确认密码'))
                }
                };
            return {
                ruleForm: {
                    user: '',
                    phone: '',
                    password: '',
                    checkPass: ''
                },
                rules: {
                    user: [
                        {required: true, message: '请输入用户名', trigger: 'blur'}
                    ],
                    phone: [
                        {required: true, message: '请输入手机号', trigger: 'blur'},
                        {min: 11, max: 11, message: '手机号格式错误', trigger: 'blur'},
                    ],
                    password: [
                        {required: true, message: '请输入密码', trigger: 'blur'}
                    ],
                    checkPass: [
                        {required: true, message: '请确认密码', trigger: 'blur'},
                        {validator: Check, trigger: 'blur'}
                    ]
                },
                checked: true
            }
        },
        mounted() {
        },
        methods: {
            register() {
                this.$refs.ruleForm.validate((valid)=> {
                    if (valid) {
                        let registerParams = {
                            username: this.ruleForm.user,
                            phone: this.ruleForm.phone,
                            password: this.ruleForm.password
                        }
                        requestRegister(registerParams).then(res => {
                            let {code, msg} = res.data;
                            alert(msg)
                            if (code == 200) {
                                this.$router.push({path: '/'})
                            }
                        })
                    }
                })
                }
            }
    }
</script>

<style scoped lang="less" >
h1{
    color: #c3ff97;
}
.register {
    text-align: -webkit-center;
    background-image: url("../../public/TAKAGI/register.jpg");
    background-position: center;
    height: 100%;
    width: 100%;
    background-size: cover;
    position:fixed;
}
.register_div{
    margin-top: 250px;
    width: 600px;
    height: 250px;
}
.register_form{
    text-align: center;
    width:99%;
    height:99%;
    border:1px solid  transparent;
    /* 为其整体设置接近透明的效果*/
    background-color: rgba(255,255,255,0.1);
    /* 设置box-shadow使其有立体感 */
    box-shadow: 5px 5px 0 0  rgba(0,0,0,0.2);
    position: relative;
}
/deep/ .el-input__inner {
    font-weight:bold ;
    color: #af8495;
    background-color: rgba(255, 255, 255, 0.347);
}
</style>