import { createApp } from 'vue'
import App from './App.vue'
import ElementPlus from 'element-plus'  // 导入element-plus
import * as ElementPlusIconsVue from '@element-plus/icons-vue' // 导入element-plus/icons-vue
import router from './router'
import store from './store'
import 'element-plus/dist/index.css'    // 引入element-plus样式
import './assets/css/mystyle.css'       // 引入mystyle主页面样式
import { Menu } from '@element-plus/icons-vue'

const app = createApp(App)
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component)
}

app.use(ElementPlus)
app.use(ElementPlusIconsVue)
app.use(store)
app.use(router)
app.mount('#app')

export default {
    name:'menuList',
    components: {
        Menu
    },
    
}

