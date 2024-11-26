<template>
  <div class="container">
    <nav>
      <ul class="nav-list">
        <li><router-link to="/" class="nav-link">Página Principal</router-link></li>
        <li><router-link to="/cadastrar" class="nav-link">Cadastrar Manifestação</router-link></li>
        <li><router-link to="/manifestacoes" class="nav-link">Manifestações</router-link></li>
      </ul>
    </nav>
    <router-view></router-view>
  </div>
</template>

<script setup>
</script>

<style scoped>
.container {
  margin-top: 40px; /* Adicionando margem no topo para afastar o conteúdo da borda superior */
  padding: 20px;
}

.nav-list {
  list-style: none; /* Remove os pontos de decoração */
  padding: 0;
  margin: 0;
  display: flex; /* Exibe os itens lado a lado */
  justify-content: center;
  margin-bottom: 40px; /* Espaçamento inferior */
}

.nav-list li {
  margin-right: 20px; /* Espaço entre os itens */
  border: 2px solid #42b983; /* Borda visível o tempo todo */
  border-radius: 5px; /* Bordas arredondadas para um visual mais suave */
  padding: 8px 15px; /* Adicionando padding para espaçamento interno */
}

.nav-link {
  text-decoration: none; /* Remove a linha debaixo padrão */
  color: #333; /* Cor do texto */
  font-size: 1.2rem;
  font-weight: bold;
}

.nav-link:hover {
  text-decoration: underline; /* Adiciona a linha embaixo ao passar o mouse */
  color: #42b983; /* Cor da linha de foco */
}
</style>
