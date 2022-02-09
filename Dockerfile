FROM python:3.8-alpine

LABEL "com.github.actions.name"="S3 Sync"
LABEL "com.github.actions.description"="Sync a directory to an AWS S3 repository"
LABEL "com.github.actions.icon"="refresh-cw"
LABEL "com.github.actions.color"="green"

LABEL version="0.1.1"
LABEL repository="https://github.com/wykeith/sync-s3-rootless"

# https://github.com/aws/aws-cli/blob/master/CHANGELOG.rst
ENV AWSCLI_VERSION='1.18.14'

RUN pip install --quiet --no-cache-dir awscli==${AWSCLI_VERSION}

ADD entrypoint.sh /entrypoint.sh

# Required default workdir when github runners starts a container on a locked down GSIB vm
# RUN mkdir /github && chmod 777 /github && chmod 777 /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
