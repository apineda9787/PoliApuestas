# 🏃‍♂️ Proyecto Flask API - CRUD de Usuarios y Deportes

Este proyecto es una API RESTful construida con **Python + Flask + SQLAlchemy**, que permite realizar operaciones CRUD sobre dos entidades: **Usuarios** y **Deportes**.

## 📦 Tecnologías utilizadas

- [Flask](https://flask.palletsprojects.com/) - Microframework web de Python.
- [SQLAlchemy](https://www.sqlalchemy.org/) - ORM para gestionar la base de datos.
- [MySQL] - Motor de base de datos.
- [Postman](https://www.postman.com/) - Para pruebas de endpoints.

---

## 🚀 ¿Cómo ejecutar el proyecto?

1. Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/nombre-repo.git
cd nombre-repo
```

2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

3. Ejecuta la API:

```bash
python app.py
```

## 📌 Endpoints disponibles

### 🔹 Usuarios

| Método | Endpoint      | Descripción                |
| ------ | ------------- | -------------------------- |
| GET    | `/getUsers`   | Obtener todos los usuarios |
| POST   | `/createUser` | Crear un nuevo usuario     |
| PUT    | `/updateUser` | Actualizar un usuario      |
| DELETE | `/deleteUser` | Eliminar un usuario        |

### 🔹 Deportes

| Método | Endpoint       | Descripción                |
| ------ | -------------- | -------------------------- |
| GET    | `/getSports`   | Obtener todos los deportes |
| POST   | `/createSport` | Crear un nuevo deporte     |
| PUT    | `/updateSport` | Actualizar un deporte      |
| DELETE | `/deleteSport` | Eliminar un deporte        |

---

## 📄 Estructura del Proyecto

```
📁 model/
   ├── Usuario.py
   └── Deporte.py

📁 database/
   └── db.py

📄 app.py
📄 README.md
📄 requirements.txt
```

---

## 🛠 Ejemplo de datos para pruebas (JSON)

### Crear Usuario

```json
{
  "id_usuario": 1,
  "nombre": "Juan",
  "correo": "juan@email.com",
  "contraseña": "1234",
  "saldo_disponible": 1000.0
}
```

### Crear Deporte

```json
{
  "id_deporte": 1,
  "nombre_deporte": "Fútbol"
}
```

---

## ✨ Autor

- 💼 Proyecto desarrollado por [Tu Nombre](https://github.com/chartorresgg)
- 📧 Contacto: chartorresg@gmail.com

---

## 📝 Licencia

Este proyecto está licenciado bajo la [MIT License](LICENSE).
