FROM ubuntu
RUN apt-get update && apt-get upgrade -y && apt-get autoremove -y
RUN apt-get install -y apt-utils
RUN apt-get install -y curl wget libpq-dev python3-dev
RUN pip3 install --upgrade pip