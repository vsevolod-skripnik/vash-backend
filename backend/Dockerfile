FROM python:3.8-alpine

ARG USER_ID
ARG USER_NAME=user
ARG CODE_FOLDER=/code
ARG RESOURCES_FOLDER=/resources

RUN adduser -u ${USER_ID} -D ${USER_NAME} && \
    \
    mkdir -p ${CODE_FOLDER} \
             ${RESOURCES_FOLDER} && \
    \
    chown -R ${USER_NAME}: ${CODE_FOLDER} \
                           ${RESOURCES_FOLDER} && \
    \
    # gcc, libpq, musl-dev and postgresql-dev for psycopg2
    apk add --no-cache gcc \
                       libpq \
                       musl-dev \
                       postgresql-dev

USER ${USER_NAME}
COPY --chown=user requirements.txt /tmp
ENV PATH=/home/${USER_NAME}/.local/bin:${PATH}
RUN pip3 --no-cache-dir install --user -r /tmp/requirements.txt && \
    rm -rf /tmp/requirements.txt

COPY code ${CODE_FOLDER}
WORKDIR ${CODE_FOLDER}
