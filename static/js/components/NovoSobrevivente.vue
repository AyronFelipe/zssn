<template>
    <div class="wrapper">
        <Header />
        <Sidebar />
        <div class="main-panel">
            <div class="content">
                <div class="page-inner">
                    <div class="page-header">
                        <h4 class="page-title">Novo sobrevivente</h4>
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
                                <router-link to="/novo-sobrevivente/">
                                    Novo sobrevivente
                                </router-link>
                            </li>
                        </ul>
                    </div>
                    <div class="row">
                        <div class="col-md-12">
                            <div class="card">
                                <div class="card-header">
                                    <div class="card-title">Dados do novo sobrevivente</div>
                                </div>
                                <form v-on:submit.prevent="onSubmit">
                                    <div class="card-body">
                                        <div class="row">
                                            <div class="col-lg-4 col-md-4 col-12">
                                                <div class="form-group">
                                                    <label for="nome">Nome <span class="required-label">*</span></label>
                                                    <input required="" type="text" maxlength="255" placeholder="Digite seu nome" class="form-control" name="nome" v-model="nome">
                                                </div>
                                            </div>
                                            <div class="col-lg-4 col-md-4 col-12">
                                                <div class="form-group">
                                                    <label for="idade">Idade <span class="required-label">*</span></label>
                                                    <input required="" type="number" min="0" placeholder="Digite sua idade" class="form-control" name="idade" v-model="idade">
                                                </div>
                                            </div>
                                            <div class="col-lg-4 col-md-4 col-12">
                                                <div class="form-check">
                                                    <label>Sexo <span class="required-label">*</span></label><br>
                                                    <label class="form-radio-label">
                                                        <input class="form-radio-input" type="radio" name="sexo" value="M" checked="" v-model="sexo">
                                                        <span class="form-radio-sign">Masculino</span>
                                                    </label>
                                                    <label class="form-radio-label ml-3">
                                                        <input class="form-radio-input" type="radio" name="sexo" value="F" v-model="sexo">
                                                        <span class="form-radio-sign">Feminino</span>
                                                    </label>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="row">
                                            <div class="col-md-6 col-12">
                                                <div class="form-group">
                                                    <label for="latitude">Latitude <span class="required-label">*</span></label>
                                                    <input required="" type="text" placeholder="Digite a latitude da sua posição atual" class="form-control" name="latitude" id="latitude" v-model="latitude">
                                                </div>
                                            </div>
                                            <div class="col-md-6 col-12">
                                                <div class="form-group">
                                                    <label for="longitude">Longitude <span class="required-label">*</span></label>
                                                    <input required="" type="text" placeholder="Digite a longitude da sua posição atual" class="form-control" name="longitude" id="longitude" v-model="longitude">
                                                </div>
                                            </div>
                                        </div>
                                        <legend class="ml-4">Itens</legend>
                                        <div class="row">
                                            <div class="col-12">
                                                <div class="table-responsive">

                                                    <table class="table">
                                                        <thead>
                                                            <tr>
                                                                <th>Item</th>
                                                                <th>Quantidade</th>
                                                                <th></th>
                                                            </tr>
                                                        </thead>
                                                        <tbody>
                                                            <tr v-for="(linha, index) in linhas" :key="index" :linha="linha">
                                                                <td>
                                                                    <div class="form-group">
                                                                        <select name="item" id="" class="form-control" v-model="linha.id">
                                                                            <option v-for="item in itens" :value="item.pk" :key="item.pk">
                                                                                {{ item.nome }}
                                                                            </option>
                                                                        </select>
                                                                    </div>
                                                                </td>
                                                                <td>
                                                                    <div class="form-group">
                                                                        <input type="number" min="1" class="form-control" placeholder="Quantidade que você possui desse item" v-model="linha.quantidade">
                                                                    </div>
                                                                </td>
                                                                <td>
                                                                    <button class="btn btn-danger" v-on:click="excluirItem(index)" type="button">Excluir</button>
                                                                </td>
                                                            </tr>
                                                        </tbody>
                                                        <tfoot>
                                                            <tr>
                                                                <td colspan="3">
                                                                    <button v-on:click="addItem" type="button" class="btn btn-primary btn-sm">Adicionar item</button>
                                                                </td>
                                                            </tr>
                                                        </tfoot>
                                                    </table>
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
    import Inputmask from "inputmask";
    import { api } from '../api/http-common';
    import Swal from 'sweetalert2'

    export default {
        name: 'inicial',
        components: {
            Header,
            Sidebar
        },
        data() {
            return {
                itens: [],
                linhas: [],
                nome: '',
                idade: '',
                sexo: '',
                latitude: '',
                longitude: '',
            }
        },
        mounted() {
            var selector = document.getElementById("latitude");
            var im = new Inputmask("99° 99' 99\"");
            im.mask(selector);
            var selector = document.getElementById("longitude");
            var im = new Inputmask("99° 99' 99\"");
            im.mask(selector);
        },
        created() {
            api.get(`itens/`)
            .then(res => {
                this.itens = res.data
            })
            .catch(e => {
                console.log(e);
            })
        },
        methods: {
            addItem() {
                let obj = {
                    itens: this.itens,
                }
                this.linhas.push(obj);

            },
            excluirItem(index) {
                this.linhas.splice(index, 1);
            },
            onSubmit() {
               let body = {
                   nome: this.nome,
                   idade: this.idade,
                   sexo: this.sexo,
                   latitude: this.latitude,
                   longitude: this.longitude,
                   linhas: this.linhas,
               }

                api.post('sobreviventes/', body)
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
                })
            }
        }
    }
</script>

<style>

</style>