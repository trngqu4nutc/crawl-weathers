import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import { routes } from './routes'
import axios from 'axios';

// setTimeout(() => {
//   axios.post('http://localhost:4000/now')
//     .then(res => {
//       console.log(res.data);
//     })
//     .catch(err => console.log(err));
//   setInterval(() => {
//     axios.post('http://localhost:4000/now')
//       .then(res => {
//         console.log(res.data);
//       })
//       .catch(err => console.log(err));
//   }, 1000 * 60 * 60 * 2);
// }, 1000);

Vue.use(VueRouter);

const router = new VueRouter({
  mode: "history",
  routes
});


new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
