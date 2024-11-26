import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../components/HomePage.vue';
import CadastrarManifestacao from '../components/CadastrarManifestacao.vue';
import Manifestacoes from '../components/Manifestacoes.vue';

const routes = [
  { path: '/', component: HomePage },
  { path: '/cadastrar', component: CadastrarManifestacao },
  { path: '/manifestacoes', component: Manifestacoes },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
