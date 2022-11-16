<template>
    <el-container>
        <el-header>
            <el-row :gutter="20">
                <el-col :span="6"><div class="grid">擅长捉弄的高木同学漫画</div></el-col>
                <el-col :span="6"><div class="grid">擅长捉弄的高木同学视频</div></el-col>
                <el-col :span="6"><div class="grid">擅长捉弄的高木同学官方日历图</div></el-col>
                <el-col :span="6"><div class="grid">1</div></el-col>
            </el-row>
        </el-header>
        <el-container/>
        <el-container>
            <el-aside width="700px">
                <el-carousel type="card" height="500px">
                    <el-carousel-item v-for="item in takagi" :key="item">
                        <img :src="item.src"/>
                    </el-carousel-item>
                </el-carousel>
            </el-aside>
            <el-main>
                111
            </el-main>
        <el-container/>

    <div class="carousel">

    </div>
    <div class="recommend">

    </div>
</template>

<script>
    export default {
        data(){
            return {
                fitHeight: 500,
                takagi:[
                    {src: '../../public/TAKAGI/1.jpg'},
                    {src: '../../public/TAKAGI/2.jpg'},
                    {src: '../../public/TAKAGI/3.jpg'},
                    {src: '../../public/TAKAGI/4.jpg'},
                ]
            }
        },
    }
</script>
<style>
    .carousel{
        border:1px solid  transparent;
        box-shadow: 1px 1px 0 0  rgba(0,0,0,0.2);
    }
    img{
        width: 100%;
        height: inherit;
    }
    /deep/ .el-col {
        border-radius: 4px;
        span: 6
    }
    /deep/ .el-row {
        margin-bottom: 20px;
    }
    .grid {
        background: #f5f6f7;
        height: 30px;
        border-radius: 10px;
        text-align: center;
        align-items:center;

    }
</style>