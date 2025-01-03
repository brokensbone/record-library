FROM python:3.12-bookworm

RUN apt-get update && apt-get -y install sqlite3
COPY requirements.txt /records/install/
RUN pip install --user -r /records/install/requirements.txt
ENV PATH="/root/.local/bin:${PATH}"
