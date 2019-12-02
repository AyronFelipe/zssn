<template>
    <div class="wrapper">
        <Header />
        <Sidebar />
        <div class="main-panel">
            <div class="content">
                <div class="page-inner">
                    <div class="page-header">
                        <div class="page-title">Informar infectado</div>
                        <ul class="breadcrumbs">
                            <li class="nav-home">
                                <router-link to="/">
                                    <i class="flaticon-home"></i>
                                </router-link>
                            </li>
                            <li class="separator">
                                <i class="flaticon-right-arrow"></i>
                            </li>
                            <li class="nav-item submenu">
                                <router-link to="/informar-infectado/">
                                    Informar infectado
                                </router-link>
                            </li>
                        </ul>
                    </div>
                    <div class="row">
                        <div class="col-md-12">
                            <div class="card">
                                <div class="card-header">
                                    <div class="card-title">Informar infectado</div>
                                </div>
                                <form v-on:submit.prevent="onSubmit">
                                    <div class="card-body">
                                        <div class="row">
                                            <div class="col-12">
                                                <div class="form-group">
                                                    <label for="nome">Sobrevivente <span class="required-label">*</span></label>
                                                    <select name="" id="" v-model="sobrevivente" class="form-control">
                                                        <option v-for="sobrevivente in sobreviventes" :key="sobrevivente.pk" :value="sobrevivente.pk">
                                                            {{ sobrevivente.nome }}
                                                        </option>
                                                    </select>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="card-action">
                                        <div class="d-flex flex-row-reverse">
                                            <button type="submit" class="btn btn-primary btn-lg"><i class="fas fa-save mr-1"></i> Salvar</button>
                                        </div>
                                    </div>
                                </form>
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
        name: 'informar_infectado',
        components: {
            Header,
            Sidebar
        },
        data() {
            return {
                sobreviventes: [],
                sobrevivente: '',
            }
        },
        created() {
            api.get('sobreviventes/')
            .then(res => {
                this.sobreviventes = res.data;
            })
            .catch(error => {
                Swal.fire({
                    icon: 'error',
                    title: 'Oops...',
                    text: error.response.data.message,
                });
            });
        },
        methods: {
            onSubmit() {
                let body ={
                    sobrevivente: this.sobrevivente
                };
                api.post(`sobrevivente/${this.sobrevivente}/infectado/`, body)
                .then(res => {
                    Swal.fire({
                        icon: 'success',
                        title: 'Sucesso!',
                        text: res.data.message,
                    })
                    .then(() => {
                        window.location.href = '/';
                    });
                })
                .catch(error => {
                    Swal.fire({
                        icon: 'error',
                        title: 'Oops...',
                        text: error.response.data.message,
                    });
                });
            }
        }
    }
</script>

<style>

</style>