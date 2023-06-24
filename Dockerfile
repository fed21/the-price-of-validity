# FROM ubuntu

# RUN apt-get update && \
#     apt-get install -y iputils-ping

# ADD run.sh /run.sh
# RUN chmod +x /run.sh

# CMD cd / && ./run.sh
# CMD ["tail", "-f", "/dev/null"]
# CMD bash

FROM python:3.8-slim-buster

WORKDIR /app

RUN pip3 install pika

COPY /docker .

# CMD ["tail", "-f", "/dev/null"]
CMD ["python3", "-u", "consumer.py"]