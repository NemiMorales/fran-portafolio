# Portafolio Francisco Muñoz

Portafolio profesional para Francisco Muñoz Urbina, chef ejecutivo, maestro chocolatero y pastelero.

El sitio presenta su trayectoria, especialidades, creaciones y filosofía profesional en torno al chocolate como un ingrediente técnico, complejo, noble y capaz de conectar a las personas.

## Descripción del proyecto

Este proyecto fue desarrollado con Python y Django como una aplicación web orientada al backend.

La estructura, configuración, creación de la aplicación, desarrollo de la lógica, lectura de datos JSON, configuración de URLs y preparación de los modelos fueron realizados por Noemí Morales.

El frontend fue diseñado a partir de la visión y los requerimientos del cliente. La información profesional, la identidad y el concepto del portafolio fueron entregados a Claude Design, herramienta utilizada como apoyo para crear la propuesta visual.

Después de revisar y validar la propuesta de diseño, Codex implementó el frontend dentro del proyecto Django, conectando la interfaz con los datos entregados por la View.

## Tecnologías utilizadas

* Python
* Django 6.1
* HTML5
* CSS3
* JSON
* SQLite, utilizada para preparar y migrar los modelos
* Git y GitHub
* Vercel
* Claude Design
* Codex

## Características principales

* Página de presentación profesional.
* Sección de filosofía del chocolatero.
* Especialidades profesionales.
* Galería de creaciones.
* Métricas y logros profesionales.
* Trayectoria laboral.
* Formación académica.
* Sección de contacto.
* Diseño responsive.
* Datos dinámicos provenientes de un archivo JSON.
* Modelos Django preparados para futuras versiones del proyecto.

## Arquitectura de la aplicación

El flujo principal de la aplicación es:

```text
Navegador
    ↓
URLs de Django
    ↓
View
    ↓
Archivo JSON
    ↓
Contexto
    ↓
Template HTML
    ↓
Frontend mostrado al usuario
```

La View recibe la solicitud del navegador, lee la información almacenada en el archivo JSON y envía esos datos al Template para que sean representados en la interfaz.

## Modelos Django

Como parte de la evolución del proyecto, se definieron modelos para representar:

* Especialidades.
* Creaciones.
* Logros.
* Experiencias laborales.

Estos modelos fueron preparados y migrados para que, en futuras versiones, el contenido pueda dejar de depender exclusivamente del archivo JSON y comenzar a administrarse desde una base de datos.

## Uso de inteligencia artificial

La inteligencia artificial se utilizó como herramienta de apoyo durante el proceso de desarrollo.

El flujo de trabajo fue:

1. Se recopiló la visión profesional del cliente, su trayectoria y sus preferencias.
2. Se entregó esta información a Claude Design para generar una propuesta visual.

**PROMPT UTILIZADO**
Quiero diseñar el frontend de un portafolio profesional para Francisco Muñoz Urbina, chef ejecutivo, maestro chocolatero y pastelero de Santiago de Chile.

El sitio debe sentirse como una experiencia editorial, sensorial y de autor. No quiero una página genérica de pastelería, una tienda de dulces ni un diseño infantil. Quiero mostrar a Francisco como un profesional creativo, técnico y apasionado por el chocolate.

CONCEPTO CENTRAL

El chocolate es un ingrediente complejo, difícil de trabajar y profundamente técnico, pero al mismo tiempo puede provocar calma, felicidad y conexión entre las personas.

La identidad debe comunicar estos contrastes:

- Complejo pero cercano.
- Técnico pero emocional.
- Artesanal pero contemporáneo.
- Endémico y conectado con la tierra, pero moderno.
- De nicho y especializado, pero capaz de unir socialmente.
- Preciso y profesional, pero cálido y humano.

Una frase conceptual importante es:

“El chocolate también puede contar historias.”

También puedes incorporar visualmente la idea:

“Un ingrediente noble, lleno de contrastes.”

INFORMACIÓN PROFESIONAL REAL

Utiliza únicamente esta información y no inventes nuevos datos:

