FROM docker.io/python:3.11-buster
LABEL maintainer="Ata Noor [@atom] <>atom@csh.rit.edu"

WORKDIR /app
ADD ./ /app
COPY ./pip_rqr.txt pip_rqr.txt
RUN apt-get -yq update && \
    pip install --no-cache-dir -r pip_rqr.txt

COPY . .

WORKDIR /app/

ENV PYTHONUNBUFFERED True

CMD ["python3", "slack.py"]
