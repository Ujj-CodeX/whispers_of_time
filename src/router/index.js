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
        path:'/dash/:id',
        name: 'dash',
        component : Dash,
        props: true
    },
    
    
    


]

const router = createRouter ({
    history : createWebHashHistory(),
    routes

})
export default router