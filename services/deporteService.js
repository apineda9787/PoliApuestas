const fetch = (...args) => import('node-fetch').then(({ default: fetch }) => fetch(...args));

const API_BASE_URL = 'http://localhost:5000'; // Cambia si tu API tiene otro host

const DeporteService = {
  getAllDeportes: async () => {
    const res = await fetch(`${API_BASE_URL}/getSports`);
    return res.json();
  },

  crearDeporte: async (deporte) => {
    const res = await fetch(`${API_BASE_URL}/createSport`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(deporte),
    });
    return res.json();
  },

  actualizarDeporte: async (id, deporte) => {
    const deporteConId = { id_deporte: id, ...deporte };
    const res = await fetch(`${API_BASE_URL}/updateSport`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(deporteConId),
    });
    return res.json();
  },

  eliminarDeporte: async (id) => {
  const res = await fetch(`${API_BASE_URL}/deleteSport`, {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json', // Asegúrate de enviar el tipo de contenido correcto
    },
    body: JSON.stringify({ id_deporte: id }), // Enviar el id_deporte en el cuerpo de la solicitud
  });

  if (!res.ok) {
    const error = await res.text();
    console.error('Error al eliminar el deporte:', error);
    return { error: 'No se pudo eliminar el deporte' };
  }
  
  return res.json();
}
};
module.exports = DeporteService;
