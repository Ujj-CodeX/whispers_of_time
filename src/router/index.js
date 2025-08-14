import { createRouter , createWebHashHistory } from 'vue-router'
import Home from '../components/Home.vue'
import Dash from '@/components/Dash.vue'
const routes =[
    {
        path:'/',
        name: 'Home',
        component : Home
    },
    {
        path:'/dash',
        name: 'dash',
        component : Dash
    },
    
    
    


]

const router = createRouter ({
    history : createWebHashHistory(),
    routes

})
export default router