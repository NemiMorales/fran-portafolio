# Portafolio Francisco Muñoz

Portafolio profesional para Francisco Muñoz Urbina, chef ejecutivo, maestro chocolatero y pastelero.

El proyecto presenta su trayectoria, especialidades, creaciones y filosofía profesional en torno al chocolate.

## Descripción

Aplicación web desarrollada con Python y Django.

El proyecto comenzó utilizando información desde un archivo JSON. Posteriormente se incorporaron modelos Django, conexión local con MySQL/MariaDB y una interfaz de gestión para administrar las creaciones del portafolio.

La rama actual corresponde a:

```
feature/crud-mysql
```

# Tecnologías utilizadas

    Python
    Django 6.1
    HTML5
    CSS3
    JavaScript
    MySQL/MariaDB mediante XAMPP
    Django Admin
    Git y GitHub
    Claude Design
    Codex

# Funcionalidades principales

Página pública de presentación profesional.
Secciones de filosofía, especialidades, creaciones, logros, trayectoria, formación y contacto.
Diseño responsive.
Datos generales del portafolio cargados desde JSON.
Modelos Django preparados para trabajar con base de datos.
Conexión local con MySQL/MariaDB.
Gestión de creaciones mediante Django Admin.
CRUD personalizado para creaciones.
Creación de nuevos registros.
Edición de registros.
Activación y desactivación de creaciones.
Las creaciones desactivadas no aparecen en el portafolio público.
Autenticación para acceder a la interfaz de gestión.
Protección CSRF en los formularios.
Variables sensibles almacenadas en .env.local.

# Arquitectura actual

El proyecto utiliza dos fuentes de información:

    Datos generales
    JSON → View → Template → Portafolio público

    Creaciones
    MySQL → View → Template → Portafolio público

Actualmente, las creaciones se obtienen desde MySQL, mientras que algunas secciones generales continúan utilizando el archivo:

portafolio/data/fran.json

Esta transición permite incorporar la base de datos gradualmente sin perder la estructura original del proyecto.

# Modelos Django

El proyecto contiene modelos para representar:

    Perfil
    Contacto
    Categorías
    Creaciones
    Especialidades
    Logros
    Experiencias laborales
    Experiencias adicionales
    Cursos
    Estudios
    Conocimientos
    Idiomas

No todos los modelos tienen una interfaz CRUD personalizada. La gestión general de los modelos se realiza mediante Django Admin.

La interfaz CRUD personalizada se concentra en el modelo Creacion, porque corresponde a la colección principal que se muestra en el portafolio.

# Interfaz de gestión

La interfaz personalizada se encuentra en:

http://127.0.0.1:8000/gestion/creaciones/

Esta sección no está enlazada desde el portafolio público.

Permite:

    Ver las creaciones registradas.
    Crear una nueva creación.
    Editar una creación.
    Activar una creación.
    Desactivar una creación.

Las creaciones no se eliminan físicamente. Se utiliza el campo booleano activo para ocultarlas temporalmente del portafolio y permitir activarlas nuevamente en el futuro.

# Django Admin

El panel administrativo se encuentra en:

http://127.0.0.1:8000/admin/

Desde allí se pueden administrar los modelos registrados en:

portafolio/admin.py

Para acceder se necesita un usuario creado mediante:

python manage.py createsuperuser

# Configuración local con MySQL/MariaDB

La rama feature/crud-mysql utiliza MySQL/MariaDB mediante XAMPP.

1. Crear el entorno virtual
   python -m venv venv
   venv\Scripts\activate

2. Instalar las dependencias
   python -m pip install -r requirements.txt

Las principales dependencias utilizadas son:

    Django
    python-decouple
    mysqlclient

3. Iniciar XAMPP

En el panel de XAMPP:

    Iniciar el módulo MySQL.
    Apache solo es necesario para acceder a phpMyAdmin.
    Entrar a:
    http://localhost/phpmyadmin/
    Crear la base de datos:
    portafolio_db
    Crear un usuario local con permisos sobre esa base de datos.

4. Crear las variables de entorno

