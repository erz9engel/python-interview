## Python

Визначення Python
Чому саме Python
Відмінності Python 2 і Python 3
Відмінність statement і функції на прикладі print у Python 2 і 3
PEP8
Стандартна бібліотека — що найчастіше використовуєте (sys, os, re, datetime)
Які бібліотеки найчастіше використовуєте
Що є в модулі functools
Що є в модулі collections
Як працюють namedtuple, defaultdict, OrderedDict, frozenset
Модуль copy, чим відрізняються copy і deepcopy
Що нового в останніх версіях Python
Чому Python скриптова мова
Чому Python мультипарадигмальна мова
Які є типи даних
Які є класифікації типів даних
Що таке mutable / immutable, які типи mutable і які immutable
Навіщо потрібні immutable типи
Як зробити власний immutable клас
Як влаштований float
Що поверне len(set([2/3, 4/6]))
Які типи даних є посилальними
Як поводиться list всередині tuple
Linked list
Як влаштований dict
Що може бути ключем у dict
Колізії в dict
Хешований об’єкт, що таке хеш
Що таке купа і стек
[Python Scopes (LGEB)](https://www.geeksforgeeks.org/scope-resolution-in-python-legb-rule/)  
Як працює пам’ять у Python
Як працює і навіщо потрібен **slots**
Як працює garbage collector, підрахунок посилань на об’єкт (refcount)
Що таке декоратор, як зробити власний декоратор
Як передати декоратору власні параметри
Вбудований декоратор @wraps
Що таке і навіщо потрібні метакласи, функція type
Абстрактні класи і методи, модуль ABC
Що таке GIL і навіщо він потрібен
Проблема deadlock, Thread Pool, модель Producer-Consumer, greenlets, мікропотоки, корутини
Concurrency і керування потоками, методи синхронізації (locks, re-entrant locks, семафори, події, спільна пам’ять, черги повідомлень)
Чим відрізняються threading, multiprocessing і async
Що є в модулі asyncio
Навіщо потрібен event_loop
Що таке корутина
asyncio.gather vs asyncio.wait
Як налагодити обмін даними між процесами
Як передати Python-об’єкт між процесами (pickling/unpickling)
Що таке ітератор
Які методи використовує ітератор
Як зробити ітератор, який не є генератором
Що таке генератор і як він працює
Переваги та недоліки генераторів
Як працюють comprehensions — list comprehensions, dict comprehensions, set comprehensions
Навіщо потрібні менеджери контексту
Які є способи написати власний менеджер контексту
Як обробити помилку під час закриття менеджера контексту
Чим відрізняються is і ==
[small integer caching](https://realpython.com/lessons/small-integer-caching/) 
Чому None краще порівнювати за допомогою is
Як зробити власний об’єкт порівнюваним
Duck typing у Python
Навіщо потрібні args і kwargs
Що робить модуль future
Як дебажити застосунки, debugging, ipdb
Замикання
Різниця між методом класу і статичним методом
Lambda-функції
Повний синтаксис циклів і try-except
Методи списків, кортежів, словників
Unicode
Регулярні вирази
dispatch()
Наслідування в Python
Що таке інкапсуляція і навіщо вона потрібна
Приклади поліморфізму в Python
Принципи ООП
Як зробити власний singleton
Що таке MRO і як воно відрізняється в Python 2 і 3
Методи класу, методи екземпляра, статичні методи
Вбудовані декоратори @classmethod і @staticmethod
Навіщо потрібні магічні методи
Які є магічні методи
Чим відрізняються **new** і **init**
Чим відрізняються **str** і **repr**
Що в Python від функціонального програмування, функції першого класу
Алгоритми сортування і пошуку
Розрахунок складності алгоритмів
Патерни

---

## Databases

PostgreSQL vs MySQL
Redis vs Memcached
У чому різниця типів JOIN у SQL
Навіщо використовується HAVING
Навіщо використовується EXPLAIN
Як працює GROUP BY
Нормалізація баз даних, умови першої нормальної форми
Денормалізація, коли застосовується
Які є типи зв’язків у базі даних
Як one-to-one реалізується на рівні бази даних
Як many-to-many реалізується на рівні бази даних
Відмінності SQL і NoSQL
Які є типи SQL і NoSQL баз і в чому різниця
Навіщо потрібні індекси і як вони працюють
У яких випадках у базі за замовчуванням створюються індекси
Які бувають індекси, різниця між кластеризованим і некластеризованим
Збережені процедури
Користувацькі функції
Навіщо потрібен primary key
Чи можна зробити таблицю без primary key
Що таке ізоляція транзакцій
Як працює Elasticsearch, який тип бази Elasticsearch (документна NoSQL)
Як підтримувати індекс Elasticsearch в актуальному стані
MongoDB, який тип бази MongoDB (документна NoSQL)
Який патерн роботи з базою в Django ORM і SQLAlchemy (Active Record vs Unit of Work)
Шардинг, різниця між вертикальним і горизонтальним
Тригери
Sequence
Реплікація, як працює master-slave
Entity-Relationship
Що таке транзакція
ACID
Керування правами доступу в SQL

---

## Services

Що таке Redis і навіщо він потрібен
Celery — пріоритезація черг, брокер і бекенд, Flower
Черги Celery vs канали Redis
RabbitMQ, AMQP

---

## Principles

REST
Мікросервіси
SOLID
KISS
DRY
YAGNI
«Запахи коду»
TDD, DDD
SOAP
WSDL

---

## Network

Модель OSI
TCP/IP, DNS
IPv4, IPv6
RPC
SMTP
HTTP — структура, методи, з чого складається запит і відповідь
Різниця між POST, PUT, PATCH
Приклади використання OPTIONS, HEAD, TRACE, CONNECT
Що таке ідемпотентність, які методи HTTP є ідемпотентними
Що таке сокети? TCP vs UDP
WebRTC, peer-to-peer
SSL/TLS
SSH
Telnet
NAT
Proxy
ARP

---

## Frameworks

Що таке Django
Архітектура MVC
Чим відрізняються Django і Flask
Як у Django зберігаються сесії
Який шлях проходить request у Django
Як працює middleware у Django
Чи можна middleware використовувати для зміни response
Як працює select_related і в чому його переваги
Як працює prefetch_related і в чому його переваги
Навіщо потрібні F і Q в Django ORM
Що є в Django REST Framework
Django signals
Django channels
Django messages
Django mixins
Class-based views vs function-based views у Django
Django services (service layer)
Що нового в Django
GeoDjango
Jinja2, Django template system
aiohttp — призначення, принцип роботи, клієнт і сервер, uvloop
Flask
Scrapy vs requests + BeautifulSoup
Selenium
Тестування — види тестів і навіщо, автоматизація тестування, моки
XML
JSON

---

## Auth

Які типи авторизації підтримує DRF
Яка проблема в Token Authentication у DRF
Де зберігається токен, як передається на фронтенд, де зберігається на фронтенді
Як працює middleware і що воно робить, що саме робить auth middleware
Що таке JWT, його переваги
Техніки рефакторингу коду — теорія code review і набір інструментів

---

## DevOps

Навіщо потрібен CI/CD, які проблеми він вирішує
GitLab vs GitHub-based CI/CD tools і що обрати для проєкту
Jenkins
Terraform
Ansible
nginx — які завдання вирішує, можливості
Docker: layers, volume, image, container
Що описується в Dockerfile і що в Compose
Оптимізація Dockerfile / docker-compose
Чи варто використовувати Docker у локальній розробці — плюси і мінуси
Docker vs VirtualBox vs Virtualenv
DMZ + VPC інфраструктура
AWS: SQS, SNS, RDS, DynamoDB, Elasticsearch, Lambda, Kinesis, EC2, S3, Route53, Redis, Load Balancer, Auto Scaling і Scaling Group
Google Cloud
Linux
Kafka
Apache Airflow
uWSGI vs Gunicorn vs Apache
uWSGI vs Daphne
Supervisor
crontab
bash, shell scripting

---

## Git

Git workflow
[Git branching model](https://nvie.com/posts/a-successful-git-branching-model/)  
Trunk-based Development
git rebase vs merge
Дерево Меркла в Git

---

## Security

Основи криптографії
Шифрування — AES, SHA, симетричне, асиметричне
Private і public key
HTTPS — навіщо, як шифрує
OWASP Top 10
Як уникнути SQL-ін’єкцій у Django (CSRF token)
Навіщо сіль і коли вона додається до токена, пароля
Identification / authentication / authorization
Безпека паролів
Райдужні таблиці

---

## Frontend

Як працює браузер
Інструменти браузера
Cookies
Local Storage
JavaScript — змінні, типи даних, оператори та конструкції, обробка подій
HTML5 features
CSS, CSS3
Осі XPATH
DOM
