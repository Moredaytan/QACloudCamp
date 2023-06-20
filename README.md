# Тестирование API

Тестирование API сервиса jsonplaceholder.typicode.com с помощью Python используя библиотеки pytest, requests

PyCharm 2022.3.1 
pytest 7.3.1
request 2.31.0
pip 23.0.1
Python 3.11.0


Тест производит 3 проверки используя методы 

POST \ GET | DELETE 

Использование 
Импортируйте библиотеки если у вас они не установлены. 

В вашем IDE в командной строке введите команды 

pip3 install pitest 
pip install requests

Запуск тестов 

Перед запуском вы должны перейти в папку с тестом 
Для этого используйте команду CD далее путь в то место куда вы распаковали проект 
Пример "  CD C:\Users\Msi\PycharmProjects\ApiTestProjekt_copy\ApiTestProjekt"

В вашем IDE в командной строке введите команду

python -m pytest -v -s

Docker 

Собрать билд - docker build -t automation-tests 
Запустить - docker run automation-tests  