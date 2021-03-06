import Vue from 'vue'
import App from './App.vue'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import './plugins/element.js'
import locale from 'element-ui/lib/locale/lang/en'

Vue.config.productionTip = false

Vue.use(ElementUI, {locale});


new Vue({
  el: '#app',
  render: h => h(App)
});
