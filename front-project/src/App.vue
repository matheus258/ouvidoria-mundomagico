<script setup>
import HomePage from './components/HomePage.vue';
import CadastrarManifestacao from './components/CadastrarManifestacao.vue';
import Manifestacoes from './components/Manifestacoes.vue';

</script>

<template>
  <div class="container">
    <HomePage />
    <CadastrarManifestacao />
    <Manifestacoes />
  </div>
</template>

<style scoped>
header {
  line-height: 1.5;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
