# EspoCRM API Test Automation

## Team: Qates

Este repositorio contiene pruebas automatizadas para la API de EspoCRM, específicamente para el manejo de reuniones (`Calendar`) (`Calls`) (`Mails`) (`Presentations`) (`Task`). Utiliza `pytest` como marco de pruebas y `requests` para realizar las solicitudes HTTP.

## Estructura del Proyecto

## Tabla de Contenidos

- [Estructura del Proyecto](#estructura-del-proyecto)
- [Instalación](#instalación)
- [Ejecución de Pruebas](#ejecución-de-pruebas)
- [Reporte de Bugs](#reporte-de-bugs)
- [Referencias](#referencias)

## Estructura del Proyecto
El proyecto tiene la siguiente estructura:

```bash 
├── src
│ ├── assertions
│ ├── espocrm_api
│ ├── resources
│   ├── auth
│   ├── credentials
│   ├── schemas
│ ├── utils
├── tests
│ ├── calendar
│ ├── calls
│ ├── correo_borrador
│ ├── coreo_importante
│ ├── login
│ ├── presentations
│ ├── task
├── .gitignore
├── config.py
├── conftest.py
└── README.md
```

## Instalación

### Requisitos Previos
- Java 
  - paso 1 https://acortar.link/eLJasd
  - paso 2 https://acortar.link/x6UHnz
- Allure https://allurereport.org/docs/install/
- Python 3.7+
- `pip`

### Instalación de Dependencias
1. Clona el repositorio y navega al directorio del proyecto:

    ```bash
    git clone https://github.com/AutenticosDecadentes/EspoCRM_Automation.git
    cd EspoCRM_Automation
    ```

2. Crea un entorno virtual e instala las dependencias:

    Crear y Activar un Entorno Virtual:
    ```bash
   python -m venv venv
   source venv/bin/activate 
   pip install -r requirements.txt
    ```
## Ejecución de Pruebas

Para ejecutar los tests, sigue estos pasos:

1. Cambia a la rama `develop`:
    ```bash
    git checkout develop
2. Para ejectuar los test e inicializar allure:
    ```bash
    pytest --alluredir=allure-results
    ```
3. Para visualizar el informe de reportes:
    ```bash
    allure serve allure-results
    ```
## Referencias

- Enlace del sitio web que se automatiza: https://espo.spartan-soft.com/