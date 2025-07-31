"""
## Astronaut ETL example DAG

This DAG queries the list of astronauts currently in space from the
Open Notify API and prints each astronaut's name and flying craft.

There are two tasks, one to get the data from the API and save the results,
and another to print the results. Both tasks are written in Python using
Airflow's TaskFlow API, which allows you to easily turn Python functions into
Airflow tasks, and automatically infer dependencies and pass data.

The second task uses dynamic task mapping to create a copy of the task for
each Astronaut in the list retrieved from the API. This list will change
depending on how many Astronauts are in space, and the DAG will adjust
accordingly each time it runs.

For more explanation and getting started instructions, see our Write your
first DAG tutorial: https://www.astronomer.io/docs/learn/get-started-with-airflow

![Picture of the ISS](https://www.esa.int/var/esa/storage/images/esa_multimedia/images/2010/02/space_station_over_earth/10293696-3-eng-GB/Space_Station_over_Earth_card_full.jpg)
"""

#from airflow.sdk.definitions.asset import Asset
from airflow.decorators import dag, task
from pendulum import datetime
from src.main import *
from dotenv import load_dotenv
from google import genai
from src.main import remover_todos_arquivos_gemini
from datetime import datetime, timedelta


load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Define the basic parameters of the DAG, like schedule and start_date
@dag(
    start_date=(datetime.now()),  # Set a fixed start date for the DAG
    schedule=timedelta(days=2),  # This DAG will run once a day
    catchup=False,
    default_args={"owner": "Astro"},
    tags=["gemini","cleanup"],
)


def remove_gemini_files_dag():
    # Define tasks
    @task
    def executar_remocao():  
        remover_todos_arquivos_gemini()

    # Use dynamic task mapping to run the print_astronaut_craft task for each
    # Astronaut in space

# Instantiate the DAG
    executar_remocao()
remove_gemini_files_dag()