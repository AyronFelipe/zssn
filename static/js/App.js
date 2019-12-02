import Vue from 'vue';
import Router from 'vue-router';
import Principal from './components/Principal.vue';
import NovoSobrevivente from './components/NovoSobrevivente.vue';
import AtualizarLocal from './components/AtualizarLocal.vue';
import Inicial from './components/Inicial.vue';
import InformarInfectado from './components/InformarInfectado.vue';

Vue.use(Router);

const routes = [
    { path: '/', name: 'inicial', component: Inicial },
    { path: '/novo-sobrevivente', name: 'novo_sobrevivente', component: NovoSobrevivente },
    { path: '/atualizar-local', name: 'atualizar_local', component: AtualizarLocal },
    { path: '/informar-infectado', name: 'informar_infectado', component: InformarInfectado },
]

const router = new Router({ routes });

new Vue({
    el: '#main',
    router,
    template: '<Principal />',
    components: { Principal }
});