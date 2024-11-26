<template>
  <div class="pagerouter">
    <PagesRouter />
  </div>

  <div class="home">
    <h1 class="text-principal">Manifestações</h1>

    <button @click="carregarManifestacoes" class="carregar-btn">Carregar Manifestações</button>

    <!-- Filtros -->
    <div class="filter-container">
      <!-- Filtro de Categoria -->
      <select v-model="filtroCategoria" class="form-control filtro-categoria">
        <option value="">Filtrar por categoria</option>
        <option value="RECLAMACAO">Reclamação</option>
        <option value="SUGESTAO">Sugestão</option>
        <option value="ELOGIO">Elogio</option>
        <option value="DENUNCIA">Denúncia</option>
        <option value="INFORMACAO">Informação</option>
        <option value="OUTROS">Outros</option>
      </select>
      <button class="pesquisar-btn" @click="filtrarPorCategoria">Pesquisar por Categoria</button>
    </div>

    <!-- Aviso caso não haja seleção -->
    <div v-if="naoSelecionado" class="aviso">
      Por favor, selecione uma categoria para filtrar.
    </div>

    <div v-if="manifestacoes.length" class="card-container">
      <div
        class="card"
        v-for="manifestacao in manifestacoes"
        :key="manifestacao.codigo"
        :style="`border-color: ${getCategoriaBorderColor(manifestacao.categoria)}; border-width: 3px;`"
        style="width: 18rem;"
        @click="abrirModal(manifestacao)"
      >
        <div class="card-body">
          <h5 class="card-title">{{ manifestacao.categoria }}</h5>
          <p class="card-text">{{ manifestacao.descricao }}</p>
        </div>
      </div>
    </div>

    <!-- Modal -->
    <div class="modal fade show" v-if="modalAberto" style="display: block;">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Detalhes da Manifestação</h5>
            <button type="button" class="btn-close" @click="fecharModal"></button>
          </div>
          <div class="modal-body">
            <p><strong>Descrição:</strong> {{ modalManifestacao.descricao }}</p>
            <p><strong>Autor:</strong> {{ modalManifestacao.autor }}</p>
            <p><strong>Categoria:</strong> {{ modalManifestacao.categoria }}</p>

            <!-- Botões Editar e Excluir -->
            <div class="button-group">
              <button @click="habilitarEdicao" class="btn btn-warning">Editar</button>
              <button @click="excluirManifestacao(modalManifestacao.codigo)" class="btn btn-danger ms-2">Excluir</button>
            </div>

            <!-- Formulário de Edição -->
            <div v-if="editando" class="mt-3">
              <div class="form-group">
                <label for="descricao">Descrição:</label>
                <textarea v-model="novaDescricao" class="form-control" rows="4"></textarea>
              </div>
              <div class="form-group">
                <label for="autor">Autor:</label>
                <input type="text" v-model="novoAutor" class="form-control" />
              </div>
              <div class="form-group">
                <label for="categoria">Categoria:</label>
                <select v-model="novaCategoria" class="form-control">
                  <option value="RECLAMACAO">Reclamação</option>
                  <option value="SUGESTAO">Sugestão</option>
                  <option value="ELOGIO">Elogio</option>
                  <option value="DENUNCIA">Denúncia</option>
                  <option value="INFORMACAO">Informação</option>
                  <option value="OUTROS">Outros</option>
                </select>
              </div>
            </div>
          </div>
          <div class="modal-footer">
            <button v-if="editando" @click="editarManifestacao(modalManifestacao.codigo)" class="btn btn-primary">Salvar</button>
            <button @click="fecharModal" class="btn btn-secondary">Fechar</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from '../api/http-common';
import PagesRouter from './PagesRouter.vue';

const manifestacoes = ref([]);
const modalAberto = ref(false);
const modalManifestacao = ref({});
const editando = ref(false);
const novaDescricao = ref('');
const novoAutor = ref('');
const novaCategoria = ref('');
const filtroCategoria = ref('');
const naoSelecionado = ref(false); // Flag para exibir a mensagem de aviso

