<template>
  <h1>欢迎光临我的小站</h1>
  <el-image  class="pic" src="/TAKAGI/login.jpg"  />
  <div class="login">
    <el-form :model="ruleForm" :rules="rules" ref="ruleForm" style="width: 400px;height: 200px" label-width="120px" label-position="top" hide-required-asterisk>
      <el-form-item prop="user" label="手机号" >
        <el-input v-model="ruleForm.user" type="text"/>
      </el-form-item>
      <el-form-item prop="checkPass" label="密码">
        <el-input v-model="ruleForm.checkPass" type="password"/>
      </el-form-item>
        <el-button type="primary" round @click="submit">登录</el-button>
        <el-button type="primary" round @click="jump">注册</el-button>
    </el-form>
  </div>
</template>


<script>
  import{ requestLogin } from '../api/api';
  export default {
    data() {
      return {
        ruleForm: {
          user: '',
          checkPass: ''
        },
        rules: {
          user: [
            { required: true, message: '请输入手机号', trigger: 'blur' },
            {min: 11, max: 11, message: '手机号格式错误', trigger: 'blur'},
          ],
          checkPass: [
            { required: true, message: '请输入密码', trigger: 'blur' },
          ]
        },
        checked: true
      };
    },
    name: "login",
    mounted(){
    },
    methods: {
      submit() {
        this.$refs.ruleForm.validate((valid =>{
          if (valid){
            let loginParams = {phoneNumber: this.ruleForm.user, password: this.ruleForm.checkPass};
            requestLogin(loginParams).then(res=>{
              console.log(res.data)
              let {msg, code, name} = res.data
              if (code == 200) {
                msg = '欢迎你,' + name
                alert(msg)
                this.$router.push({path:'/register'})
              }
              else {
                alert(msg)
              }
          })
          }
        }))
      },
      jump(){
        this.$router.push({path:'/register'})
      }
    }
  }
</script>
<style lang="less">
  h1 {
    color: red;
  }
  .pic{
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.5); //增加阴影
    border-radius: 8px;
    width: 400px;
    height: 600px;
  }
  .login {
    text-align: -webkit-center;
  }
</style>