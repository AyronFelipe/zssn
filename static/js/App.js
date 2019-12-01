import Vue from 'vue';
import axios from 'axios';
import Principal from './components/Principal.vue';
import lodash from 'lodash';

Vue.use(axios, lodash);

new Vue(Principal).$mount("#main");