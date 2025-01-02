FROM python:3.12-bookworm

RUN apt-get update && apt-get -y install sqlite3
RUN useradd -m dj

USER dj
COPY requirements.txt /home/dj/
ENV PATH="/home/dj/.local/bin:${PATH}"
RUN pip install --user -r /home/dj/requirements.txt
COPY --chown=dj:dj beetsconf.yaml /home/dj/.config/beets/config.yaml
