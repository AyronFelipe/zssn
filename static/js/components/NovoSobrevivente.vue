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
                                <div class="card-body"></div>
                                <div class="card-action">
                                    <button class="btn btn-primary pull-right"><i class="fas fa-save mr-1"></i> Salvar</button>
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

    export default {
        name: 'inicial',
        components: {
            Header,
            Sidebar
        }
    }
</script>

<style>

</style>