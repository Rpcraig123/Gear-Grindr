import Vue from 'vue'
import { BootstrapVue, LayoutPlugin } from 'bootstrap-vue'
import App from './App.vue'
import './styles/App.css'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.config.productionTip = false

Vue.use(BootstrapVue)
Vue.use(LayoutPlugin)

new Vue({
  render: h => h(App),
}).$mount('#app')