- Nombre: Francisco Muñoz Urbina.
- Profesión: chef ejecutivo y maestro chocolatero/pastelero.
- Ubicación: Santiago, Chile.
- Actualmente trabaja como Chef Ejecutivo en LOVA Chocolates desde mayo de 2025.
- Tiene experiencia en chocolatería premium, desarrollo de productos, formulación, control de calidad, costeo y liderazgo de equipos.
- También ha trabajado en Pastelería Sinfonía, Café Mirandes, Wenger Haus, Giser S.A., Testardos Pizza, Otten S.A., CIG Boragó y 99 Restaurante.
- Ha desarrollado bombones, barras, decoraciones para cafeterías y otros productos de chocolatería.
- Ha participado en marketing, redes sociales y comercio electrónico.
- Contribuyó a un aumento de ventas del 13%.
- Contribuyó a una reducción del 28% en los tiempos de entrega a clientes corporativos.
- Tiene formación en Administración Gastronómica Internacional.
- Tiene un Técnico en Programación y Análisis de Sistemas.
- Estudió Chocolatería y Templado.
- Tiene conocimientos de inglés C1, portugués en curso, SQL, JavaScript, HTML y Excel.

No muestres su teléfono ni correo personal. Deja un botón o espacio de contacto profesional que después pueda conectarse a Django.

DIRECCIÓN VISUAL

Crea una estética elegante, oscura, cálida y editorial.

Paleta sugerida:

- Cacao oscuro: #241914
- Chocolate profundo: #3A241D
- Crema cálida: #F2E8D8
- Terracota: #A85F45
- Dorado apagado: #C99A5A
- Verde hoja oscuro: #465447
- Rosado cacao muy sutil: #C99B91

La interfaz debe tener mucho contraste y buena legibilidad. El fondo principal puede ser crema cálida o chocolate oscuro, alternando secciones claras y oscuras.

Usa una combinación tipográfica:

- Una serif elegante y expresiva para títulos.
- Una sans-serif limpia para textos, etiquetas y datos.
- La tipografía debe sentirse artística, profesional y contemporánea.

REFERENCIAS DE ATMÓSFERA

Inspírate en:

- Chocolate derretido.
- Cacao en polvo.
- Texturas de papel artesanal.
- Mesas de trabajo de chocolatería.
- Detalles de laboratorio gastronómico.
- Macrofotografía de chocolate.
- Ingredientes naturales.
- Hojas secas y enredaderas.
- Hongos y formas orgánicas usados de manera sutil.
- Contrastes entre naturaleza y precisión técnica.
- Diseño editorial de revistas gastronómicas.
- Portafolios de chefs y artistas contemporáneos.
- Una energía alternativa y ligeramente experimental, sin perder elegancia.

Los gustos personales de Francisco incluyen la naturaleza, los hongos, girasoles, monsteras, tulipanes, enredaderas, hojas secas, gatos, perros, ratas, pulpos, skate, arte, teatro, tatuajes, café, mate y chocolate. Utiliza estos elementos solo como referencias visuales sutiles. No llenes la página de ilustraciones ni hagas que parezca una página de fanático de música.

ESTRUCTURA DEL SITIO

Diseña una landing page responsive con estas secciones:

1. NAVBAR

- Logo textual: FRANCISCO MUÑOZ.
- Subtítulo pequeño: CHOCOLATERO / PASTELERO.
- Enlaces: Inicio, Filosofía, Creaciones, Trayectoria, Contacto.
- Navbar elegante, liviana y con buen comportamiento en mobile.

2. HERO

Debe ser la sección más impactante.

Incluir:

- Nombre de Francisco.
- Título profesional.
- La frase “El chocolate también puede contar historias.”
- Un texto breve sobre su forma de entender el chocolate.
- Botón “Conocer su trayectoria”.
- Botón secundario “Explorar creaciones”.
- Una imagen protagonista de chocolate artesanal o una composición visual de autor.
- Algún detalle gráfico que recuerde una textura molecular, una semilla de cacao o una forma orgánica.

La imagen no debe mostrar un rostro inventado de Francisco. Usa una imagen conceptual de chocolate, herramientas, cacao o manos trabajando, o deja un placeholder claramente reemplazable.

3. FILOSOFÍA

Crear una sección narrativa titulada:

“Un ingrediente de contrastes.”

Explicar visualmente que el chocolate puede ser complejo y técnico, pero también cálido, social y capaz de provocar felicidad.

