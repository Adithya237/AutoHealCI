FROM jenkins/jenkins:lts

USER root

RUN apt-get update && \
    apt-get install -y maven python3 python3-pip git

USER jenkins