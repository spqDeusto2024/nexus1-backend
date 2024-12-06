# Nexus 1

## Autores
- Josu Igoa  
- Carlos Gonzalez  
- Iker Perez  
- Manuel Garcés  

## Introducción
**Nexus 1** es un proyecto de la asignatura *Proceso y Calidad del Software*, basado en una temática de administración de recursos y activos de un refugio postapocalíptico.  
El proyecto ha sido desarrollado utilizando las siguientes tecnologías: **Docker**, **Python**, **MySQL**, **FastAPI** y **Vue**.

---

## Módulos y Estructura

### Nexus-backend  
Módulo que aloja el backend, documentación y testing del proyecto (API y procesos).

- **App**: Contiene el proyecto principal.  
  - `Auth`: Proporciona las funcionalidades de creación y verificación de tokens.  
  - `Controllers`: Alberga los controladores con sus respectivos CRUD.  
  - `Endpoints`: Contiene los puntos de acceso a la API.  
  - `Models`: Incluye los modelos de request a los endpoints.  
  - `Mysql`: Contiene los modelos de las bases de datos.  
  - `Utils`: Proporciona utilidades varias del proyecto (hashing, variables de entorno).

- **Test**: Contiene los tests de los controladores del proyecto.  

- **Docs**: Alberga los ficheros de configuración y generación de documentación automática, junto con los resultados generados.  
  - `Build`: Contiene los ficheros de configuración y creación de documentación automática.  
  - `Docs`: Incluye los resultados de la documentación generada.

- **Docker**: Contiene los ficheros de configuración para la creación de imágenes de Docker.

---

### Nexus-frontend  
Módulo que aloja el frontend del proyecto.

- **Docker**: Contiene los ficheros de configuración para la creación de imágenes de Docker.

- **Src**: Contiene el código principal del frontend.  
  - `Api`: Clase de configuración para la conexión con la API del backend.  
  - `Assets`: Archivos estáticos (imágenes, videos).  
  - `Components`: Componentes de Vue reutilizables en diferentes vistas.  
  - `Views`: Vistas del frontend.

---

## Estructura de Proyecto (Visual)
**IMAGEN**  
![IMAGEN DE PROYECTO](nexus_struct.png)

---

## Pasos para la Ejecución

### Backend
1. Construcción de la imagen:  
   ```bash
   sudo ./build.sh
2. Creacion de contenedores:
    ```bash
    docker-compose up
3. Eliminar contenedores:
    ```bash
    docker-compose down
### Frontend
1. Construcción de la imagen y los contenedores:  
   ```bash
    docker-compose up --build
2. Creacion de contenedores:
    ```bash
    docker-compose up
3. Eliminar contenedores:
    ```bash
    docker-compose down


