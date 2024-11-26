<!-- <template>
  <div class="home-page">
    <h1 class="text-principal">Bem-vindo</h1>
    <PagesRouter />
  </div>
</template>

<script setup>
import PagesRouter from './PagesRouter.vue';


</script>

<style scoped>
  .home-page{
    text-align: center;
  }
  .text-principal {
    margin-bottom: 25px;
    font-family: "Montserrat", serif;
    font-optical-sizing: auto;
    font-size: 2.8em;
  }
</style> -->

<template>
  <div class="home-page">   
    <PagesRouter />
    <h1 class="text-principal">Bem-vindo ao Nosso Site!</h1>
    <p class="description">
      Este é o espaço onde você pode compartilhar e consultar manifestações sobre diversos assuntos. 
      Seja uma <strong>reclamação</strong>, uma <strong>sugestão</strong>, ou até mesmo um <strong>elogio</strong>, 
      sua voz é importante e será ouvida! Navegue pelas categorias ou cadastre sua própria manifestação.
    </p>
    <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
    <div class="carousel-inner">
      <div class="carousel-item active">
        <img src="@/assets/img/kid_spider.png" class="d-block w-100" alt="Kid Spider">
      </div>
      <div class="carousel-item">
        <img src="@/assets/img/spidr_st.png" class="d-block w-100" alt="Spider ST">
      </div>
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Anterior</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Próximo</span>
    </button>
  </div>
 
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import PagesRouter from './PagesRouter.vue';

const router = useRouter();

const navigateToManifestacoes = () => {
  router.push({ name: 'manifestacoes' }); // Supondo que a rota para manifestações se chame 'manifestacoes'
};

const navigateToCadastro = () => {
  router.push({ name: 'cadastro-manifestacao' }); // Supondo que a rota de cadastro se chame 'cadastro-manifestacao'
};
</script>

<style scoped>
.home-page {
  text-align: center;
  padding: 30px;
}

.text-principal {
  margin-bottom: 20px;
  font-family: "Montserrat", serif;
  font-size: 2.8em;
  color: #333;
}

.description {
  margin-bottom: 30px;
  font-size: 1.2em;
  color: #555;
  line-height: 1.6;
}

.cta-container {
  display: flex;
  justify-content: center;
  gap: 20px;
  margin-top: 20px;
}

.cta-button {
  background-color: #42b983;
  color: white;
  padding: 12px 25px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 1rem;
}

.cta-button:hover {
  background-color: #368a6e;
}

.cta-button:focus {
  outline: none;
}
.carousel-item img {
  object-fit: contain; /* A imagem será redimensionada para caber totalmente no contêiner */
  width: 100%; /* Garante que a imagem preencha a largura do carrossel */
  height: 400px; /* Ajuste a altura do carrossel conforme necessário */
}
</style>
