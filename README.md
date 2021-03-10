# InMemoryCacheAPI

![GitHub main code](https://img.shields.io/github/languages/top/PotapkinVsevolod/InMemoryCacheAPI)
![GitHub repo size](https://img.shields.io/github/repo-size/potapkinvsevolod/InMemoryCacheAPI)

InMemoryCacheAPI - это REST приложение, написанное на Flask/Python для временного хранениея кэша в памяти по принципу ключ-значение, с возможностью установки
TTL для каждого ключа (имплементация in memory cache Redis).

## Необходимые условия

Прежде чем начать, убедитесь, что на вашем компьютере установлены:
* Python 3 (проект сделан на Python 3.8.5).
* Git

## Установка InMemoryCacheAPI

Для установки InMemoryCacheAPI, клонируйте репозиторий с github с помощью ссылки:

```
git clone https://github.com/PotapkinVsevolod/InMemoryCacheAPI.git
```
Для работы приложения необходимо установить все необходимые зависимости из файла requirements.txt.

## Использование InMemoryCacheAPI
Приложение можно запустить следующей командой
```
python app.py
```

## Примеры обращения к API.

Для того, чтобы положить значение в кэш:
```
curl -X POST 'http://localhost:5000/SET/key/value'
```
при этом, можно опционально добавить время жизни ключа (ttl), добавив в конце url /EX='секунд' или /PX='миллисекунд'
#
Для того, чтобы получить значение по ключу из кэша:
```
curl -X GET 'http://localhost:5000/GET/key'
```

Для того, чтобы удалить ключ из кэша:
```
curl -X DELETE 'http://localhost:5000/DEL/key'
```

Для того, чтобы получить все ключи из кэша.
```
curl -X GET 'http://localhost:5000/KEYS/*'
```

## Контакты

Если возникли какие-либо вопросы, вы можете со мной связаться, написав на <potapkinvsevolod@gmail.com>.
