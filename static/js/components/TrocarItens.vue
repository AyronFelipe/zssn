<template>
    <div class="wrapper">
        <Header />
        <Sidebar />
        <div class="main-panel">
            <div class="content">
                <div class="page-inner">
                    <div class="page-header">
                        <div class="page-title">Trocar itens</div>
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
                                <router-link to="/trocar-itens/">
                                    Trocar itens
                                </router-link>
                            </li>
                        </ul>
                    </div>
                    <div class="row">
                        <div class="col-md-12">
                            <div class="card">
                                <div class="card-header">
                                    <div class="card-title">Trocar itens</div>
                                </div>
                                <form v-on:submit.prevent="onSubmit">
                                    <div class="card-body">
                                        <div class="row">
                                            <div class="col-12">
                                                <div class="form-group">
                                                    <label for="nome">Sobrevivente 1<span class="required-label">*</span></label>
                                                    <select name="" id="" v-model="sobrevivente1" class="form-control" @change="onChangeSobrevivente1">
                                                        <option v-for="sobrevivente in sobreviventes" :key="sobrevivente.pk" :value="sobrevivente.pk">
                                                            {{ sobrevivente.nome }}
                                                        </option>
                                                    </select>
                                                </div>
                                                <table class="table">
                                                    <thead>
                                                        <tr>
                                                            <th>Item</th>
                                                            <th>Quantidade</th>
                                                            <th>Valor unitário</th>
                                                            <th>Total</th>
                                                            <th></th>
                                                        </tr>
                                                    </thead>
                                                    <tbody>
                                                        <tr v-for="(item, index) in itens1" :key="index" :item="item">
                                                            <td>
                                                                <div class="form-group">
                                                                    <input type="hidden" class="form-control" v-model="item.item">
                                                                    <input type="text" class="form-control" :value="item.item_nome" readonly>
                                                                </div>
                                                            </td>
                                                            <td>
                                                                <div class="form-group">
                                                                    <input type="number" class="form-control" :max="item.quantidade_total" min="1" :v-model="item.quantidade" :placeholder="item.quantidade_total" @change="onChangeQuantidade1($event, index)">
                                                                </div>
                                                            </td>
                                                            <td>
                                                                <p>{{ item.valor }}</p>
                                                            </td>
                                                            <td>
                                                                <p>{{ item.quantidade * item.valor }} </p>
                                                            </td>
                                                            <td>
                                                                <button class="btn btn-danger" v-on:click="excluirItem1(index)" type="button">Excluir</button>
                                                            </td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </div>
                                        </div>
                                        <div class="d-flex justify-content-center">
                                            <div class="icon-preview" style="font-size: 1.8rem"><i class="fas fa-arrow-alt-circle-up"></i></div>
                                            <div class="icon-preview" style="font-size: 1.8rem"><i class="fas fa-arrow-alt-circle-down"></i></div>
                                        </div>
                                        <div class="row">
                                            <div class="col-12">
                                                <div class="form-group">
                                                    <label for="nome">Sobrevivente 2<span class="required-label">*</span></label>
                                                    <select name="" id="" v-model="sobrevivente2" class="form-control" @change="onChangeSobrevivente2">
                                                        <option v-for="sobrevivente in sobreviventes" :key="sobrevivente.pk" :value="sobrevivente.pk">
                                                            {{ sobrevivente.nome }}
                                                        </option>
                                                    </select>
                                                </div>
                                                <table class="table">
                                                    <thead>
                                                        <tr>
                                                            <th>Item</th>
                                                            <th>Quantidade</th>
                                                            <th>Valor unitário</th>
                                                            <th>Total</th>
                                                            <th></th>
                                                        </tr>
                                                    </thead>
                                                    <tbody>
                                                        <tr v-for="(item, index) in itens2" :key="index" :item="item">
                                                            <td>
                                                                <div class="form-group">
                                                                    <input type="hidden" class="form-control" v-model="item.item">
                                                                    <input type="text" class="form-control" :value="item.item_nome" readonly>
                                                                </div>
                                                            </td>
                                                            <td>
                                                                <div class="form-group">
                                                                    <input type="number" class="form-control" :max="item.quantidade_total" min="1" :v-model="item.quantidade" :placeholder="item.quantidade_total" @change="onChangeQuantidade2($event, index)">
                                                                </div>
                                                            </td>
                                                            <td>
                                                                <p>{{ item.valor }}</p>
                                                            </td>
                                                            <td>
                                                                <p>{{ item.valor * item.quantidade }}</p>
                                                            </td>
                                                            <td>
                                                                <button class="btn btn-danger" v-on:click="excluirItem2(index)" type="button">Excluir</button>
                                                            </td>
                                                        </tr>
                                                    </tbody>
                                                </table>
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
        name: 'trocar_itens',
        components: {
            Header,
            Sidebar
        },
        data() {
            return {
                sobreviventes: [],
                sobrevivente1: '',
                sobrevivente2: '',
                itens1: [],
                itens2: []
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
            onChangeSobrevivente1() {
                api.get(`sobrevivente/${this.sobrevivente1}/itens/`)
                .then(res => {
                    this.itens1 = res.data.itens;
                })
                .catch(error => {
                    Swal.fire({
                        icon: 'error',
                        title: 'Oops...',
                        text: error.response.data.message
                    })
                });
            },
            onChangeSobrevivente2() {
                api.get(`sobrevivente/${this.sobrevivente2}/itens/`)
                .then(res => {
                    this.itens2 = res.data.itens;
                })
                .catch(error => {
                    Swal.fire({
                        icon: 'error',
                        title: 'Oops...',
                        text: error.response.data.message
                    })
                });
            },
            excluirItem1(index) {
                this.itens1.splice(index, 1);
            },
            excluirItem2(index) {
                this.itens2.splice(index, 1);
            },
            onSubmit() {
                let body = {
                    sobrevivente1: this.sobrevivente1,
                    sobrevivente2: this.sobrevivente2,
                    itens1: this.itens1,
                    itens2: this.itens2,
                }

                api.post('trocar-itens/', body)
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
                    })
                })
            },
            onChangeQuantidade1(event, index) {
                this.itens1[index].quantidade = parseInt(event.target.value);
            },
            onChangeQuantidade2(event, index) {
                this.itens2[index].quantidade = parseInt(event.target.value);
            }
        }
    }
</script>