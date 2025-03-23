# API del Proyecto de Temperatura

> [!WARNING]
> En desarrollo

[EN](readme.md)

## Descripción General
Esta API es parte del Proyecto de Temperatura y proporciona endpoints para gestionar y recuperar datos relacionados con la temperatura. Está construida utilizando tecnologías modernas de backend para garantizar escalabilidad y rendimiento.

## Iniciar API

### Requisitos
- Docker
- Crear .env en el mismo directorio de .env.example y poner las variables de entorno a tu gusto

### Ejecutar
Ejecuta el siguiente comando desde /software

> [!NOTE]
> Esto ejecutara el backend y el frontend, si solo quieres ejecutar el backend especifica después de la palabra up `backend`
> Ejemplo: `docker compose -f docker-compose.yaml up backend -d`

#### Desarrollo
```bash
docker compose -f docker-compose-dev.yaml up -w
```
#### Producción
```bash
docker compose -f docker-compose.yaml up -d
```

## Características
- Recuperar datos de temperatura
- Agregar nuevos registros de temperatura
- Actualizar registros de temperatura existentes
- Eliminar registros de temperatura

## Licencia
Este proyecto está licenciado bajo la [Licencia MIT](/LICENSE).