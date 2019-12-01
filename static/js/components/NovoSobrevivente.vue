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
                                <form>
                                    <div class="card-body">
                                        <div class="row">
                                            <div class="col-lg-4 col-md-4 col-12">
                                                <div class="form-group">
                                                    <label for="nome">Nome <span class="required-label">*</span></label>
                                                    <input required="" type="text" maxlength="255" placeholder="Digite seu nome" class="form-control" name="nome">
                                                </div>
                                            </div>
                                            <div class="col-lg-4 col-md-4 col-12">
                                                <div class="form-group">
                                                    <label for="idade">Idade <span class="required-label">*</span></label>
                                                    <input required="" type="number" min="0" placeholder="Digite sua idade" class="form-control" name="idade">
                                                </div>
                                            </div>
                                            <div class="col-lg-4 col-md-4 col-12">
                                                <div class="form-check">
                                                    <label>Sexo <span class="required-label">*</span></label><br>
                                                    <label class="form-radio-label">
                                                        <input required="" class="form-radio-input" type="radio" name="sexo" value="M" checked="">
                                                        <span class="form-radio-sign">Masculino</span>
                                                    </label>
                                                    <label class="form-radio-label ml-3">
                                                        <input required="" class="form-radio-input" type="radio" name="sexo" value="F">
                                                        <span class="form-radio-sign">Feminino</span>
                                                    </label>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="row">
                                            <div class="col-md-6 col-12">
                                                <div class="form-group">
                                                    <label for="latitude">Latitude <span class="required-label">*</span></label>
                                                    <input required="" type="text" maxlength="10" placeholder="Digite a latitude da sua posição atual" class="form-control" name="latitude" id="latitude">
                                                </div>
                                            </div>
                                            <div class="col-md-6 col-12">
                                                <div class="form-group">
                                                    <label for="longitude">Longitude <span class="required-label">*</span></label>
                                                    <input required="" type="text" maxlength="10" placeholder="Digite a longitude da sua posição atual" class="form-control" name="longitude" id="longitude">
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="card-action">
                                        <button type="submit" class="btn btn-primary pull-right"><i class="fas fa-save mr-1"></i> Salvar</button>
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

    export default {
        name: 'inicial',
        components: {
            Header,
            Sidebar
        },
        mounted: function() {
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