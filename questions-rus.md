----------------
Python
----------------
Определение Python  
Почему именно Python  
Отличия Python 2 и Python 3  
Отличие statement и функции на примере print в Python 2 и 3  
pep8  
Стандартная библиотека - что чаще всего используете(sys, os, re, datetime)  
Какие библиотеки чаще всего используете  
Что есть в модуле functools  
Что есть в модуле collection 
Как работают namedtuple, defaultdict, ordereddict, frozenset
Модуль copy, чем отличается copy и deepcopy  
Что нового в последних версиях Python  
Почему Python скриптовый  
Почему Python мультипарадигмальный  
Какие есть типы данных  
Какие есть классификации типов данных  
Что такое mutable / immutable, какие есть типы mutable и какие immutable  
Зачем нужны immutable типы  
Как сделать свой immutable класс  
Как устроен float  
Что вернет len(set(2/3, 4/6))  
Какие типы данных ссылочные  
Как ведет себя list внутри у tuple  
linkedlist  
Как устроен dict  
Что может быть ключем в dict  
Коллизии в dict  
хешируемы объект, что такое хеш  
Что такое куча и стек  
[Python Scopes (LGEB)](https://www.geeksforgeeks.org/scope-resolution-in-python-legb-rule/)  
Как работает память в Python  
Как работает и зачем нужен __slots__
Как работает garbage collector, подсчет ссылок на объект refcount  
Что такое декоратор, как сделать свой декоратор  
Как передать декоратору свои параметры  
Встроенный декоратор @wraps  
Что такое и зачем нужны метаклассы, функция type  
Абстрактные классы и методы, модуль ABC  
Что такое GIL и зачем он нужен  
Deadlock problem, Thread Pool, Producer-Consumer model, Greenlets, microthreads, coroutines.  
Concurrency and thread management, synchronization methods (locks, re-entrant locks, semaphores, events, shared memory, message queues)  
Чем отличаются threading, multiprocessing и async  
Что есть в модуле asyncio
Зачем нужен event_loop
Что такое корутина
asyncio.gather vs asyncio.wait
Как наладить обмен данными между процессами  
Как передать Python обьект между процессами pickling/unpickling  
Что такое итератор  
Какие методы использует итератор  
Как сделать итератор, который не будет генератором  
Что такое генератор как он работает  
В чем преимущества и недостатки генераторов  
Как работают comprehensions - list comprehensions, dict-comprehensions, set-comprehensions  
Зачем нужны менеджеры контекста  
[Какие есть способы написать свой менеджер контекста](https://python-scripts.com/contextlib)  
Как обработать ошибку при закрытии менеджера контекста  
Чем отличается is и ==  
[small integer caching](https://realpython.com/lessons/small-integer-caching/)  
Почему None лучше сравнивать с помощью is  
Как сделать свой объект сравниваемым  
Ducktyping в Python  
Зачем нужны args и kwargs  
Что делает модуль future  
Как дебажить приложения, debugging, Ipdb  
Замыкания  
Разница между методом класса и статическим методом  
lambda функции  
полний синтаксис циклов и try-except  
методы списков, кортежей, словарей  
Unicode  
Регулярные выражения  
dispatch()  
Наследование в Python  
Что такое инкапсуляция и зачем она нужна  
Какие примеры полиморфизма в Python  
Принципы ООП  
Как сделать свой singleton  
Что такое MRO и как оно отличается в Python 2 и 3  
Методы класса, методы интанса, статические методы  
Встроенные декораторы @classmethod и @staticmethod  
Зачем нужны magic методы  
Какие есть magic методы  
[Чем отличается __new__ и __init__](https://habr.com/ru/post/480022/)  
Чем отличаются __str__ и __repr__  
Что в Python от функционального программирования, функции первого порядка  
Алгоритмы сортировки и поиска  
[Расчет сложности алгоритмов](https://dou.ua/lenta/articles/what-you-should-know-about-algorithms/)  
[Паттерны](https://refactoring.guru/ru/design-patterns/python/)  


----------------
Databases
----------------
PostgreSQL vs MySQL  
Redis vs Memcached  
В чем различия типов join в SQL  
Зачем используется HAVING  
Зачем используется EXPLAIN  
Как работает GROUP BY  
Нормализация баз данных, какие условия 1 нормальной формы  
Денормализация, когда применяется  
Какие есть типы связей в базе данных  
Как one-to-one реализован на уровне базы данных  
Как устроен many-to-many на уровне базы данных  
Отличия SQL и No-SQL  
Какие есть типы SQL и No-SQL баз и в чем разница  
Зачем нужны индексы и как они работают  
В каких случаях в базе по дефолту строятся индексы  
Какие бывают индексы, разница между кластеризированный/некластеризированый  
Хранимые процедуры torres  
Пользовательские функции  
Зачем нужен primary key  
Можно ли сделать таблицу без primary key  
Что такое изоляция транзакций  
Как работает Elasticsearch, какой тип базы Elasticsearch(документная nosql)  
Как поддерживать индекс эластика в актуальном состоянии  
MongoDB, rакой тип базы MongoDB(документная nosql)  
Какой паттерн работы с базой в Django ORM и SQLAlchemy(Active Record vs Unit of work)  
шардинг, разница между вертикальным и горизонтальным  
триггеры  
сиквенс  
репликация, как работает master-slave  
Entity-Relationship  
Что такое транзакция?  
ACID  
SQL permission management  


----------------
Services
----------------
Что такое Redis и зачем он нужен  
Celery - приоритезация очередей, брокер и бекенд, Flower  
Celery очереди vs Redis каналы  
RabbitMQ, AMPQ  


----------------
Principles
----------------
REST  
Микросервисы  
SOLID  
KISS  
DRY  
YAGNI  
"запахи кода"  
TDD, DDD  
SOAP  
WSDL  


----------------
Network
----------------
Модель OSI  
TCP/IP, DNS  
IPv4, IPv6  
rpc  
smtp  
HTTP - структура, методы, из чего состоит запрос и ответ  
Разница между POST, PUT, PATCH  
Примеры использования OPTIONS, HEAD, TRACE, CONNECT  
Что такое идемпотентность, какие методы HTTP идемпотентны  
Что такое сокеты? TCP vs UDP  
WebRTC, peer-to-peer  
SSL/TLS  
SSH  
Telnet  
NAT  
Proxy  
ARP  


----------------
Frameworks
----------------
Что такое Django  
MVC архитектура  
Чем отличается Django и Flask  
Как в Django хранятся сессии  
[Какой путь проходит request в Django](https://www.youtube.com/watch?v=fxs5dFB3xD4)  
Как работает middleware в Django  
Можно ли middleware использовать для изменения response  
Как работает select_related и в чем его преимущества  
Как работает prefetch_related и в чем его преимущества  
Зачем нужен F и Q в Django ORM  
Что есть в Django REST Framework  
django signals  
django channels  
django messages  
django mixins  
django class-based views vs function-based views  
django services(serviceLayer)  
Что нового в Django?  
GeoDjango  
Jinja2, Django template system  
aiohttp - назначение, принцип, клиент и сервер, uvloop  
Flask  
Scrapy vs requests + beautifulsoap  
Selenium  
Тестирование - виды тестов и зачем, aвтоматизация тестирования, моки  
XML  
JSON  


----------------
Auth
----------------
Какие типы авторизации поддерживает DRF  
Какая проблема в Token Authentication DRF  
Где хранится токен, как передается на фронт, где храниться на фронте  
Как работает middleware и что делает, authmiddleware что именно делает  
Что такое JWT, его преимущества  
Техники рефакторинга кода - Code review theory and toolset  


----------------
DevOps
----------------
Зачем нужен CI/CD, какие проблемы решает  
Gitlab vs Github-based CI/CD tools и что бы вы выбрали для проекта  
jenkins  
terraform  
ansible  
nginx - какие задачи решает, возможности  
[Docker: layers, volume, image, container](https://www.youtube.com/watch?v=fqMOX6JJhGo)  
Что описывается в Dockerfile и что в Compose  
Оптимизация Dockerfile/docker-compose
Стоит ли использовать Docker в локальной разработке - плюсы и минусы  
Docker vs Virtualbox vs Virtualenv  
DMZ + VPC инфраструктура  
AWS: SQS, SNS, RDS, DynamoDB, Elasticsearch, Lambda, Kinesis, EC2, S3, Route53, Redis, Load Balancer, Auto Scaling and Scaling group  
Google Cloud  
Linux  
Kafka  
Apache Airflow  
uwsgi vs Gunicorn vs Apache  
iwsgi vs Daphne  
supervisor  
crontab  
bash, shell scripting  

----------------
git
----------------
Git Workflow  
[Git branching model](https://nvie.com/posts/a-successful-git-branching-model/)  
Trunk-based Development
git rebase vs merge  
Дерево Меркла в git  


----------------
Security
----------------
Основы криптографии  
Шифрование - AES, sha, синхронное, асинхронное  
private and public key  
https - зачем, как шифрует  
OWASP top 10  
Как избежать sql инъекций в Django(csrf token)  
Зачем соль и когда она добавляется в токен, пароль  
identification / authentication / authorization  
password security  
Радужные таблицы  


----------------
Frontend
----------------
Как работает браузер?  
Browser tools  
Cookies  
Local Storage  
JavaScript - variables, data type, operators and constructions, event handling  
HTML5 features  
CSS, CSS3  
Оси XPATH  
DOM  
