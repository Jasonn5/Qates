# EspoCRM API Test Automation

## Team: Qates

Este repositorio contiene pruebas automatizadas para la API de EspoCRM, específicamente para el manejo de reuniones (`Calendar`) (`Calls`) (`Mails`) (`Meetings`) (`Task`). Utiliza `pytest` como marco de pruebas y `requests` para realizar las solicitudes HTTP.

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
QAstes/
│
├── api/
│   ├── endpoints/
│   │   ├── activities.py
│   │   ├── calls.py
│   │   ├── contact.py
│   │   ├── mail_draft.py
│   │   ├── mail_important.py
│   │   ├── meeting.py
│   │   └── task.py
│   ├── requests/
│   │   └── api_request.py
│   ├── params/
│       ├── activities_params.py
│       ├── call_params.py
│       ├── email_important_params.py
│       ├── meeting_params.json
│       └── task_params.json
│       └── task_params_list.json
│
├── core/
│   ├── assertions/
│   │   ├── calendar.py
│   │   ├── comparison.py
│   │   ├── content.py
│   │   ├── headers.py
│   │   ├── payloads.py
│   │   ├── response_data.py
│   │   ├── schemas.py
│   │   └── status.py
│   ├── config/
│   │   └── config.py
│   ├── payloads/
│   │   ├── activities/
│   │   │   └── payload_activities.json
│   │   ├── calls/
│   │   │   ├── payload_call_schema.json
│   │   │   └── payload_call.py
│   │   ├── contact/
│   │   │   ├── payload_contact.py
│   │   │   └── payload_contact_full_values.py
│   │   ├── mail_draft/
│   │   │   ├── payload_email_draft.json
│   │   │   ├── payload_email_draft_invalid_email_format.json
│   │   │   └── payload_email_draft_success.json
│   │   ├── mail_important/
│   │   │   └── payload_mail_important.json
│   │   ├── meeting/
│   │   │   └── payload_meeting.json
│   │   ├── tasks/
│   │   │   ├── payload_schema_task.json
│   │   │   └── payload_tasks.py
│   ├── utils/
│       └── load_resources.py
│
├── resources/
│   ├── auth/
│   │   └── auth.py
│   ├── credentials/
│   │   └── user.json
│   └── schemas/
│       ├── activity.json
│       ├── contact_error_post.json
│       ├── contact_post.json
│       ├── correoImportant.json
│       ├── email.json
│       ├── get_completeFields_all_calls_schema.json
│       ├── payload_meeting_schema.json
│       ├── post_call_schema_response.json
│       ├── presentation.json
│       └── task.json
│
├── tests/
│   ├── calendar/
│   │   ├── conftest.py
│   │   └── test_get_activities.py
│   ├── calls/
│   │   ├── conftest.py
│   │   ├── test_delete_calls.py
│   │   ├── test_get_calls.py
│   │   └── test_post_call.py
│   ├── contact/
│   │   ├── conftest.py
│   │   └── test_post_contact.py
│   │   └── test_put_contact.py
│   ├── login/
│   │   └── test_login.py
│   ├── mail_draft/
│   │   ├── conftest.py
│   │   ├── test_get_email_draft.py
│   │   └── test_post_email_draft.py
│   ├── mail_important/
│   │   ├── conftest.py
│   │   └── test_delete_mail_important.py
│   │   └── test_mail_important.py
│   │   └── test_post_email_insert_important.py
│   ├── meeting/
│   │   ├── conftest.py
│   │   ├── test_delete_meeting.py
│   │   ├── test_get_meeting.py
│   │   └── test_post_meeting.py
│   └── task/
│       ├── conftest.py
│       ├── test_get_task.py
│       └── test_post_create_task.py
│
├── .gitignore
├── README.md
├── requirements.txt
└── venv/
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