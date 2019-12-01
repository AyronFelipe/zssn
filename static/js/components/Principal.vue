<template>
    <div class="wrapper">
        <Sidebar />
        <Header />
    </div>
</template>
<script>
    import Sidebar from './Sidebar'
    import Header from './Header'

    export default {
        components: {
            Sidebar,
            Header
        },
        data() {
            return {
                sobreviventes: []
            }
        },
    }
</script>