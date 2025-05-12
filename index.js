const prompt = require('prompt-sync')({ sigint: true });
const UsuarioService = require('./services/usuarioService');
const DeporteService = require('./services/deporteService');

async function mostrarMenu() {
  console.log('\n=== MENÚ PRINCIPAL ===');
  console.log('1. Ver todos los usuarios');
  console.log('2. Crear un nuevo usuario');
  console.log('3. Actualizar un usuario');
  console.log('4. Eliminar un usuario');
  console.log('5. Ver todos los deportes');
  console.log('6. Crear un nuevo deporte');
  console.log('7. Actualizar un deporte');
  console.log('8. Eliminar un deporte');
  console.log('9. Salir');
  const opcion = prompt('Seleccione una opción: ');
  return opcion;
}

async function main() {
  let salir = false;

  while (!salir) {
    const opcion = await mostrarMenu();

    switch (opcion) {
      case '1':
        const usuarios = await UsuarioService.getAllUsuarios();
        console.log('\n--- USUARIOS ---');
        console.log(usuarios);
        break;

      case '2':
        const nuevoUsuario = {
          id_usuario: prompt('ID de usuario: '),
          nombre: prompt('Nombre: '),
          correo: prompt('Correo: '),
          contraseña: prompt('Contraseña: '),
          saldo_disponible: parseFloat(prompt('Saldo disponible: ')),
        };
        console.log('Creando usuario...');
        console.log(await UsuarioService.crearUsuario(nuevoUsuario));
        break;

      case '3':
      const idActualizar = parseInt(prompt('ID del usuario a actualizar: '));
      const datosActualizar = {
        nombre: prompt('Nuevo nombre: '),
        correo: prompt('Nuevo correo: '),
        contraseña: prompt('Nueva contraseña: '),
        saldo_disponible: parseFloat(prompt('Nuevo saldo disponible: ')),
        };
        console.log('Actualizando usuario...');
        console.log(await UsuarioService.actualizarUsuario(idActualizar, datosActualizar));
        break;


      case '4':
        const idEliminar = prompt('ID del usuario a eliminar: ');
        console.log(await UsuarioService.eliminarUsuario(idEliminar));
        break;

      case '5':
        const deportes = await DeporteService.getAllDeportes();
        console.log('\n--- DEPORTES ---');
        console.log(deportes);
        break;

      case '6':
        const nuevoDeporte = {
          id_deporte: prompt('ID de deporte: '),
          nombre_deporte: prompt('Nombre del deporte: '),
        };
        console.log('Creando deporte...');
        console.log(await DeporteService.crearDeporte(nuevoDeporte));
        break;

      case '7':
        const idDeporteActualizar = prompt('ID del deporte a actualizar: ');
        const datosActualizarDeporte = {
          id_deporte: idDeporteActualizar,
          nombre_deporte: prompt('Nuevo nombre del deporte: '),
        };
        console.log('Actualizando deporte...');
        console.log(await DeporteService.actualizarDeporte(idDeporteActualizar, datosActualizarDeporte));
        break;

      case '8':
        const idDeporteEliminar = prompt('ID del deporte a eliminar: ');
        console.log('Eliminando deporte...');

        // Llamada a eliminarDeporte con el idDeporte
        console.log(await DeporteService.eliminarDeporte(idDeporteEliminar));
        break;

      case '9':
        console.log('Saliendo del programa...');
        salir = true;
        break;

      default:
        console.log('Opción inválida, intenta de nuevo.');
    }
  }
}

main();