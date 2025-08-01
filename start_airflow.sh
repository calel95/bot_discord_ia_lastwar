#!/bin/bash
airflow db upgrade
airflow db migrate

airflow scheduler