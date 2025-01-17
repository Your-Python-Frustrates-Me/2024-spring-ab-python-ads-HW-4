[app](..%2Fapp)
[app.Dockerfile](..%2Fapp.Dockerfile)
[database.sql](..%2Fdatabase.sql)
[postgres.Dockerfile](..%2Fpostgres.Dockerfile)
[docker-compose.yml](..%2Fdocker-compose.yml)
[trees.db](..%2Ftrees.db)# 2024-spring-ab-python-ads-HW-4

## Интеграции и БД + повторение прошлого семестра :)

* Реализовать с помощью FastAPI приложение с эндпоинтом (POST), позволяющим получить количество деревьев в определенном городе в определенном году с помощью Open Street Map.
  API (см. example 3 здесь: https://wiki.openstreetmap.org/wiki/OSMPythonTools). Название города и страны + год должны передаваться в теле запроса.
* Для обращения к Open Street Map API использовать библиотеку requests, НЕ OSMPythonTools.
* Каждый успешный запрос должен логироваться в базу данных (postgresql).
* Реализовать хранимую процедуру в базе данных на plpython, вычисляющую город, который встретился наибольшее количество раз в истории обращений к эндпоинту.

Подсказка - Dockerfile для postgres с plpython лежит в репе.

**Критерии оценки**
* Реализован эндопинт - +2 балла
* Используется библиотека requests - +1 балл
* Реализован docker-compose с приложением и базой данных - +4 балла
* Реализована хранимая процедура - +2 балла
* Правильная структура репозитория - +1 балл
