## P1 — Reconoce las características de los lenguajes de marcas

> Habla de cómo los lenguajes de marcas y lo que hemos visto en la asignatura han hecho que tu proyecto sea posible.
>

**Introducción**

Los lenguajes de marcas, también denominados lenguajes de marcado, se utilizan como un lenguaje común, cuya finalidad será ser interpretada por el navegador en cuestión.

**HTML**

Las páginas del blog se dividirán en dos vistas principales, la vista de usuario, y la vista de admin; esta última se utilizará para añadir o quitar entradas.

**CSS**

Utilizaremos un CSS sencillo, sin complicarnos, queremos algo funcional antes que estilístico.


**Conclusión**

Gracias a estos dos lenguajes de marcado, crearemos una página web que, de momento, sin ser funcional, y a falta de base de datos, solamente nos mostrará las funciones que tendrá más adelante.

🎥 Vídeo: https://drive.google.com/file/d/1vJmthYJvgtBfbNLmeUbDc6VRgNXI8HMM/view?usp=sharing

## P2 — Utiliza lenguajes de marcas para la transmisión y presentación de información

> Habla de la parte HTML y CSS de tu proyecto.
>

**Introducción**

La interfaz, como previamente hemos visto, está creada con HTML y CSS, HTML se encontrará en la carpeta templates, pues será la que seguirá flask para buscar los HTML, así como dentro de static se encontrará el CSS.

**HTML**

`base.html` — será la base de nuestra herencia, cualquier otro HTML que tengamos, sera un {% extends %} de ésta y {% block contenido %} para llamar a los párrafos por así decirlo.

Etiquetas semánticas — tanto `<nav>`, `<main>`, `<footer>`, `<article>` se utilizarán para estructurar el contenido en la página.

Bucle Jinja2 — [{% for entrada in entradas %} para mostrar cada post], aquí llamaremos a cada tabla y a cada columna de cada tabla que crearemos en el próximo paso.

Formulario admin — `<form>`, `<input>`, `<textarea>` El admin utilizará estas etiquetas solamente en su página con tal de poder crear entradas, así como borrarlas.

**CSS**

Navbar — Nuestro Navbar utilizará Flexbox con justify-content: space-between para que se amolde al espacio en pantalla.


**Cómo ayuda al usuario final**

Como bien hemos dicho antes, esto nos servirá para poder acceder a nuestra página a modo de lector, o si quisieramos editarla; a modo de administrador.

**Conclusión**

Volvemos a repetir que, sin nuestro lenguaje de marcas, este archivo no sería interpretable por ningún buscador, así como casi inaccesible para cualquier usuario sin conocimientos previos.

🎥 Vídeo: https://drive.google.com/file/d/1lLBog5HAJEu2XNU7de364NzYt2lnRUKq/view?usp=sharing

## P3 — Accede y manipula documentos web con Python

> Habla del controlador Flask y el CRUD del admin.
>
> 📹 VÍDEO: Crea una entrada nueva desde el admin, edítala y elimínala en tiempo real.

**Introducción**

Utilizaremos FLASK como interprete que unifique todos los recursos, gracias a éste uniremos todos los datos en una sola app de Python. 

**Soluciones tecnológicas aplicadas**

`@app.route()` — Nos hará el llamamiento a cada página del HTML

`GET / POST` — GET muestra, POST recibe del formulario


`sqlite3.connect()` — Abrirá la conexión con el blog.db que habremos creado en este paso.

`cur.execute()` — Veremos que en el código saldrán consultas SELECT así como inserción de datos UPDATE, DELETE... (DML)

**Cómo ayuda al usuario final**

El administrador podrá cambiar todo desde la página sin saber de programación, haciendo un sistema sencillo tanto para el usuario como para el administrador.

**Conclusión**

Python, será la mente que controle todo, no sin herramientas como Flask para importar el resto de herramientas y poder abrirlas en local.

🎥 Vídeo: https://drive.google.com/file/d/1dwEb7_lEDb3ferz9oOmYMzY4V0DT1Uy4/view?usp=sharing

## P4 — Gestiona información en formatos de intercambio de datos

> Habla de cómo tu aplicación gestiona datos contenidos en bases de datos.
>

**Introducción**

SQLite, es un programa que favorece al usuario, ya que se podrá crear la base de datos de forma intuitiva con una interfaz no abusiva, despues, gracias a Flask, podremos llamarla desde Python.

**Soluciones tecnológicas aplicadas**

`sqlite3.connect()` — Abre la conexión con la base de datos 'blog.db'

`cur.execute("SELECT * FROM entradas")` — Hará una consulta que nos mostrará todas las entradas

`cur.execute("INSERT INTO ...")` — Insertará una nueva entrada a nivel Admin

`cur.execute("UPDATE ... WHERE id=?")` — Modificará la entrada

`cur.execute("DELETE FROM ... WHERE id=?")` — La eliminará

`cur.fetchall()` / `cur.fetchone()` — Convertirá los resultados a HTML

`con.commit()` — Confirmará los cambios

**Cómo ayuda al usuario final**

Ayudará al usuario a crear las entradas modificarlas y borrarlas sin tener ni idea de SQL

**Conclusión**

Teniendo la base de datos en local gracias a SQLite podremos facilitar aún más las cosas.

🎥 Vídeo: (https://drive.google.com/file/d/1owiL1143ukqHa0FpMhZUDVNpgmTnP-2b/view?usp=sharing)

## P5 — Opera sistemas empresariales de gestión de información

> Habla de qué función empresarial cumple la aplicación. NO hables de código, habla de para qué les sirve a las personas.
>

**Introducción**

Este blog que hemos creado aquí hoy es una facilidad para toda aquella empresa que necesite actualizar su datos, añadir actualizaciones de su software o cualquier otra tarea que, gracias a esta pequeña herramienta, le será mucho más sencillo de complir.

**Función empresarial**

Poder crear de una manera más intuitiva y sin código cualquier post o información relevante en su propia página web.

**Cómo ayuda a cada perfil**

Administrador — crear, editar y eliminar contenido sin tocar código

Lector — acceder al contenido desde cualquier navegador

**Conclusión**

La facilidad para darte a conocer, y conseguir que esto, sea una tarea sencilla.
A continuación te dejo el mismo blog, pero poblado, como si de una página de empresa se tratara.

🎥 Vídeo: (https://drive.google.com/file/d/1IUhVmncNep_EmLjw7MbZ89amHErPTbcG/view?usp=sharing)