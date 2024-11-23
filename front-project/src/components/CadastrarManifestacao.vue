<template>
  <div class="cadastrar">
    <h2>Cadastrar Manifestação</h2>
    <form @submit.prevent="cadastrarManifestacao">
      <div>
        <label for="autor">Autor:</label>
        <input type="text" v-model="autor" id="autor" required />
      </div>

      <div>
        <label for="categoria">Categoria:</label>
        <select v-model="categoria" id="categoria" required>
          <option value="" disabled selected>Escolha uma categoria</option>
          <option value="RECLAMACAO">Reclamação</option>
          <option value="SUGESTAO">Sugestão</option>
          <option value="ELOGIO">Elogio</option>
          <option value="DENUNCIA">Denúncia</option>
          <option value="INFORMACAO">Informação</option>
          <option value="OUTROS">Outros</option>
        </select>
      </div>

      <div>
        <label for="descricao">Descrição:</label>
        <textarea
          v-model="descricao"
          id="descricao"
          required
          maxlength="300"
          rows="4"
          placeholder="Digite a descrição da manifestação aqui..."
        ></textarea>
        <p :class="{ 'verde': descricao.length < 300, 'vermelho': descricao.length >= 300 }">
          {{ descricao.length }} / 300 caracteres
        </p>
      </div>

      <button type="submit">Cadastrar</button>
    </form>
    <p v-if="mensagem" :class="{ 'verde': mensagem.includes('sucesso'), 'vermelho': mensagem.includes('Erro') }">
      {{ mensagem }}
    </p>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from '../api/http-common';

const descricao = ref('');
const autor = ref('');
const categoria = ref('');
const mensagem = ref('');

const cadastrarManifestacao = async () => {
  try {
    if (!descricao.value || !autor.value || !categoria.value) {
      mensagem.value = 'Todos os campos devem ser preenchidos.';
      return;
    }

    const dados = {
      descricao: descricao.value,
      autor: autor.value,
      categoria: categoria.value,
    };

    await axios.post('/manifestacoes', dados);
    mensagem.value = 'Manifestação cadastrada com sucesso!';

    // Limpar o formulário
    descricao.value = '';
    autor.value = '';
    categoria.value = '';
  } catch (error) {
    console.error('Erro ao cadastrar manifestação:', error);

    // Tratar mensagens do backend se disponíveis
    if (error.response && error.response.data) {
      mensagem.value = `Erro: ${error.response.data.mensagem || 'Falha no servidor.'}`;
    } else {
      mensagem.value = 'Erro ao cadastrar a manifestação.';
    }
  }
};
</script>

<style scoped>
.cadastrar {
  max-width: 400px;
  margin: 50px auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

h2 {
  text-align: center;
  margin-bottom: 30px;
  font-size: 1.5rem;
  color: #333;
}

form {
  display: flex;
  flex-direction: column;
}

label {
  display: block;
  margin: 10px 0 5px;
  font-size: 1rem;
  font-weight: bold;
  color: #333;
}

textarea,
select,
input {
  width: 100%;
  box-sizing: border-box;
  padding: 10px;
  margin-bottom: 15px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 1rem;
  background-color: #fff;
  transition: border-color 0.3s ease;
}

textarea:focus,
select:focus,
input:focus {
  border-color: #42b983;
  outline: none;
}

button {
  margin-top: 15px;
  background-color: #42b983;
  color: white;
  padding: 12px 20px;
  border: none;
  border-radius: 5px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #368a6e;
}

p {
  text-align: center;
  font-size: 1rem;
  font-weight: bold;
}

.verde {
  color: green !important;
}

.vermelho {
  color: red !important;
}
</style>
