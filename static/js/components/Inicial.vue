<template>
    <div class="wrapper">
        <Header />
        <Sidebar />
        <div class="main-panel">
            <div class="content">
                <div class="page-inner">
                    <div class="row">
                        <div class="col-md-6">
                            <div class="card card-secondary">
                                <div class="card-body skew-shadow">
                                    <h1>{{ Math.round(porcentagem_sobreviventes_nao_infectados) }} %</h1>
                                    <h5 class="op-8">Sobreviventes não infectados</h5>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="card card-dark bg-secondary-gradient">
                                <div class="card-body bubble-shadow">
                                    <h1>{{ Math.round(porcentagem_sobreviventes_infectados) }} %</h1>
                                    <h5 class="op-8">Sobreviventes infectados</h5>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-sm-6 col-md-3" v-for="(stats, index) in estatisticas" :key="index">
                            <div class="card card-stats card-primary card-round">
                                <div class="card-body">
                                    <div class="row">
                                        <div class="col-5">
                                            <div class="icon-big text-center">
                                            </div>
                                        </div>
                                        <div class="col-7 col-stats">
                                            <div class="numbers">
                                                <p class="card-category">{{ stats.nome }}</p>
                                                <h4 class="card-title">{{ stats.media }}</h4>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-md-12">
                            <div class="card">
                                <div class="card-header">
                                    <div class="card-head-row">
                                        <div class="card-title">Sobreviventes</div>
                                    </div>
                                </div>
                                <div class="card-body">
                                    <div class="table-responsive">

                                        <table class="table">
                                            <thead>
                                                <tr>
                                                    <th>Nome</th>
                                                    <th>Idade</th>
                                                    <th>Última localização</th>
                                                    <th>Infectado?</th>
                                                </tr>
                                            </thead>
                                            <tbody>
                                                <tr v-for="sobrevivente in sobreviventes" :key="sobrevivente.pk">
                                                    <td>{{ sobrevivente.nome }}</td>
                                                    <td>{{ sobrevivente.idade }}</td>
                                                    <td>{{ sobrevivente.latitude }}S {{ sobrevivente.longitude }}O</td>
                                                    <td>
                                                        <p v-if="sobrevivente.infectado">Sim</p>
                                                        <p v-else>Não</p>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import Header from './Header';
    import Sidebar from './Sidebar';
    import { api } from '../api/http-common';
    import Swal from 'sweetalert2';


    export default {
        name: 'inicial',
        components: {
            Header,
            Sidebar
        },
        data() {
            return{
                sobreviventes: [],
                porcentagem_sobreviventes_nao_infectados: '',
                porcentagem_sobreviventes_infectados: '',
                estatisticas: [],
            }
        },
        created() {
            api.get(`sobreviventes-totais/`)
            .then(res => {
                this.sobreviventes = res.data.sobreviventes;
                this.porcentagem_sobreviventes_nao_infectados = res.data.porcentagem_sobreviventes_nao_infectados
                this.porcentagem_sobreviventes_infectados = res.data.porcentagem_sobreviventes_infectados
            });
            api.get('media-recurso')
            .then(res => {
                this.estatisticas = res.data
            });
        }
    }
</script>

<style>

</style>