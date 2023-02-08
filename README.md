
# Todo App, template para proyectos de FastApi

El siguiente proyecto es una lista de tareas hecha en fastapi, el cual incluye:



* Autenticación con JWT
* Documentación de openapi
* Operaciones Crud
* Gestor de migraciones de base de datos
* Modularidad siguiendo una arquitectura Clean


## Stack

**Cliente:** OpenApi

**Servidor:** Python, FastApi

**Servidor de Base de datos**: Mysql 8

**Requisitos:**

- Python 3.10 o superior


## Instalación

Crear un entorno virtual de python y levantar ambiente virtual
```bash
  git clone https://github.com/IlopezChan/TodoFastApi.git
  cd TodoFastApi
  python -m venv venv
  
  en Windows:
  .\venv\Scripts\activate

  en sistemas base Unix:
  source venv/bin/activate
```

Instalar las dependencias del proyecto

```bash
  python -r requirements.txt
```

Renombrar el archivo alembic.example por alembic.ini y editar la linea, con los datos de su base de datos
```bash
  sqlalchemy.url = driver://user:pass@localhost/dbname
```

Renombrar el archivo .env.example a .env, y agregar los datos de sus variables de entorno

Ejecutar Migraciones de Base de Datos
```bash
  alembic upgrade head
```

Ejecutar app
```bash
  python -m app.main 
```

### Variables de entorno
Para correr el proyecto, es necesario agregar las siguientes variables de entorno al archivo .env(o editar el .env.example)

#### Configuracion de la Base de datos

`HOST`

`DATABASE_PORT`

`DATABASE_DRIVER`

`DATABASE`

`DATABASE_USER`

`DATABASE_PASSWORD`

`DATABASE_URL`

#### Configuración de la aplicación

`APP_PORT`

`ENV`

`DEBUG_MODE`

#### Configuracion de JWT

`SECRET_KEY`

`ALGORITHM`

`ACCESS_TOKEN_EXPIRE_MINUTES`


## Referencias y Documentación

