FROM python:latest
WORKDIR /app
COPY requirements.txt /app
RUN pip install pip --upgrade \
    && pip install -r requirements.txt
COPY . /app
