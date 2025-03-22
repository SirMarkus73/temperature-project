# Temperature project

*[ES](readme_es.md)*

## Overview

This project consists of an ESP32 microcontroller that reads temperature data and sends it to an API. The project also includes the development of the API and a frontend to display the temperature data.

## Features

- **ESP32 Integration**: Reads temperature data using a sensor and sends it to the API.
- **API**: A backend service to receive and store temperature data from the ESP32.
- **Frontend**: A user interface to visualize the temperature data in real-time.

## Usage

### 1. Setting up the ESP32
1. Connect the temperature sensor to the ESP32.
2. Flash the ESP32 with the provided firmware to enable it to read temperature data and send it to the API.


> [!NOTE]
> The firmware is under development (it is not yet stable enough for production)


### 2. Running the API
> [!NOTE]
> This is not created yet

### 3. Running the Frontend
> [!NOTE]
> This is not created yet

### 4. Viewing Temperature Data
- Once the ESP32 is running and sending data to the API, open the frontend in your browser to view the temperature readings.

## Project Structure

- ### /hardware
    - **/esp32**: Code for the ESP32 microcontroller.
- ### /software
    - **/backend**: Backend API code.
    - **/frontend**: Frontend application code.

## Requirements

- ESP32 microcontroller
- Temperature sensor
- Docker

## License

This project is licensed under the [MIT License](LICENSE).