Crear un archivo .env.local en la raíz del proyecto, junto a manage.py.

Ejemplo:

DATABASE_NAME=portafolio_db
DATABASE_USER=fran_user
DATABASE_PASSWORD=TU_CLAVE_LOCAL
DATABASE_HOST=localhost
DATABASE_PORT=3306
DEBUG=True

El archivo .env.local no debe subirse al repositorio porque contiene información sensible.

5. Ejecutar las migraciones
   python manage.py makemigrations
   python manage.py migrate
6. Crear un usuario administrador
   python manage.py createsuperuser
7. Ejecutar el servidor
   python manage.py runserver

El portafolio público estará disponible en:

http://127.0.0.1:8000/

# Seguridad implementada

Las credenciales de la base de datos se almacenan en .env.local.
.env.local está incluido en .gitignore.
La interfaz de gestión requiere iniciar sesión.
Los formularios utilizan protección CSRF.
Las acciones de activar y desactivar requieren una solicitud POST.
La interfaz de gestión no está enlazada desde el portafolio público.
Las creaciones desactivadas no se muestran públicamente.
La base de datos SQLite local no se utiliza en esta rama.

# Uso de inteligencia artificial

La inteligencia artificial fue utilizada como herramienta de apoyo para el diseño y la implementación.

# Claude Design

Claude Design fue utilizado inicialmente para crear la propuesta visual del portafolio, considerando:

    La identidad profesional de Francisco.
    El concepto del chocolate como ingrediente técnico y emocional.
    La estética editorial, cálida, oscura y sofisticada.
    La estructura de las secciones del portafolio.
    La paleta de colores y el diseño responsive.

Posteriormente, se entregó a la misma herramienta la necesidad de crear una interfaz CRUD para gestionar las creaciones.

Claude Design adaptó el diseño del CRUD para mantener la misma identidad visual del portafolio y ajustarlo a la nueva estructura del proyecto Django.

# Codex

Codex fue utilizado como apoyo para:

    Revisar la estructura existente del proyecto.
    Integrar el frontend dentro de Django Templates.

La estructura general del proyecto, la configuración, las decisiones técnicas, las pruebas y la supervisión del resultado fueron realizadas por la desarrolladora.

# Estructura principal del proyecto

    fran-portafolio/
    │
    ├── manage.py
    ├── requirements.txt
    ├── .env.local
    ├── .gitignore
    │
    ├── config/
    │   ├── settings.py
    │   ├── urls.py
    │   ├── asgi.py
    │   └── wsgi.py
    │
    └── portafolio/
        ├── admin.py
        ├── apps.py
        ├── forms.py
        ├── models.py
        ├── tests.py
        ├── urls.py
        ├── views.py
        │
        ├── data/
        │   └── fran.json
        │
        ├── migrations/
        │
        ├── templates/
        │   └── portafolio/
        │       ├── home.html
        │       └── gestion/
        │           ├── base.html
        │           ├── creacion_form.html
        │           └── creaciones_lista.html
        │
        └── static/
            └── portafolio/
                ├── css/
                ├── js/
                └── img/

# Ramas del proyecto

La rama principal contiene la versión base del proyecto.

La rama actual contiene la implementación de MySQL:

main
feature/crud-mysql

En una etapa posterior se puede crear una rama independiente para PostgreSQL:

feature/crud-postgresql

La versión PostgreSQL reutilizará la mayor parte del CRUD y cambiará principalmente:

El motor de Django.
El driver de Python.
El puerto.
El usuario y la contraseña.
La base de datos utilizada.

# Despliegue

La conexión actual con MySQL está preparada para funcionar localmente mediante XAMPP.

No se deben utilizar los valores localhost ni las credenciales locales en un entorno de producción.

Para desplegar el proyecto se necesitaría:

Una base de datos MySQL o PostgreSQL alojada.
Variables de entorno configuradas en la plataforma de despliegue.
Un servidor compatible con Django.
Configuración de ALLOWED_HOSTS.
Configuración de archivos estáticos.
Configuración de seguridad para producción.

# Autora

Desarrollado por Noemí Morales.
Proyecto académico y de portafolio.
