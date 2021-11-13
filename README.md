# Tienda la 40 - Orquestador
Repositorio para el orquestador (back-end) del proyecto de tienda de barrio "Tienda La 40" con fines académicos para Ingeniería de Software 1 de la MCIC de la Universidad Distrital Francisco José de Caldas, Bogotá, Colombia.

## Integrantes

- Javier Hospital Melo
- Norbey Danilo Muñoz
- Camilo Enrique Rocha
- Juan Sebastián Sánchez
- Brayan Leonardo Sierra
- Ivan Daniel Villegas

## Especificaciones Técnicas
### Tecnologías Implementadas y Versiones

- Flask 0.12, SQLAlquemy 2.5.1
- Python 3.6
- Sqlite 3
- Docker

### Microservices

Esta aplicación trabaja una arquitectura de microservicios. 

```
.
├── apicrud (crud api operations: GET, POST, PATCH, DELETE, GET BY ID)
    ├── database
        ├── tienda.db (database sqlite3)
        └── tienda.sql (script)
    ├── app.py
    ├── requirements.txt
    ├── controller.py (crud operations)
    ├── models.py (classes-models)
    ├── serialisers.py (helps data transformation)
    └── Dockerfile
```

### Ejecución del Proyecto / Instrucciones

```
# 1. Obtener el repositorio de git
git clone https://github.com/Ataches/TiendaLa40_Orquestador.git

# 2. Moverse a la carpeta del repositorio, si aplica
cd TiendaLa40_Orquestador

# 3. Moverse a la rama **master**
git pull origin master && git checkout master

# 4. Instalar dependencias

# 5. Ejecutar
docker-compose build
docker-compose run
docker-compose up 
docker-compose up -d
```

### Licencia

This file is part of TiendaLa40_Orquestador.

TiendaLa40_Orquestador is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

TiendaLa40_Orquestador is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with sintomas_crud. If not, see https://www.gnu.org/licenses/.
