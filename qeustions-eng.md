## Python

Definition of Python
Why Python
Differences between Python 2 and Python 3
Difference between a statement and a function using print in Python 2 and 3 as an example
PEP 8
Standard library — what you use most often (sys, os, re, datetime)
Which libraries you use most often
What is in the functools module
What is in the collections module
How namedtuple, defaultdict, OrderedDict, frozenset work
The copy module, difference between copy and deepcopy
What’s new in the latest Python versions
Why Python is considered a scripting language
Why Python is multi-paradigm
What data types exist
Classifications of data types
What mutable / immutable means, which types are mutable and which are immutable
Why immutable types are needed
How to create your own immutable class
How float is implemented
What len(set([2/3, 4/6])) returns
Which data types are reference types
How a list behaves inside a tuple
Linked list
How dict is implemented
What can be a dict key
Collisions in dict
Hashable object, what a hash is
What heap and stack are
[Python Scopes (LGEB)](https://www.geeksforgeeks.org/scope-resolution-in-python-legb-rule/)  
How memory works in Python
How **slots** works and why it is needed
How the garbage collector works, reference counting (refcount)
What a decorator is, how to create your own decorator
How to pass parameters to a decorator
Built-in decorator @wraps
What metaclasses are and why they are needed, the type function
Abstract classes and methods, ABC module
What GIL is and why it is needed
Deadlock problem, Thread Pool, Producer–Consumer model, greenlets, microthreads, coroutines
Concurrency and thread management, synchronization methods (locks, re-entrant locks, semaphores, events, shared memory, message queues)
Differences between threading, multiprocessing, and async
What is in the asyncio module
Why event_loop is needed
What a coroutine is
asyncio.gather vs asyncio.wait
How to organize data exchange between processes
How to pass a Python object between processes (pickling/unpickling)
What an iterator is
What methods an iterator uses
How to create an iterator that is not a generator
What a generator is and how it works
Advantages and disadvantages of generators
How comprehensions work — list, dict, and set comprehensions
Why context managers are needed
Ways to implement your own context manager
How to handle an error when closing a context manager
Difference between is and ==
[small integer caching](https://realpython.com/lessons/small-integer-caching/) 
Why None should be compared using is
How to make your own object comparable
Duck typing in Python
Why args and kwargs are needed
What the future module does
How to debug applications, debugging, ipdb
Closures
Difference between a class method and a static method
Lambda functions
Full syntax of loops and try-except
Methods of lists, tuples, dictionaries
Unicode
Regular expressions
dispatch()
Inheritance in Python
What encapsulation is and why it is needed
Examples of polymorphism in Python
OOP principles
How to implement your own singleton
What MRO is and how it differs in Python 2 and 3
Class methods, instance methods, static methods
Built-in decorators @classmethod and @staticmethod
Why magic methods are needed
What magic methods exist
Difference between **new** and **init**
Difference between **str** and **repr**
Functional programming features in Python, first-class functions
Sorting and searching algorithms
Algorithm complexity analysis
Design patterns

---

## Databases

PostgreSQL vs MySQL
Redis vs Memcached
Differences between JOIN types in SQL
Why HAVING is used
Why EXPLAIN is used
How GROUP BY works
Database normalization, conditions of the first normal form
Denormalization, when it is applied
Types of relationships in databases
How one-to-one is implemented at the database level
How many-to-many is implemented at the database level
Differences between SQL and NoSQL
Types of SQL and NoSQL databases and their differences
Why indexes are needed and how they work
When indexes are created by default
Types of indexes, difference between clustered and non-clustered
Stored procedures
User-defined functions
Why a primary key is needed
Can a table exist without a primary key
Transaction isolation
How Elasticsearch works, what type of database Elasticsearch is (document-oriented NoSQL)
How to keep an Elasticsearch index up to date
MongoDB, what type of database MongoDB is (document-oriented NoSQL)
Database interaction patterns in Django ORM and SQLAlchemy (Active Record vs Unit of Work)
Sharding, difference between vertical and horizontal
Triggers
Sequence
Replication, how master–slave works
Entity–Relationship
What a transaction is
ACID
SQL permission management

---

## Services

What Redis is and why it is needed
Celery — queue prioritization, broker and backend, Flower
Celery queues vs Redis channels
RabbitMQ, AMQP

---

## Principles

REST
Microservices
SOLID
KISS
DRY
YAGNI
Code smells
TDD, DDD
SOAP
WSDL

---

## Network

OSI model
TCP/IP, DNS
IPv4, IPv6
RPC
SMTP
HTTP — structure, methods, request and response composition
Difference between POST, PUT, PATCH
Examples of using OPTIONS, HEAD, TRACE, CONNECT
What idempotency is, which HTTP methods are idempotent
What sockets are, TCP vs UDP
WebRTC, peer-to-peer
SSL/TLS
SSH
Telnet
NAT
Proxy
ARP

---

## Frameworks

What Django is
MVC architecture
Difference between Django and Flask
How sessions are stored in Django
Request lifecycle in Django
How middleware works in Django
Whether middleware can modify the response
How select_related works and its advantages
How prefetch_related works and its advantages
Why F and Q objects are needed in Django ORM
What Django REST Framework provides
Django signals
Django channels
Django messages
Django mixins
Class-based views vs function-based views in Django
Django services (service layer)
What’s new in Django
GeoDjango
Jinja2, Django template system
aiohttp — purpose, principles, client and server, uvloop
Flask
Scrapy vs requests + BeautifulSoup
Selenium
Testing — types of tests and why, test automation, mocks
XML
JSON

---

## Auth

Authentication types supported by DRF
Problem with Token Authentication in DRF
Where the token is stored, how it is sent to the frontend, where it is stored on the frontend
How middleware works and what it does, what auth middleware specifically does
What JWT is and its advantages
Code refactoring techniques — code review theory and toolset

---

## DevOps

Why CI/CD is needed, what problems it solves
GitLab vs GitHub-based CI/CD tools and what to choose for a project
Jenkins
Terraform
Ansible
nginx — tasks it solves, capabilities
Docker: layers, volume, image, container
What is defined in Dockerfile and what in Compose
Optimizing Dockerfile / docker-compose
Whether to use Docker in local development — pros and cons
Docker vs VirtualBox vs Virtualenv
DMZ + VPC infrastructure
AWS: SQS, SNS, RDS, DynamoDB, Elasticsearch, Lambda, Kinesis, EC2, S3, Route53, Redis, Load Balancer, Auto Scaling and Scaling Group
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
Merkle tree in Git

---

## Security

Basics of cryptography
Encryption — AES, SHA, symmetric, asymmetric
Private and public keys
HTTPS — why it is needed, how it encrypts
OWASP Top 10
How to prevent SQL injection in Django (CSRF token)
Why salt is needed and when it is added to a token or password
Identification / authentication / authorization
Password security
Rainbow tables

---

## Frontend

How a browser works
Browser developer tools
Cookies
Local Storage
JavaScript — variables, data types, operators and constructions, event handling
HTML5 features
CSS, CSS3
XPATH axes
DOM
