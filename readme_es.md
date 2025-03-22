# Proyecto de Temperatura

*[EN](readme.md)*

## Descripción General

Este proyecto consiste en un microcontrolador ESP32 que lee datos de temperatura y los envía a una API. El proyecto también incluye el desarrollo de la API y un frontend para mostrar los datos de temperatura.

## Características

- **Integración con ESP32**: Lee datos de temperatura utilizando un sensor y los envía a la API.
- **API**: Un servicio backend para recibir y almacenar los datos de temperatura del ESP32.
- **Frontend**: Una interfaz de usuario para visualizar los datos de temperatura en tiempo real.

## Uso

### 1. Configuración del ESP32
1. Conecta el sensor de temperatura al ESP32.
2. Flashea el ESP32 con el firmware proporcionado para habilitar la lectura de datos de temperatura y enviarlos a la API.

> [!NOTE]
> El firmware esta bajo desarrollo (todavía no es suficientemente estable para producción)

### 2. Ejecutar la API
> [!NOTE]
> Esto aún no está creado.

### 3. Ejecutar el Frontend
> [!NOTE]
> Esto aún no está creado.

### 4. Visualizar los Datos de Temperatura
- Una vez que el ESP32 esté funcionando y enviando datos a la API, abre el frontend en tu navegador para ver las lecturas de temperatura.

## Estructura del Proyecto

- ### /hardware
    - **/esp32**: Código para el microcontrolador ESP32.
- ### /software
    - **/backend**: Código de la API backend.
    - **/frontend**: Código de la aplicación frontend.

## Requisitos

- Microcontrolador ESP32
- Sensor de temperatura
- Docker

## Licencia

Este proyecto está licenciado bajo la [Licencia MIT](LICENSE).