// Carregar manifestações
const carregarManifestacoes = async () => {
  try {
    const response = await axios.get('/manifestacoes');
    manifestacoes.value = response.data;
  } catch (error) {
    console.error('Erro ao carregar manifestações:', error);
  }
};

// Abrir modal
const abrirModal = (manifestacao) => {
  modalManifestacao.value = { ...manifestacao };
  modalAberto.value = true;
  editando.value = false; // Garante que o formulário começa oculto
};

// Fechar modal
const fecharModal = () => {
  modalAberto.value = false;
  modalManifestacao.value = {};
  editando.value = false;
};

// Habilitar edição
const habilitarEdicao = () => {
  novaDescricao.value = modalManifestacao.value.descricao;
  novoAutor.value = modalManifestacao.value.autor;
  novaCategoria.value = modalManifestacao.value.categoria;
  editando.value = true;
};

// Editar manifestação
const editarManifestacao = async (codigo) => {
  try {
    const dadosAtualizados = {
      descricao: novaDescricao.value,
      autor: novoAutor.value,
      categoria: novaCategoria.value,
    };
    await axios.put(`/manifestacoes/${codigo}`, dadosAtualizados);
    fecharModal();
    carregarManifestacoes(); // Recarrega a lista
  } catch (error) {
    console.error('Erro ao editar manifestação:', error);
  }
};

// Excluir manifestação
const excluirManifestacao = async (codigo) => {
  try {
    await axios.delete(`/manifestacoes/${codigo}`);
    fecharModal();
    carregarManifestacoes(); // Recarrega a lista após exclusão
  } catch (error) {
    console.error('Erro ao excluir manifestação:', error);
  }
};

// Função para filtrar por categoria
const filtrarPorCategoria = async () => {
  try {
    if (!filtroCategoria.value) {
      naoSelecionado.value = true; // Exibe a mensagem de aviso
      return;
    }

    const response = await axios.get('/manifestacoes/pesquisar', {
      params: { categoria: filtroCategoria.value }
    });
    manifestacoes.value = response.data;
    naoSelecionado.value = false; // Esconde a mensagem de aviso
  } catch (error) {
    console.error("Erro ao pesquisar por categoria:", error);
    alert("Erro ao buscar por categoria. Tente novamente.");
  }
};

// Função para retornar a cor da borda de acordo com a categoria
const getCategoriaBorderColor = (categoria) => {
  switch (categoria) {
    case 'RECLAMACAO':
      return 'red';
    case 'SUGESTAO':
      return 'blue';
    case 'ELOGIO':
      return 'green';
    case 'DENUNCIA':
      return 'orange';
    case 'INFORMACAO':
      return 'purple';
    case 'OUTROS':
      return 'gray';
    default:
      return 'black'; // Cor padrão
  }
};

onMounted(() => {
  carregarManifestacoes();
});
</script>

<style scoped>
.home {
  text-align: center;
  margin-top: 2rem;
}

.text-principal {
  margin-bottom: 25px;
  font-family: "Montserrat", serif;
  font-optical-sizing: auto;
  font-size: 2.8em;
  text-align: center;
}

.carregar-btn {
  background-color: #42b983;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 1rem;
  line-height: 1.5;
  margin-top: 20px;
  margin-bottom: 20px;
}
.pesquisar-btn {
  background-color: #42b983;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;

}

.carregar-btn:hover {
  background-color: #368a6e;
}

.card-container {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 20px;
  margin-top: 40px; /* Ajusta o espaçamento entre o filtro e as manifestações */
}

.card {
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s;
  padding: 20px;
  border-radius: 8px;
}

.card:hover {
  transform: scale(1.05);
}

.filter-container {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.filtro-categoria {
  width: 200px;
  margin-right: 15px;
}

.aviso {
  color: red;
  font-size: 1.2rem;
  margin-top: 20px;
}

.modal-header {
  background-color: #f8f9fa;
  border-bottom: 1px solid #ddd;
}

.modal-body {
  padding: 20px;
}

.modal-footer {
  background-color: #f8f9fa;
  border-top: 1px solid #ddd;
}

.button-group {
  display: flex;
  gap: 10px;
  justify-content: center;
}
</style>
