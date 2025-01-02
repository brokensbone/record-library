FROM python:3.12-bookworm

RUN useradd -m dj

USER dj
COPY requirements.txt /home/dj/
ENV PATH="/home/dj/.local/bin:${PATH}"
RUN pip install --user -r /home/dj/requirements.txt