FROM resin/rpi-raspbian:jessie
MAINTAINER madsfeup

RUN \
  apt-get update && \
  apt-get install -y python python-dev python-pip python-virtualenv

RUN mkdir /code
ADD ./src/ /code/
RUN pip install -r ./code/requirements.txt

CMD ["python", "/code/index.py"]