- Framework web [FastApi](https://fastapi.tiangolo.com/)

- ORM [SqlAlchemy](https://docs.sqlalchemy.org/en/14/)

- Gestor de migraciones [Alembic](https://alembic.sqlalchemy.org/en/latest/tutorial.html)

- Información sobre [Clean Architecture](https://clean-architecture-python.readthedocs.io/en/latest/introduccion/)


## Rutas de la API

#### Modulo de usuarios

**Obtener usuario**

```http
  GET /users
```

Obtiene los datos del usuario en base a su JWT y revuelve un json con los datos de dicho usuario

| Parametro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `bearer token` | `string` | **Requerido**. JWT del usuario, ruta protegida, requiere login y mandar jwt por header |

**Registrar Usuario**

```http
  POST /users/register
```

Crea un usuario con base a los parametros enviados en el request body

| Parametro | Tipo     | Descripción                       |
| :-------- | :------- | :-------------------------------- |
| `Nombre`      | `string` | **Requerido**. Nombre del usuario, enviar por request body |
| `UserName`      | `string` | **Requerido**. UserName del usuario, enviar por request body |
| `Email`      | `string` | **Requerido**. Email, enviar por request body |
| `Password`      | `string` | **Requerido**. Password del usuario, enviar por request body |

#### Modulo de Autentificación

**Login de usuario**

```http
  POST /auth/login
```

Obtiene 2 parametros y regresa un jwt con información del usuario

| Parametro | Tipo     | Descripción                       |
| :-------- | :------- | :-------------------------------- |
| `UserName`      | `string` | **Requerido**. UserName o Email del usuario, enviar por Form Data |
| `Password`      | `string` | **Requerido**. Password del usuario, enviar por Form Data |


#### Modulo de tareas

**Obtener tareas**

```http
  GET /tasks
```

Obtiene los datos del usuario en base a su JWT y devuelve un json con las tareas de dicho usuario

| Parametro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `bearer token` | `string` | **Requerido**. JWT del usuario, ruta protegida, requiere login y mandar jwt por header |

**Obtener tarea**

```http
  GET /tasks/{task_id}
```

Obtiene los datos del usuario en base a su JWT y devuelve un json con la tarea especifica solicitada de dicho usuario

| Parametro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `bearer token` | `string` | **Requerido**. JWT del usuario, ruta protegida, requiere login y mandar jwt por header |
| `task_id` | `int` | **Requerido**. Id de la tarea a obtener |

**Crear tarea**

```http
  POST /tasks
```

Obtiene los datos del usuario del jwt y crea una tarea relacionada a el

| Parametro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `bearer token` | `string` | **Requerido**. JWT del usuario, ruta protegida, requiere login y mandar jwt por header |
| `Nombre`      | `string` | **Requerido**. Nombre de la tarea, enviar por request body |
| `Descripcion`      | `string` | **Requerido**. Descripcion de la tarea, enviar por request body |

**Actualizar tarea**

```http
  PUT /tasks/{task_id}
```

Obtiene los datos del usuario en base a su JWT, actualiza una tarea con los datos enviados en el request body y devuelve un json con la tarea actualizada

| Parametro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `bearer token` | `string` | **Requerido**. JWT del usuario, ruta protegida, requiere login y mandar jwt por header |
| `task_id` | `int` | **Requerido**. Id de la tarea a actualizar |
| `Nombre`      | `string` | **Requerido**. Nombre de la tarea, enviar por request body |
| `Descripcion`      | `string` | **Requerido**. Descripcion de la tarea, enviar por request body |
| `Estatus`      | `string` | **Requerido**. Descripcion de la tarea, enviar por request body |


**Eliminar tarea**

```http
  DELETE /tasks/{task_id}
```

Obtiene los datos del usuario en base a su JWT y devuelve un json con la tarea eliminada de dicho usuario

| Parametro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `bearer token` | `string` | **Requerido**. JWT del usuario, ruta protegida, requiere login y mandar jwt por header |
| `task_id` | `int` | **Requerido**. Id de la tarea a eliminar |


## Arquitectura

La arquitectura que se implemento, esta basada en la arquitectura clean de Robert Cecil Martin.

En este caso la estructura de proyectos se definio de la siguiente forma:

- Modulo
  - **controllers:** Aqui van nuestros controladores, se encarga de enlazar los interactors con nuestra capa de presentación.
  - **services:** Capa dedicada a la logica de negocios
  - **entities:** Nuestro core, capa que va a tener la definicion de nuestras entidades en forma de clases, en otros lenguajes se conocen como DTO
  - **models:** al igual que las entities, parte de nuestro core, aqui se define el modelo de las tablas de base de datos.
  - **interactors:** Capa intermedia entre el controlador y los servicios, en esta capa se definen los requerimientos, llamando a los diferentes servicios para cumplir dicho requerimientos 
  - **repositories:** Capa que se encarga de consultar nuestra fuente de datos.     
  - **routers**: Capa donde declaramos las rutas, junto con los metodos http y llamamos a los controladores
### Clean Architecture
Clean Architecture o arquitectura limpia, es un compendio de principios y patrones de desarrollo que tienen como objetivo el facilitar el proceso de construcción del software, así como su mantenimiento.

#### Beneficios
- Creación de aplicaciones desacopladas que son más fáciles de probar
- Mayor flexibilidad para añadir o remover funcionalidades del software
- Diseño basado en componentes con responsabilidades bien definidas
- Aplazamiento de decisiones críticas hasta el último momento requerido
#### Usos
- Aplicaciones de negocios proyectadas para estar en operación indefinidamente.
- Sistemas distribuidos que se beneficien de un diseño desacoplado (e.g. usando microservicios).
- Infraestructuras heterogeneas a nivel de bases de datos, servicios web, etc.
- Aplicaciones pensadas para ser extendidas por terceros a través de plugins.

### Diagrama de capas de arquitectura clean
![App Screenshot](https://raw.githubusercontent.com/IlopezChan/TodoFastApi/main/app/doc/clean.png)


La arquitectura clean nos dice que el nucleo de nuestra aplicación debe ser el dominio, asi como que las capas exteriores deben tener todo el conocimiento de las capas interiores, pero las interiores no deben tener conocimiento de las capaz superiores, esto para evitar el acoplamiento de dependencias.

Ejemplo:

En nuestra capa de servicios, tenemos un servicio que consume información de una base de datos mysql

```diff
class MySQLConnection:

    def function connect():
        # maneja la conexion a la base de datos
        return 'Database connection';
    
class UserService:

    dbConnection;

    def __init__():
        #injectamos dependencia de la clase MySQLConnection
        self.dbConnection = dbConnection();

    def change_password(self, User):
        #logica para cambiar el password
        self.dbConnection.connect().update('Tabla').where(id, User.id)...etc
        return 'Entidad Actualizada'
```
En el ejemplo anterior, tenemos 2 clases, una clase se encarga de manejar la conexion a la base de datos, y la otra clase es un servicio que consume información y la manipula, podemos observar que el servicio esta teniendo acceso a una capa mas externa de manera directa.

Aparentemente no hay nada mal, ya que el codigo cumple con su función, pero que pasaría, si por X o Y razón, nos cambian nuestra fuente de datos, dejamos de usar una base de datos mysql y pasamos a una de SQL Server, una noSQL como MongoDB o de plano no usamos una base de datos y comenzamos a consumir de una api externa o algún microservicio.

Tendriamos que reactorizar todo el codigo, tanto el servicio como la clase que se conecta a la la fuente de datos.

#### Solución:

Una de las soluciones seria implementar el patron de repositorios e interfaces, siguiendo las capas de la arquitectura clean.

```diff
# Interfaz del repositorio
class IRepositorio:
    def insert(): pass
    def get(): pass
    def get_by_id():pass 
    def update(): pass
    def delete(): pass

#Implementacion de la interfaz
class UserRepository(IRepository):
    def __init__(self, url):
        self.db = driver.connect(url)

    def update(id, userData):
        user = self.db.update('table').where(user_id == id).data_to_update(userData)
        return user

# Controlador, capa mas externa
class UserController:
    def __init__():
        self.userRepository = UserRepository('URL') 
    
    def change_password(self, id, userData):
        return UserService().change_password(id, userData, self.userRepository) 

# Servicio, capa mas interna
class UserService:
    def change_password(self, id, userData, userRepository):
        #logica para cambiar el password
        user = userRepository.update(id, userData)
        return 'Entidad Actualizada'
```
La cosa cambio, ciertamente es "Más Codigo", pero ninguna capa interna tiene conocimiento de la externa y esto es bueno.

- El controlador tiene conocimiento del repositorio(capa interna a el), y lo utiliza, en su metodo change_password, "injecta" el repositorio en su servicio.

- El repositorio se encuentra aislado, solo implementa a la interfaz IRepositorio y hace operaciones relacionadas a la db en los metodos que implemento.

- El servicio, no tiene conocimiento ni de su controlador ni de su repositorio

En este caso ya no dependemos de nuestra fuente de datos, si se cambia la fuente de datos, solo se crea una nueva clase que implemente IRepository, sin afectar a las capas interiores como el servicio, ya que los metodos no van a cambiar.

Esto es una ventaja al momento de realizar testing por partes, podriamos crear un repositorio con datos dummy y testear toda nuestra aplicación sin mayores efectos.
## Lecciones aprendidas

**¿Que aprendiste realizando este proyecto?** 

En principio aprender a usar FastApi y orientarlo a objetos para mayor modularidad, asi como la implementacion de una arquitectura clean que va de la mano con los principios SOLID.

**¿Que retos encontraste y como los sobrepasastes?**

FastAPI es un framework muy rapido y poderoso, con un sistema de injección de dependencias muy sencillo de usar, sirve para crear rest apis de forma muy rapida, sin embargo tiene unos "Problemas" que pueden hacer arreglados con algo de tiempo:

- Poca documentación, en la pagina oficial hay poca documentación cubriendo los conceptos basicos para que puedas generar una api de forma rapida, pero no profundiza.
- No soporta programación orientada a objetos de forma "nativa", muchos de sus decoradores, por defecto no funcionan en funciones dentro de clases, se tiene que tener un conocimiento un poco avanzado de funciones especiales de python para poder hacer funcionar los metodos del framewor.

- Soporta asincronía, esto es un arma de doble filo, la asincronía nos sirve para poder ejecutar procesos pesados, sin embargo en la documentacion del propio framework nos dice que solo usemos asincronía si sabemos lo que estamos haciendo.

- Pocas Bibliotecas compatibles de entrada, a diferencia de frameworks como Flask o Django que llevan años, fastapi es relativamente reciente, y hay pocas bibliotecas enfocadas a el, la mayoria del tiempo se va a tener que usar una biblioteca diseñada para otro framework y adaptarla a fastapi, no es algo dificil, pero hay que considerar el tiempo que se lleva adaptandola.

Como recomendación general, creo que es necesario crear un catalogo de biblioteca con su implementación en fastapi


## Roadmap

- Creación de un catalogo de bibliotecas propias

- Agregar mas métodos de autenticación(soporte para autenticacion con json, etc)

- Agregar metodos de autorización




## Feedback

Toda retroalimentación es bienvenida, porfavor de contactar por microsoft teams

