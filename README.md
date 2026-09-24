Sí, Noemí. Copia todo este contenido y reemplaza tu `README.md` completo:

````md
# Portafolio Francisco Muñoz

Portafolio profesional para Francisco Muñoz Urbina, chef ejecutivo, maestro chocolatero y pastelero.

El sitio presenta su trayectoria, especialidades, creaciones y filosofía profesional en torno al chocolate.

## Descripción del proyecto

Aplicación web desarrollada con Python y Django.

El proyecto comenzó utilizando información desde un archivo JSON. Posteriormente se incorporaron modelos Django, conexión con bases de datos y una interfaz de gestión para administrar las creaciones del portafolio.

La rama actual corresponde a:

```text
feature/crud-postgresql
```
````

## Tecnologías utilizadas

- Python
- Django 6.1
- HTML5
- CSS3
- JavaScript
- PostgreSQL
- MySQL/MariaDB
- XAMPP
- Django Admin
- Git y GitHub
- Claude Design
- Codex

## Funcionalidades principales

- Página pública de presentación profesional.
- Sección de filosofía.
- Sección de especialidades.
- Galería de creaciones.
- Métricas y logros profesionales.
- Trayectoria laboral.
- Formación académica.
- Sección de contacto.
- Diseño responsive.
- Modelos Django.
- Conexión con bases de datos.
- Gestión de creaciones mediante Django Admin.
- CRUD personalizado para creaciones.
- Autenticación de usuarios.
- Gestión de sesiones.
- Permisos para usuarios.
- Activación y desactivación de creaciones.
- Protección CSRF en formularios.
- Variables sensibles almacenadas en `.env.local`.

## Arquitectura actual

El proyecto utiliza Django como framework para conectar las URLs, las Views, los Models, las bases de datos y los Templates.

El flujo principal es:

```text
Navegador
    ↓
URLs de Django
    ↓
View
    ↓
Modelo Django
    ↓
Base de datos
    ↓
Contexto
    ↓
Template HTML
    ↓
Respuesta al navegador
```

Algunas secciones generales del portafolio continúan utilizando información desde:

```text
portafolio/data/fran.json
```

Las creaciones se administran mediante modelos Django y base de datos.

## Modelos Django

El proyecto contiene modelos para representar:

- Perfil.
- Contacto.
- Categorías.
- Creaciones.
- Especialidades.
- Logros.
- Experiencias laborales.
- Experiencias adicionales.
- Cursos.
- Estudios.
- Conocimientos.
- Idiomas.

La interfaz CRUD personalizada se concentra en el modelo `Creacion`, ya que corresponde a la colección principal que se muestra en el portafolio.

Los demás modelos pueden administrarse mediante Django Admin.

## CRUD de creaciones

La interfaz personalizada se encuentra en:

```text
http://127.0.0.1:8000/gestion/creaciones/
```

Permite:

- Listar creaciones.
- Crear nuevas creaciones.
- Editar creaciones.
- Activar creaciones.
- Desactivar creaciones.

Las creaciones no se eliminan físicamente. Se utiliza el campo booleano:

```python
activo = models.BooleanField(default=True)
```

Cuando una creación se desactiva:

- Permanece guardada en la base de datos.
- Deja de aparecer en el portafolio público.
- Puede volver a activarse posteriormente.

Este sistema funciona como una desactivación lógica o soft delete.

## Django Admin

El panel administrativo se encuentra en:

```text
http://127.0.0.1:8000/admin/
```

Desde este panel se pueden administrar los modelos registrados en:

```text
portafolio/admin.py
```

Para crear un usuario administrador se utiliza:

```powershell
python manage.py createsuperuser
```

## Usuarios, sesiones y permisos

El proyecto utiliza el sistema de autenticación integrado de Django.

### Superusuario

El superusuario tiene acceso completo al panel administrativo y a todos los modelos registrados.

Se utiliza para administrar la configuración general del proyecto.

### Usuario staff

Fran utiliza un usuario staff con permisos limitados mediante el grupo:

```text
Gestores de creaciones
```

Este grupo puede tener permisos para:

- Ver creaciones.
- Crear creaciones.
- Editar creaciones.

No tiene permiso para eliminar registros.

### Sesiones

Cuando un usuario inicia sesión, Django crea una sesión que permite mantener su autenticación mientras navega por el sistema.

Las vistas de gestión requieren que el usuario haya iniciado sesión.

### Contraseñas

Django no guarda las contraseñas directamente.

Las almacena mediante un hash seguro, por lo que la contraseña original no puede recuperarse desde la base de datos.

Si una contraseña se olvida, debe restablecerse.

## Seguridad implementada

- Las credenciales de la base de datos se almacenan en `.env.local`.
- `.env.local` está incluido en `.gitignore`.
- La interfaz de gestión requiere autenticación.
- Los formularios utilizan protección CSRF.
- Las acciones de activar y desactivar utilizan solicitudes `POST`.
- La interfaz de gestión no está enlazada desde el portafolio público.
- Las creaciones desactivadas no se muestran públicamente.
- Las contraseñas de los usuarios se almacenan mediante hash.
- La base de datos SQLite no se utiliza en las ramas MySQL y PostgreSQL.

## Configuración local con PostgreSQL

La rama `feature/crud-postgresql` utiliza PostgreSQL de forma local.

### Requisitos

- PostgreSQL instalado.
- PostgreSQL Server activo.
- pgAdmin 4.
- Python.
- Entorno virtual.
- Driver `psycopg`.

### Crear la base de datos

