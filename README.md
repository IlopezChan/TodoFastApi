# TodoFastApi

Renombrararchivo .env.example a .env e ingresar datos de variables
Renombrar archivo alembic.example a alembic.ini
Buscar en el archivo de alembic la variable sqlalchemy.url = driver://user:pass@localhost/dbname
y agregar los datos de la bd

En mysql:
CREATE DATABASE todo;

posicionarse en raiz de projecto y correr migraciones
alembic revision --autogenerate -m "First migration" 
alembic upgrade head

correr app
python -m app.main 