import { createApp } from 'vue'
import App from './App.vue'
import ElementPlus from 'element-plus'  // 导入element-plus
import router from './router'
import store from './store'
import 'element-plus/dist/index.css'    // 引入element-plus样式
import './assets/css/mystyle.css'       // 引入mystyle主页面样式

createApp(App).use(ElementPlus).use(store).use(router).mount('#app')



