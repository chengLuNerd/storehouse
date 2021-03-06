## 20191009



[TOC]

### SQLAlchemy概述

**SQLAlchemy** is the Python SQL toolkit and Object Relational Mapper(ORM) that gives application developers the full power and flexibility of SQL.

python用来操作数据库的工具库

**SQLAlchemy Core** 和 **SQLAlchemy ORM**

两种方式都可以

关键取决于，你是否把数据看做业务对象？如果不是，请使用Core；如果是，请使用ORM

使用Core还是ORM？

### 安装

1. 安装sqlalchemy

```
pip install sqlalchemy
```

2. 安装数据库驱动

```
pip install pymysql
```

### 使用

1. 创建引擎
2. 连接数据库
3. 表定义
4. 表的持久化

```python
from sqlalchemy import create_engine
from sqlalchemy import (MetaData, Table, Column, Integer, String, Numeric)

engine = create_engine('sqlite:///cookies.db') #创建引擎
connection = engine.connect() #连接数据库
metadata = MetaData()
#表定义
cookies = Table('cookies', metadata, Column('cookie_id', Integer(), primary_key=True),
               Column('cookie_name', String(50), index=True),
               Column('cookie_recipe_url', String(255)),
               Column('cookie_sku', String(255)),
               Column('quantity', Integer()),
               Column('unit_cost', Numeric(12, 2))) 

metadata.create_all(engine)
```



更多创建表的示例

另外创建一个users表，orders表，line_items表

```python
users = Table('users', metadata, Column('user-id', Integer(), primary_key=True),
              Column('customer_number', Integer(), autoincrement=True),
              Column('username', String(15), nullable=False, unique=True),
              Column('email-address', String(255), nullable=False),
              Column('phone', String(20), nullable=False),
              Column('password', String(25), nullable=False),
              Column('created_on', DateTime(), default=datetime.now),
              Column('updated_on', DateTime(), default=datetime.now, 	                                     onupdate=datetime.now)
             )

orders = Table('orders', metadata, Column('order-id', Integer(), primary_key=True),
              Column('user_id', Foreignkey('users.user-id')),
              Column('shipped', Boolean(), default=False))

line_items = Table('line_items', metadata,
                   Column('line_items_id', Integer(), primary_key=True),
                   Column('order_id', ForeignKey('orders.order-id')),
                   Column('cookie_id', ForeignKey('cookies.cookie_id')),
                   Column('quantity', Integer()),
                   Column('extended_cost', Numeric(12, 2))
                  )
```