Usar una composición editorial con una frase grande, párrafos cortos y detalles visuales inspirados en cacao, naturaleza y precisión.

4. ESPECIALIDADES

Mostrar tarjetas o bloques visuales para:

- Chocolatería premium.
- Desarrollo de productos.
- Formulación de recetas.
- Pastelería.
- Control de calidad.
- Liderazgo de equipos.

Cada tarjeta debe tener un icono simple, elegante y preferentemente SVG o CSS. No uses emojis.

5. CREACIONES

Crear una galería visual con tarjetas para:

- Bombones de autor.
- Barras artesanales.
- Decoraciones para cafetería.

Cada tarjeta debe contener:

- Imagen.
- Nombre.
- Categoría.
- Descripción breve.
- Interacción hover sutil.

Deja la estructura preparada para que después las tarjetas puedan recibir datos dinámicos desde Django mediante JSON.

6. LOGROS

Crear una sección de métricas visuales:

- 13% aumento de ventas.
- 28% reducción de tiempos de entrega.
- 10+ años de experiencia gastronómica.

La sección debe ser elegante y no parecer un dashboard corporativo.

7. TRAYECTORIA

Crear una línea de tiempo o lista editorial con sus experiencias laborales principales:

- LOVA Chocolates — Chef Ejecutivo — Mayo 2025 a la actualidad.
- Café Mirandes — Chef Ejecutivo y Maestro Pastelero — 2022 a 2023.
- Otten S.A. — Ayudante de producción y Chocolatero — 2019 a 2020.
- CIG Boragó — Pastelero — 2019.

Deja la estructura preparada para que los datos puedan venir desde un archivo JSON.

8. FORMACIÓN

Mostrar:

- Administración Gastronómica Internacional.
- Técnico en Programación y Análisis de Sistemas.
- Chocolatería y Templado.

9. CONTACTO

Crear una sección final cálida y profesional con:

- Una frase de cierre.
- Botón “Conversemos”.
- Espacio para Instagram o contacto profesional.
- No inventes enlaces reales.
- Usa placeholders claramente marcados.

10. FOOTER

Incluir:

- Francisco Muñoz Urbina.
- Chef ejecutivo y maestro chocolatero.
- Santiago, Chile.
- Año actual.
- Enlaces sociales como placeholders.

REQUISITOS TÉCNICOS DEL FRONTEND

- No uses React.
- No uses Next.js.
- No uses backend.
- No uses base de datos.
- Usa HTML semántico, CSS y JavaScript vanilla solo si es estrictamente necesario.
- Evita frameworks complejos.
- No dependas de componentes difíciles de trasladar a Django Templates.
- Usa clases CSS claras y organizadas.
- Usa diseño responsive para desktop, tablet y mobile.
- Prioriza accesibilidad, buen contraste, textos alternativos y navegación por teclado.
- No uses información inventada.
- No incluyas teléfono ni correo personal.
- No uses imágenes de personas generadas que puedan hacerse pasar por Francisco.
- Utiliza imágenes conceptuales de chocolate, cacao, herramientas, texturas e ingredientes.
- Deja claramente identificados los lugares donde después reemplazaremos contenido estático por variables Django.

PREPARACIÓN PARA DJANGO

Organiza el frontend pensando que luego será integrado en un proyecto Django.

Usa bloques fáciles de conectar con variables como:

- {{ datos.perfil.nombre }}
- {{ datos.perfil.titulo }}
- {{ datos.perfil.frase }}
- {{ datos.perfil.descripcion }}

Y ciclos para listas como:

- {% for especialidad in datos.especialidades %}
- {% for creacion in datos.creaciones %}
- {% for trabajo in datos.experiencia %}
- {% for logro in datos.logros %}

No es necesario implementar Django ahora, pero la estructura HTML debe ser compatible con Django Templates.

ENTREGABLE

Genera:

1. Una propuesta visual completa de la landing page.
2. HTML semántico.
3. CSS separado y organizado.
4. Componentes visuales reutilizables.
5. Diseño responsive.
6. Imágenes conceptuales o placeholders reemplazables.
7. Una breve explicación de las decisiones visuales.
8. Una lista de los lugares donde después se conectarán los datos JSON de Django.

