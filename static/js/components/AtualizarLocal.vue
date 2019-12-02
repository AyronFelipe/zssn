<template>
    <div class="wrapper">
        <Header />
        <Sidebar />
        <div class="main-panel">
            <div class="content">
                <div class="page-inner">
                    <div class="page-header">
                        <div class="page-title">Atualizar local</div>
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
                                <router-link to="/atualizar-local/">
                                    Atualizar local
                                </router-link>
                            </li>
                        </ul>
                    </div>
                    <div class="row">
                        <div class="col-md-12">
                            <div class="card">
                                <div class="card-header">
                                    <div class="card-title">Atualizar local</div>
                                </div>
                                <form v-on:submit.prevent="onSubmit">
                                    <div class="card-body">
                                        <div class="row">
                                            <div class="col-md-6 col-12">
                                                <div class="form-group">
                                                    <label for="nome">Sobrevivente <span class="required-label">*</span></label>
                                                    <select name="" id="" v-model="sobrevivente" class="form-control" @change="onChange">
                                                        <option v-for="sobrevivente in sobreviventes" :key="sobrevivente.pk" :value="sobrevivente.pk">
                                                            {{ sobrevivente.nome }}
                                                        </option>
                                                    </select>
                                                </div>
                                            </div>
                                            <div class="col-md-6 col-12">
                                                <div class="form-group">
                                                    <p><strong>Latitude Atual:</strong> {{ latitude }}</p>
                                                    <p><strong>Longitude Atual:</strong> {{ longitude }}</p>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="row">
                                            <div class="col-md-6 col-12">
                                                <div class="form-group">
                                                    <label for="latitude">Nova Latitude<span class="required-label">*</span></label>
                                                    <input required="" type="text" placeholder="Digite a latitude da sua posição atual" class="form-control" name="latitude" id="latitude" v-model="nova_latitude">
                                                </div>
                                            </div>
                                            <div class="col-md-6 col-12">
                                                <div class="form-group">
                                                    <label for="longitude">Nova Longitude<span class="required-label">*</span></label>
                                                    <input required="" type="text" placeholder="Digite a longitude da sua posição atual" class="form-control" name="longitude" id="longitude" v-model="nova_longitude">
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
    import Inputmask from "inputmask";


    export default {
        name: 'atualizar_local',
        components: {
            Header,
            Sidebar
        },
        data() {
            return {
                sobrevivente: '',
                sobreviventes: [],
                latitude: '',
                longitude: '',
                nova_latitude: '',
                nova_longitude: '',
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
                })
            })
        },
        methods: {
            onChange() {
                api.get(`sobrevivente/${this.sobrevivente}/coordenadas/`)
                .then(res => {
                    this.latitude = res.data.latitude;
                    this.longitude = res.data.longitude;
                })
                .catch(error => {
                    console.log(error);
                })
            },
            onSubmit() {
                let body = {
                    sobrevivente: this.sobrevivente,
                    latitude: this.nova_latitude,
                    longitude: this.nova_longitude,
                }
                api.put(`sobreviventes/${this.sobrevivente}/`, body)
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
                        text: error.response.data.message
                    })
                })
            }
        },
        mounted() {
            var selector = document.getElementById("latitude");
            var im = new Inputmask("99° 99' 99\"");
            im.mask(selector);
            var selector = document.getElementById("longitude");
            var im = new Inputmask("99° 99' 99\"");
            im.mask(selector);
        }
    }
</script>

<style>

</style>