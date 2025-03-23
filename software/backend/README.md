# Temperature Project API

> [!WARNING]
> Under development

[ES](readme_es.md)

## Overview
This API is part of the Temperature Project and provides endpoints to manage and retrieve temperature-related data. It is built using modern backend technologies to ensure scalability and performance.

## Start API

### Requirements
- Docker
- Create a .env file in the same directory as .env.example and set the environment variables as desired

### Run
Run the following command from /software

> [!NOTE]
> This will run both the backend and the frontend. If you only want to run the backend, specify it after the word `up`.
>
> Example: `docker compose -f docker-compose.yaml up backend -d`

#### Development
```bash
docker compose -f docker-compose-dev.yaml up -w
```
#### Production
```bash
docker compose -f docker-compose.yaml up -d
```

## Features
- Retrieve temperature data
- Add new temperature records
- Update existing temperature records
- Delete temperature records

## License
This project is licensed under the [MIT License](/LICENSE).