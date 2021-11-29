import axios from 'axios';

export default {
  namespaced: true,
  actions: {
    loadAllModulesForBrand(context, brand) {
      return axios.get('/api/brand/' + brand + '/modules');
    },
    doActionGrantSchemeList(context, { id, action }) {
      return axios.post('/api/user/' + id + '/' + action);
    },
    loadGrantSchemes() {
      return axios.get('/api/grant-schemes');
    },
    loadGrantScheme(context, id) {
      return axios.get('/api/grant-scheme/' + id);
    },
    deleteGrantScheme(context, id) {
      return axios.delete('/api/grant-scheme/' + id);
    },
    loadModulesFromGrantScheme(context, id) {
      return axios.get('/api/grant-scheme/' + id + '/modules');
    },
    loadUsersFromGrantScheme(context, id) {
      return axios.get('/api/grant-scheme/' + id + '/users');
    },
    loadSegments() {
      return axios.get('/api/segments');
    },
    updateGrantScheme(context, { id, data }) {
      return axios.put('/api/grant-scheme/' + id, data);
    },
    addGrantScheme(context, data) {
      return axios.post('api/grant-scheme', data);
    },
  }
};