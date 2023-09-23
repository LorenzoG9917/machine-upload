# Machine-Upload
## Descripción
Este proyecto está diseñado para cargar información desde una instancia de [Cloud SQL](http://cloud.google.com/sql) (usando **MySQL**) en [BigQuery](https://cloud.google.com/bigquery).
## Objetivo
Este proyecto tiene como objetivo facilitar la transferencia de datos desde una instancia de Cloud SQL (MySQL) a BigQuery, lo que permite a los usuarios aprovechar las capacidades de análisis y visualización de datos de BigQuery. La herramienta proporciona una interfaz interactiva para conectar fácilmente a la base de datos de Cloud SQL, explorar las tablas disponibles y seleccionar datos específicos para cargar en BigQuery. El proceso es ágil y amigable para los usuarios, lo que lo hace adecuado tanto para profesionales de datos como para aquellos con menos experiencia técnica. El objetivo es simplificar el flujo de trabajo de carga de datos, ahorrar tiempo y garantizar la integridad de los datos en el proceso.
## Arquitectura
![Machine_upload](https://github.com/LorenzoG9917/machine-upload/assets/121797266/ae1d1b4c-c597-4f2d-987d-6b6c7d4c501c)
## Requisitos
Para ejecutar este proyecto, se requiere lo siguiente:
- Una cuenta en Google Cloud Platform para utilizar Cloud SQL y BigQuery.
- Python instalado en su máquina local.
- Un editor de texto (por ejemplo, Visual Studio Code, Sublime Text).
- Una cuenta de servicio de GCP con los siguientes roles:
  - Editor de datos de BigQuery (BigQuery Data Editor).
  - Usuario de BigQuery (BigQuery User).
  - Visualizador de datos de BigQuery (BigQuery Data Viewer).
- Una instancia de Cloud SQL con una base de datos MySQL configurada.
## Primeros Pasos
1. Cree una nueva carpeta para el proyecto y configure un entorno virtual:

    ```shell
    mkdir upload_project
    cd upload_project
    python -m venv env
    ```

2. Active el entorno virtual (para Windows):

    ```shell
    env/Scripts/activate
    ```

3. Instale las bibliotecas requeridas desde el archivo requirements.txt:

    ```shell
    pip install -r requirements.txt
    ```

4. Ejecute la aplicación:

    ```shell
    python main.py
    ```

- La aplicación le pedirá al usuario que proporcione la información correcta para establecer una conexión con la base de datos, incluyendo el usuario de la base de datos, la contraseña, el host (dirección IP) y el nombre de la base de datos.
- Ademas le da la opción de cargar toda las tablas o una tabla en especifica.

## Autor

Este proyecto fue desarrollado por Lorenzo Guerrero.

[![Linkedin](https://i.stack.imgur.com/gVE0j.png) LinkedIn](https://www.linkedin.com/in/lorenzoguerrero17/)



