import { createRouter,createWebHistory } from 'vue-router'
import register from '../components/register.vue'
import login from '../components/login.vue'
import index from '../components/index.vue'

const router = new createRouter({
    history : createWebHistory(),
    routes: [
        {
            path: '/',
            name: 'index',
            component:index,
        },
        {
            path: '/login',
            name: 'login',
            component: login,
        },
        {
            path:'/register',
            name:'register',
            component:register
        }
    ]
})
export default router


