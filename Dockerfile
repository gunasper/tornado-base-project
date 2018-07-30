# This dockerfile uses a local created id_rsa to clone/pull a remote repository;
# Easy way to prototype a dockerfile for this project;
FROM ubuntu:latest
MAINTAINER Gustavo Nascimento "gunasperm"
ENV REFRESHED_AT 2018-07-31

#OS dependences
RUN apt update
RUN apt upgrade -y
RUN apt install -y git python3-pip python3-setuptools make libpq-dev 

RUN mkdir /root/.ssh/
COPY id_rsa /root/.ssh/id_rsa
RUN chmod 700 /root/.ssh/id_rsa 
RUN touch /root/.ssh/known_hosts
RUN ssh-keyscan github.com >> /root/.ssh/known_hosts

RUN git clone git@github.com:rep

WORKDIR project
RUN make deps

ARG build
ENV BUILD $build
RUN git pull origin master
RUN make deps

EXPOSE 8000
CMD make run