El resultado debe parecer el portafolio de un chocolatero de autor: profesional, sensorial, técnico, artístico y humano. 
**PROMPT UTILIZADO**


3. Se revisó la propuesta y se validó su coherencia con la identidad del cliente.

4. Codex implementó el apartado frontend dentro de Django.
**PROMPT UTILIZADO**
Revisa el proyecto Django existente y utiliza el PDF adjunto “Portafolio Francisco Muñoz” como referencia visual y de contenido. Implementa el frontend del portafolio dentro de Django Templates, utilizando HTML semántico y CSS separado. Mantén la estética editorial, cálida, oscura y sofisticada del diseño, inspirada en el chocolate, el cacao, la precisión técnica y el trabajo artesanal. Requisitos: - No utilizar React. - No utilizar Next.js. - No crear una aplicación independiente. - No eliminar la View existente. - No eliminar ni reemplazar el archivo fran.json. - Mantener la aplicación sin conexión a APIs externas para los datos. - Utilizar los datos enviados desde la View mediante el contexto “datos”. - Adaptar el HTML para utilizar variables y ciclos de Django Templates. - Usar las imágenes ubicadas en portafolio/static/portafolio/img/. - Mantener textos alternativos en las imágenes. - Crear un diseño responsive para desktop, tablet y dispositivos móviles. - Utilizar una paleta basada en cacao oscuro, chocolate, crema, terracota y dorado apagado. - Implementar las secciones de presentación, filosofía, especialidades, creaciones, logros, trayectoria, formación, contacto y footer. - No inventar información profesional o personal. - No mostrar teléfono ni correo personal. - Dejar placeholders para enlaces de redes sociales o contacto profesional. Conecta correctamente las siguientes estructuras del JSON: - datos.perfil - datos.filosofia - datos.especialidades - datos.creaciones.items - datos.logros - datos.experiencia.items - datos.formacion - datos.contacto - datos.footer Utiliza ciclos como: {% for especialidad in datos.especialidades %} {% for creacion in datos.creaciones.items %} {% for logro in datos.logros %} {% for trabajo in datos.experiencia.items %} {% for estudio in datos.formacion.estudios %} Antes de modificar archivos, revisa la estructura actual del proyecto. Al finalizar: 1. Indica qué archivos fueron modificados. 2. Explica cómo se conectan el JSON, la View y el Template. 3. Verifica que el servidor Django funcione. 4. Comprueba que las imágenes y los estilos se carguen correctamente. 5. Mantén el código sencillo y comprensible para poder explicarlo en una evaluación académica.
**PROMPT UTILIZADO**

5. Se conectaron las secciones visuales con los datos enviados desde la View.
6. Se revisó y ajustó el código para comprobar su funcionamiento.

La IA fue utilizada como apoyo al diseño y desarrollo, mientras que la estructura del proyecto, la configuración de Django, el backend y la integración general fueron realizados y supervisados por la desarrolladora.

## Estructura del proyecto

```text
fran_portafolio/
│
├── manage.py
├── requirements.txt
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
└── portafolio/
    ├── admin.py
    ├── apps.py
    ├── models.py
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
    │       └── home.html
    │
    └── static/
        └── portafolio/
            ├── css/
            │   └── estilos.css
            └── img/
```

## Instalación y ejecución local

Clonar el repositorio:

```bash
git clone https://github.com/NemiMorales/fran-portafolio.git
cd fran-portafolio
```

Crear el entorno virtual:

```bash
py -m venv venv
```

Activar el entorno virtual en Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Instalar las dependencias:

```bash
python -m pip install -r requirements.txt
```

Ejecutar las migraciones:

```bash
python manage.py migrate
```

Iniciar el servidor local:

```bash
python manage.py runserver
```

Luego abrir en el navegador:

```text
http://127.0.0.1:8000/
```

## Despliegue

El proyecto fue publicado utilizando Vercel.

Para permitir el funcionamiento de Django en producción se configuraron:

* Dependencias mediante `requirements.txt`.
* Dominio autorizado en `ALLOWED_HOSTS`.
* Configuración de Django para el entorno de despliegue.

## Autora

Desarrollado por **Noemí Morales**.

Proyecto académico y de portafolio.
