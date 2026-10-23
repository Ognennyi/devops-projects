## Part 1. Готовый докер

1) ![alt text](images/image.png)
Скачал докер-образ с nginx

2) ![alt text](images/image-1.png)
Проверка наличие докер образа через docker-images/image


3) ![alt text](images/image-2.png)
Создал контейнер и видим ID контейнера


4) ![alt text](images/image-3.png)
Проверил, что контейнер запустился

5) Выполнение команды - docker inspect interesting_tu
   ![alt text](images/image-6.png)

![alt text](images/image-4.png)
IP адрес контейнера

![alt text](images/image-8.png)
Видим что запампленных портов нет

Ввожу docker inspect --size interesting_tu чтобы узнать размер контейнера
![alt text](images/image-7.png)


![alt text](images/image-5.png)
Размеры в байтах. SizeRootFs - размер файловой системы контейнера. 
SizeRw - объём данных, которые контейнер записал поверх исходного образа.

6) ![alt text](images/image-10.png)
Остановка контейнера и проверка что он остановился


7) ![alt text](images/image-9.png)
Запустил докер с портами 80 и 443 в контейнере
-p ХОСТ:КОНТЕЙНЕР

8) ![alt text](images/image-13.png)
Вывод страницы в браузере по ссылке - http://localhost:80

9) ![alt text](images/image-12.png)
Рестарт и проверка того, что контейнер запустился


## Part 2. Операции с контейнером

1) ![alt text](images/image-11.png)
Прочитал конфигурационный файл nginx.conf

2) Далее создаю nginx.conf на локальной машине
   
3) ![alt text](images2/image.png) 
   
В данном фале добавляю путь /status для отдачи страницы статуса сервера

4) ![alt text](images2/image-1.png)
Скопировал конфиг из локальной машины в докер. Потом проверил что мой файл перенесся

5) ![alt text](images2/image-2.png)
Перезапустил nginx

6) ![alt text](images2/image-3.png)
Проверка работы /status в браузере

7) ![alt text](images2/image-4.png)
Скопировал container.tar

8) ![alt text](images2/image-5.png)
Остановка контейнера и проверка

9) ![alt text](images2/image-6.png)
Принудительное удаление образа и проверка

10)  ![alt text](images2/image-7.png)
Удаление контейнера и проверка

11)  ![alt text](images2/image-9.png)
![alt text](images2/image-8.png)
Создал образ из файла container.tar

12)  ![alt text](images2/image-10.png)
Создание контейнера и проверка на то что он действительно создался

13)  ![alt text](images2/image-11.png)
Проверка в браузере страницы /status

## Part 3. Мини веб-сервер

1) ![alt text](images3/image.png)
Мини сервер на Си

2) ![alt text](images3/image-1.png)
Запуск сервера на порту 8080

3) ![alt text](images3/image-3.png)
nginx.conf который проксирует все запросы с 81 порта на 127.0.0.1:8080

4) ![alt text](images3/image-2.png)
локальный запуск nginx с написанной конфигурацией

5) ![alt text](images3/image-4.png) 
Проверка через браузер


## Part 4. Свой докер

1) ![alt text](images4/image.png)
1) собирает исходники мини сервера на FastCgi из Части 3;
2) запускает его на 8080 порту;
3) копирует внутрь образа написанный ./nginx/nginx.conf;
4) запускает nginx.

2) ![alt text](images4/image-1.png)
Сборка докер образа, указав имя и тег. + проверка через docker images

3) ![alt text](images4/image-2.png)
запускаю собранный докер образ с маппингом 81 порта на 80 на локальной машине и маппингом папки ./nginx внутрь контейнера по адресу, где лежат конфигурационные файлы nginx'а 

4) ![alt text](images4/image-3.png)
Проверяю в браузере работу контейнера

5) ![alt text](images4/image-4.png)
Дописал /status в конфиг

6) ![alt text](images4/image-5.png)
Перезапуск контейнера

7) ![alt text](images4/image-6.png)
Проверка добавленного /status


## Part 5. Dockle

1) ![alt text](images5/image.png)
Запуск Dockle. 1 ошибка и 1 предупреждение

2) ![alt text](images5/image-1.png)
Ошибок нет

3) ![alt text](images5/image-2.png)
Был исправлен Dockerfile 


## Part6. Базовый Docker Compose


1) ![alt text](images6/image-1.png)
Теперь proxy слушает 8080 и отправляет на порт 81 

2) ![alt text](images6/image.png)
Останавливаю все запущенные контейнеры

3) ![alt text](images6/image-2.png)
Запустил проект с помощью команд docker compose build и docker compose up

4) ![alt text](images6/image-3.png)
Проверка в браузере