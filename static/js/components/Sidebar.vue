<template>
    <div class="sidebar sidebar-style-2">
        <div class="sidebar-wrapper scrollbar scrollbar-inner">
            <div class="sidebar-content">
                <ul class="nav nav-primary">
                    <li class="nav-item active">
                        <router-link to="/">
                            <i class="fas fa-home"></i>
                            <p>Início</p>
                        </router-link>
                    </li>
                    <li class="nav-item">
                        <router-link to="/novo-sobrevivente/">
                            <i class="fas fa-plus"></i>
                            <p>Novo sobrevivente</p>
                        </router-link>
                    </li>
                    <li class="nav-item">
                        <router-link to="/atualizar-local/">
                            <i class="fas fa-map-marked-alt"></i>
                            <p>Atualizar local</p>
                        </router-link>
                    </li>
                    <li class="nav-item">
                        <router-link to="/informar-infectado/">
                            <i class="fas fa-atom"></i>
                            <p>Informar infectado</p>
                        </router-link>
                    </li>
                    <li class="nav-item">
                        <router-link to="/trocar-itens/">
                            <i class="fas fa-handshake"></i>
                            <p>Trocar itens</p>
                        </router-link>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'Sidebar'
    }
</script>