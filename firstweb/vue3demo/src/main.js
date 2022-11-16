import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import '../../node_modules/element-plus/dist/index.css'
//将app.vue声明过来
import App from './App.vue'
import './index.css'
import router from '../src/route/index'

//以声明过来的app创建实例
const app = createApp(App)
app.use(ElementPlus)
app.use(router)
// 给实例绑定在index.html的相应位置，这里就是把这个app绑定在html中id=app的div中
app.mount('#app')

