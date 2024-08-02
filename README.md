# Login System with Flask

Este proyecto es una aplicación web simple de gestión de usuarios utilizando **Flask**, **Python**, **HTML**, **CSS** y **MySQL**. La aplicación permite a los usuarios registrarse, iniciar sesión y, para los administradores, visualizar la lista de usuarios. También incluye funcionalidades modernas como mostrar/ocultar contraseña y un diseño estilizado.

## Características

- **Registro de usuario:** Permite a los usuarios crear una cuenta con un nombre de usuario y una contraseña.
- **Inicio de sesión:** Los usuarios pueden iniciar sesión con sus credenciales registradas.
- **Validación:** Mensajes de error claros cuando las credenciales son incorrectas o el nombre de usuario ya existe.
- **Inicio de sesión de administrador:** Permite a los administradores ver una lista de todos los usuarios registrados.
- **Interfaz de usuario moderna:** Diseño limpio y atractivo utilizando CSS.
- **Mostrar/Ocultar contraseña:** Funcionalidad para mostrar u ocultar la contraseña en los campos de entrada.

## Requisitos

- Python 3.x
- Flask
- MySQL
- Paquetes de Python listados en `requirements.txt`

## Uso

1. **Abre tu navegador y visita:**

    - `http://127.0.0.1:5000/register` para registrarte.
    - `http://127.0.0.1:5000/login` para iniciar sesión.
    -  Si el inicio de sesión es exitoso, serás redirigido a `http://127.0.0.1:5000/success`.
    - `http://127.0.0.1:5000/admin_login` para iniciar sesión como administrador y ver el listado de usuarios.
    

## Estructura del Proyecto

- **`/static/style.css`**: Archivo CSS con el diseño moderno de la aplicación.
- **`/static/script.js`**: Archivo JavaScript para funcionalidades como mostrar/ocultar contraseña.
- **`/templates/login.html`**: Página de inicio de sesión de usuario.
- **`/templates/register.html`**: Página de registro de usuarios.
- **`/templates/success.html`**: Página que muestra un mensaje de éxito después de iniciar sesión correctamente.
- **`/templates/admin_login.html`**: Página de inicio de sesión de administrador.
- **`/templates/view_users.html`**: Página de visualización de la lista de usuarios para administradores.
- **`app.py`**: Archivo principal de la aplicación Flask que gestiona las rutas y la lógica.
- **`Config.py`**: Archivo de configuración de la aplicación.


