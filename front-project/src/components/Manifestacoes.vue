<template>
  <div class="home">
    <h1 class="text-principal">Manifestações</h1>
    <button @click="carregarManifestacoes">Carregar Manifestações</button>

    <div v-if="manifestacoes.length" class="card-container">
      <div
        class="card"
        v-for="manifestacao in manifestacoes"
        :key="manifestacao.codigo"
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

            <!-- Botão Editar -->
            <button @click="habilitarEdicao" class="btn btn-warning">Editar</button>

            <!-- Botão Excluir -->
            <button @click="excluirManifestacao(modalManifestacao.codigo)" class="btn btn-danger ms-2">
              Excluir
            </button>

            <!-- Formulário de edição visível apenas se `editando` for true -->
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

const manifestacoes = ref([]);
const modalAberto = ref(false);
const modalManifestacao = ref({});
const editando = ref(false);
const novaDescricao = ref('');
const novoAutor = ref('');
const novaCategoria = ref('');

const carregarManifestacoes = async () => {
  try {
    const response = await axios.get('/manifestacoes');
    manifestacoes.value = response.data;
  } catch (error) {
    console.error('Erro ao carregar manifestações:', error);
  }
};

const abrirModal = (manifestacao) => {
  modalManifestacao.value = { ...manifestacao };
  modalAberto.value = true;
  editando.value = false; // Garante que o formulário começa oculto
};

const fecharModal = () => {
  modalAberto.value = false;
  modalManifestacao.value = {};
  editando.value = false;
};

const habilitarEdicao = () => {
  novaDescricao.value = modalManifestacao.value.descricao;
  novoAutor.value = modalManifestacao.value.autor;
  novaCategoria.value = modalManifestacao.value.categoria;
  editando.value = true;
};

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

const excluirManifestacao = async (codigo) => {
  try {
    await axios.delete(`/manifestacoes/${codigo}`);
    fecharModal();
    carregarManifestacoes(); // Recarrega a lista após exclusão
  } catch (error) {
    console.error('Erro ao excluir manifestação:', error);
  }
};

const cadastrarManifestacao = async () => {
  try {
    const novaManifestacao = {
      autor: novoAutor.value,
      descricao: novaDescricao.value,
      categoria: novaCategoria.value,
    };

    await axios.post('/manifestacoes', novaManifestacao);

    // Limpar os campos após o cadastro
    novoAutor.value = '';
    novaDescricao.value = '';
    novaCategoria.value = 'RECLAMACAO';

    // Atualiza a lista
    carregarManifestacoes();
  } catch (error) {
    console.error('Erro ao cadastrar manifestação:', error);
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

.card-container {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 20px;
  margin-top: 2rem;
}

.card {
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
}

.card:hover {
  transform: translateY(-5px);
}

button {
  background-color: #42b983;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #368a6e;
}

/* Modal styles */
.modal-content {
  max-width: 500px;
  margin: auto;
}

.modal-header, .modal-footer {
  padding: 10px;
}

textarea, input, select {
  width: 100%;
  padding: 10px;
  margin-bottom: 15px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

textarea:focus, input:focus, select:focus {
  border-color: #42b983;
  outline: none;
}
.modal-content {
  color: black;
}
</style>
