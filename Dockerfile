#FROM astrocrpublic.azurecr.io/runtime:3.0-6

# WORKDIR /app

# COPY  requirements.txt /app/requirements.txt


# RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# COPY src /app/src

# ENV PYTHONPATH=/app/src:${PYTHONPATH}

FROM astrocrpublic.azurecr.io/runtime:3.0-6

RUN pip install poetry

WORKDIR /app

# Copia somente os arquivos de dependências para cache
COPY pyproject.toml /app/
COPY README.md  /app/
COPY start_bot.sh  /app/
COPY start_airflow.sh  /app/
COPY src /app/src
COPY data /app/data

ENV PYTHONPATH=/app/src:${PYTHONPATH}
# Instala dependências com poetry sem criar virtualenv
RUN poetry install --no-root --no-interaction

# Copia o código fonte



