Shortener: pet project on python 3.7
==============================

What Is This?
-------------

Pet project, созданные в процессе изучения aoihttp, asyncio, etc
Возможно будет применен в боевой среде

Запуск в Docker
---------------
```sh
$ mv .env.example .env
$ ./docker_up.sh
```
Testing
-------
Должен быть запущен postgres на 5432 порте и создан тестовый юзер (см. `.env.test`)
```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -r requirements.dev.txt
pytest
```
