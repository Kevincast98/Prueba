# Prueba tecnica
**Prueba macarenia**
-	Crear una aplicación con Django Rest Framework
-	Configurar un proyecto Django.
-	Crear dos modelos (PERSONAS y TAREAS) que incluya los campos (título, descripción y fecha límite) para el modelo de Tareas. Los campos del modelo de Personas los creará a su parecer y se apreciará la buena estructura de datos. Debe definir las debidas relaciones, una persona puede tener varias tareas

**Crear los siguientes endpoints:**

    	CRUD de personas:
         	a. Filtrar persona por número de documento
    	CRUD de tareas
         	a. Filtrar tareas por fecha limite
         	b. Filtrar tareas por rango de fecha limite
        	 c. Filtrar tareas por persona (tipo y número de documento)
Se recomienda hacer uso de vistas basadas en clases, serializadores y demás estándares recomendados.

**•	Implementar la conexión a una base de datos PostgreSQL:**

	Configurar PostgreSQl como base de datos para la aplicación.
	Realizar migraciones iniciales y comprobar que los endpoints funcionen correctamente.

**•	Configurar el repositorio Git:**

	 Inicializar un repositorio Git y realizar commits de todo el código desarrollado.
	 Crear al menos una rama adicional y hacer al menos un cambio en cada una de ellas.
	 Compartir el enlace al repositorio en GitHub.

**•	Probar endpoints:**

	Probar los servicios utilizando la herramienta de Postman.
	Documentar cada servicio desarrollado en Postman.


# CRUD PERSONAS
Con estos cambios, hemos asociado las rutas URL con las vistas correspondientes. Ahora puedes acceder a los endpoints utilizando las siguientes URLs:

**- Acceder al crud de personas:**

Debes acceder por la seguiente ruta 

	URL: http://localhost:8000/core/personas

[![persona.jpg](https://i.postimg.cc/02jtN8ZF/persona.jpg)](https://postimg.cc/w7K5fYCQ)

**- Obtener todas las personas: /personas/ (método GET):**
Seleccionar el boton de metodo GET que hay dentro de pagina para mostrar los datos almacenados en la base de datos

**- Crear una nueva persona: /personas/ (método POST):**
Completar los datos que se solicitan dentro del crud persona y luego seleccionar el boton de post para crearlo.

[![crear.jpg](https://i.postimg.cc/XJJtww4c/crear.jpg)](https://postimg.cc/946x2w4r)

**- Obtener, actualizar o eliminar una persona específica: /personas/<id>/ (métodos GET, PUT, DELETE):**
Para editar vamos a poner un ejemplo en el cual vamos a acceder a la siguiente ruta:

	URL: "http://localhost:8000/core/personas/1"

[![actualizar.jpg](https://i.postimg.cc/PJ4CDs4R/actualizar.jpg)](https://postimg.cc/GT430f6F)

en este caso nos mostrara la informacion de la persona relacionado con el ID numero 1 y de igual manera podemos ver sus datos y editarlos, para validar esos cambios lo hacemos mediante un PUT.

**- Filtrar persona por número de documento:**
Para filtrar persona por numero de documento vamos a poner un ejemplo en el cual vamos a acceder a la siguiente ruta:

	URL: "http://localhost/core/personas/documento/1111/"

[![filtro-documento.jpg](https://i.postimg.cc/d1VpFGfZ/filtro-documento.jpg)](https://postimg.cc/QBv0kKhj)

de esta manera nos muestra todas las persona que coinciden con ese numero de documento



# CRUD TAREAS

**- Acceder al crud de tareas:**

Debes acceder por la seguiente ruta 

	URL: http://localhost:8000/core/tareas

[![TAREA.jpg](https://i.postimg.cc/6pBDzshh/TAREA.jpg)](https://postimg.cc/fJg2Trp3)

**- Obtener todas las tareas: /tareas/ (método GET):**
Seleccionar el boton de metodo GET que hay dentro de pagina para mostrar los datos almacenados en la base de datos

**- Crear una nueva tarea: /tareas/ (método POST):**
Completar los datos que se solicitan dentro del crud tareas y luego seleccionar el boton de post para crearlo.

**- Obtener, actualizar o eliminar una tarea específica: /tareas/<id>/ (métodos GET, PUT, DELETE):**
Para editar vamos a poner un ejemplo en el cual vamos a acceder a la siguiente ruta:

	URL: "http://localhost:8000/core/tarea/1"

[![editar-tareas.jpg](https://i.postimg.cc/h4d6B846/editar-tareas.jpg)](https://postimg.cc/8sTtd66m)

en este caso nos mostrara la informacion de la persona relacionado con el ID numero 1 y de igual manera podemos ver sus datos y editarlos, para validar esos cambios lo hacemos mediante un PUT.

**- Filtrar tareas por fecha límite:**

**- Obtener tareas por fecha límite: /tareas/fecha_limite/<fecha_limite>/ (método GET):**
Para filtrar por fecha limite vamos a poner un ejemplo en el cual vamos a acceder a la siguiente ruta:

	URL: "http://localhost:8000/core/tareas/fecha_limite/2023-07-10/"

[![tareas-fecha-limite.jpg](https://i.postimg.cc/pX0Dc4bH/tareas-fecha-limite.jpg)](https://postimg.cc/2VZbVHSc)

en este ejemplo mostrar todos las tareas que este asocicados con esta fecha limite

**- Filtrar tareas por rango de fecha límite:**

**- Obtener tareas por rango de fecha límite: /tareas/fecha_limite_range/?fecha_inicio=<fecha_inicio>&fecha_fin=<fecha_fin> (método GET)**

Para obtener las tareas por fecha limite en un rango vamos a poner un ejemplo en el cual vamos a acceder a la siguiente ruta:

	URL:"http://localhost:8000/core/tareas/fecha_limite_range/?fecha_inicio=2023-07-9&fecha_fin=2023-07-10"

[![fecha-limite-range.jpg](https://i.postimg.cc/6pJ9K5NL/fecha-limite-range.jpg)](https://postimg.cc/PPyGzHJP)

en este caso nos mostrara la informacion de las tareas que este en rango de la fecha incial hasta la fecha final.

**- Filtrar tareas por persona (tipo y número de documento):**

**- Obtener tareas por persona: /tareas/persona/<tipo_documento>/<numero_documento>/ (método GET):**

Para obtener las tareas por persona (tipo y número de documento) vamos a poner un ejemplo en el cual vamos a acceder a la siguiente ruta:

	URL: "http://localhost:8000/core/tareas/persona/cc/1234/"
[![tarea-filtro-persona.jpg](https://i.postimg.cc/bwwjpGBn/tarea-filtro-persona.jpg)](https://postimg.cc/VdphFN1s)


en este caso nos mostrara la informacion de las tareas que este asociado a ese tipo de documento y a al numero de documento.

# BASE DE DATOS

[![pngwing-com-11.png](https://i.postimg.cc/fbypbKPN/pngwing-com-11.png)](https://postimg.cc/2qp2c4mc)

**BASE DE DATOS DE PERSONA**
[![DB-PERSONA.jpg](https://i.postimg.cc/cLJdCNYz/DB-PERSONA.jpg)](https://postimg.cc/0bhTXFVG)

**BASE DE DATOS DE TAREAS**

[![DB-TAREAS.jpg](https://i.postimg.cc/76BS04hW/DB-TAREAS.jpg)](https://postimg.cc/gXZwbfvV)


# POSTMAN

[![POST-LOG.png](https://i.postimg.cc/ZRHLy9Mh/POST-LOG.png)](https://postimg.cc/gXwhC0pM)



