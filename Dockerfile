FROM python:alpine3.15

 COPY ./vault_export.py ./
 COPY ./requirements.txt /tmp/
 RUN pip install --upgrade pip \
    && apk add build-base \
    && pip install -r /tmp/requirements.txt
 ENTRYPOINT [ "python3", "./vault_export.py" ]
