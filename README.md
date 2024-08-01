# Login System with Flask

Este proyecto es una aplicación web simple de inicio de sesión y registro utilizando **Flask**, **Python**, **HTML** y **CSS**. La aplicación permite a los usuarios registrarse con un nombre de usuario y una contraseña, y luego iniciar sesión con esas credenciales. Los datos de usuario se almacenan en un archivo JSON.

## Características

- **Registro de usuario:** Permite a los usuarios crear una cuenta con un nombre de usuario y una contraseña.
- **Inicio de sesión:** Los usuarios pueden iniciar sesión con sus credenciales registradas.
- **Validación:** Mensajes de error claros cuando las credenciales son incorrectas.
- **Interfaz de usuario moderna:** Diseño limpio y atractivo utilizando CSS.

## Requisitos

- Python 3.x
- Flask

## Instalación

1. **Clona el repositorio:**

    ```sh
    git clone https://github.com/tu-usuario/nombre-del-repositorio.git
    cd nombre-del-repositorio
    ```

2. **Instala Flask:**

    ```sh
    pip install Flask
    ```

## Estructura del Proyecto

- **`/static/style.css`**: Archivo CSS con el diseño moderno de la aplicación.
- **`/templates/login.html`**: Página de inicio de sesión.
- **`/templates/register.html`**: Página de registro de usuarios.
- **`/templates/success.html`**: Página que muestra un mensaje de éxito después de iniciar sesión correctamente.
- **`app.py`**: Archivo principal de la aplicación Flask que gestiona las rutas y la lógica.
- **`users.json`**: Archivo que almacena los datos de los usuarios registrados.

## Uso

1. **Ejecuta la aplicación:**

    ```sh
    python app.py
    ```

2. **Abre tu navegador y visita:**

    - `http://127.0.0.1:5000/register` para registrarte.
    - `http://127.0.0.1:5000/login` para iniciar sesión.
    - Si el inicio de sesión es exitoso, serás redirigido a `http://127.0.0.1:5000/success`.

