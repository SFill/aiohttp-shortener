FROM python:3.7-stretch
COPY requirements.txt /mnt/
WORKDIR /mnt
RUN pip install -Ur requirements.txt
COPY dist/ /mnt/dist
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
RUN chmod +x /usr/local/bin/docker-entrypoint.sh
RUN pip install /mnt/dist/*
ENTRYPOINT ["docker-entrypoint.sh"]