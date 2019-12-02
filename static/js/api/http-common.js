import axios from 'axios';

export const api = axios.create({
    baseURL: `https://morning-depths-60314.herokuapp.com/api/`,
});