Base de datos:

```text
portafolio_db_pg
```

Usuario:

```text
fran_user_pg
```

Puerto:

```text
5432
```

### Variables de entorno

Crear un archivo `.env.local` en la raíz del proyecto, junto a `manage.py`.

Ejemplo:

```env
DATABASE_NAME=portafolio_db_pg
DATABASE_USER=fran_user_pg
DATABASE_PASSWORD=TU_CLAVE_LOCAL
DATABASE_HOST=localhost
DATABASE_PORT=5432
DEBUG=True
```

El archivo `.env.local` no debe subirse al repositorio.

### Motor configurado en Django

La rama PostgreSQL utiliza:

```python
"ENGINE": "django.db.backends.postgresql"
```

### Instalar dependencias

```powershell
python -m pip install -r requirements.txt
```

El proyecto utiliza, entre otras, estas dependencias:

```text
Django
python-decouple
mysqlclient
psycopg[binary]
```

### Ejecutar migraciones

```powershell
python manage.py makemigrations
python manage.py migrate
```

### Crear usuario administrador

```powershell
python manage.py createsuperuser
```

### Iniciar el servidor

```powershell
python manage.py runserver
```

El portafolio público estará disponible en:

```text
http://127.0.0.1:8000/
```

El panel administrativo estará disponible en:

```text
http://127.0.0.1:8000/admin/
```

La interfaz personalizada de gestión estará disponible en:

```text
http://127.0.0.1:8000/gestion/creaciones/
```

## Configuración local con MySQL/MariaDB

La rama `feature/crud-mysql` utiliza MySQL/MariaDB mediante XAMPP.

### Configuración general

- Iniciar MySQL desde XAMPP.
- Crear la base de datos `portafolio_db`.
- Crear el usuario correspondiente.
- Utilizar el puerto `3306`.
- Configurar las credenciales en `.env.local`.
- Ejecutar las migraciones con Django.

Ejemplo:

```env
DATABASE_NAME=portafolio_db
DATABASE_USER=fran_user
DATABASE_PASSWORD=TU_CLAVE_LOCAL
DATABASE_HOST=localhost
DATABASE_PORT=3306
DEBUG=True
```

Apache solo es necesario para acceder a phpMyAdmin:

```text
http://localhost/phpmyadmin/
```

Django se conecta directamente al servicio MySQL/MariaDB.

## Ramas del proyecto

```text
main
feature/crud-mysql
feature/crud-postgresql
```

### `main`

Contiene la versión principal del proyecto.

### `feature/crud-mysql`

Contiene la conexión local con MySQL/MariaDB mediante XAMPP.

### `feature/crud-postgresql`

Contiene la conexión local con PostgreSQL.

Ambas ramas reutilizan:

- Los modelos.
- El CRUD.
- El diseño.
- La autenticación.
- Las sesiones.
- Los permisos.
- La lógica de activación y desactivación.

Los principales cambios entre las ramas corresponden a:

- El motor de base de datos.
- El driver de Python.
- El nombre de la base.
- El usuario.
- La contraseña.
- El puerto.

## Uso de inteligencia artificial

La inteligencia artificial se utilizó como herramienta de apoyo durante el diseño y desarrollo del proyecto.

### Claude Design

Claude Design fue utilizado inicialmente para crear la propuesta visual del portafolio.

Se le entregó información sobre:

- La identidad profesional de Francisco.
- Su trayectoria.
- Su trabajo como chocolatero y pastelero.
- El concepto del chocolate.
- La estética visual deseada.
- La estructura de las secciones.
- La paleta de colores.
- El diseño responsive.

Posteriormente, se le solicitó a la misma herramienta diseñar la interfaz CRUD de creaciones.

Claude Design adaptó el CRUD al diseño inicial del portafolio y a la nueva estructura del proyecto Django, manteniendo:

- La identidad visual.
- La paleta de colores.
- La organización de los componentes.
- La estética editorial.
- La coherencia entre el portafolio público y la interfaz de gestión.

## Estructura principal del proyecto

```text
fran-portafolio/
│
├── manage.py
├── requirements.txt
├── .gitignore
├── .env.local
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
    │           ├── _creacion_form.html
    │           └── creaciones_lista.html
    │
    └── static/
        └── portafolio/
            ├── css/
            ├── js/
            └── img/
```

## Pruebas realizadas

Se verificó el funcionamiento mediante:

```powershell
python manage.py check
```

```powershell
python manage.py makemigrations
```

```powershell
python manage.py migrate
```

También se comprobó:

- Conexión con MySQL/MariaDB.
- Conexión con PostgreSQL.
- Acceso a Django Admin.
- Creación de usuarios.
- Inicio de sesión.
- Gestión de permisos.
- Creación de registros.
- Edición de registros.
- Activación de creaciones.
- Desactivación de creaciones.
- Ocultamiento de creaciones desactivadas en el portafolio público.

## Despliegue

La configuración actual con MySQL y PostgreSQL está pensada para desarrollo local.

No se deben utilizar en producción:

```text
localhost
```

ni las credenciales locales de `.env.local`.

Para desplegar el proyecto se necesitaría:

- Una base de datos alojada.
- Variables de entorno configuradas en la plataforma.
- Un servidor compatible con Django.
- Configuración de `ALLOWED_HOSTS`.
- Configuración de archivos estáticos.
- Configuración de seguridad para producción.
- Un servicio de base de datos accesible desde Internet.

## Autora

Desarrollado por **Noemí Morales**.

Proyecto académico y de portafolio.

```

```
