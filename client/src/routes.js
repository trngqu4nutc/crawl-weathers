// const Header = (reslove) => {
//     require.ensure(['./components/layouts/Header'], () => {
//         reslove(require('./components/layouts/Header'));
//     });
// }
// const Home = (reslove) => {
//     require.ensure(['./components/Home'], () => {
//         reslove(require('./components/Home'));
//     });
// }
// const Weathers = (reslove) => {
//     require.ensure(['./components/Weathers'], () => {
//         reslove(require('./components/Weathers'));
//     });
// }
// const Days = (reslove) => {
//     require.ensure(['./components/Days'], () => {
//         reslove(require('./components/Days'));
//     });
// }
// const Error = (reslove) => {
//     require.ensure(['./components/Error'], () => {
//         reslove(require('./components/Error'));
//     });
// }

import Header from './components/layouts/Header';
import Home from './components/Home';
import Weathers from './components/Weathers';
import Days from './components/Days';
import Error from './components/Error';

export const routes = [
    {
        path: '/', name: 'homepage', components: {
            default: Home,
            'Header': Header
        }
    },
    {
        path: '/weather', name: 'weather', component: Weathers
    },
    {
        path: '/days', name: 'days', component: Days
    },
    { path: '/404', name: 'error', component: Error },
    { path: '*', redirect: { path: '/404' } }
]