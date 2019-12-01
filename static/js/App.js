import Vue from 'vue';
import Router from 'vue-router';
import Principal from './components/Principal.vue';
import NovoSobrevivente from './components/NovoSobrevivente.vue';
import Inicial from './components/Inicial.vue';

Vue.use(Router);

const routes = [
    { path: '/', name: 'inicial', component: Inicial },
    { path: '/novo-sobrevivente', name: 'novo_sobrevivente', component: NovoSobrevivente },
]

const router = new Router({ routes });

new Vue({
    el: '#main',
    router,
    template: '<Principal />',
    components: { Principal }
});