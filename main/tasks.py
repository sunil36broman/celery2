from __future__ import absolute_import, unicode_literals

from celery import shared_task
from celery.utils.log import get_task_logger
from django.core.mail import EmailMessage

from django.db import connections
import random
from faker import Faker


import datetime
# import the logging library
# import logging
# Get an instance of a logger
logger = get_task_logger(__name__)



@shared_task
def add(x, y):
    fake = Faker()
    # logger.info("send review email")
    # fruits = ['scandra36@email.com','scandra36@email.com','scandra36@email.com']
    # for xx in fruits:
    #     print(xx)
    #     logger.info('Homepage was accessed at '+str(datetime.datetime.now())+' hours!')
    #     email = EmailMessage('Subjectttt', 'Body yyy', to=[xx])
    #     email.send()
    # return x + y



    # with connections['report_db'].cursor() as cursor:
    #     for i in random.sample(range(1, 9000), 3):
    #         value_id=i
    #         value_title=fake.name()
    #         query_va="INSERT INTO categories(category_id, category_name) VALUES(%s,%s)"
    #         cursor.execute(query_va,(value_id,value_title))

    # with connections['dham_db'].cursor() as cursor:
    #     for i in random.sample(range(1, 9000), 3):
    #         product_id=i
    #         product_name=fake.name()
    #         cat_id=i
    #         query_va="INSERT INTO products(product_id, product_name, category_id) VALUES(%s,%s,%s)"
    #         cursor.execute(query_va,(product_id,product_name,cat_id))        
    # return x + y



    with connections['dham_db'].cursor() as cursor:
        for i in random.sample(range(1, 9000), 10):
            value_id=i
            value_title=fake.name()
            query_va="INSERT INTO todos(content) VALUES(%s) RETURNING *"
            cursor.execute(query_va,([value_title])) 
            id = cursor.fetchone()[0]
            print("todos----", id) 

            with connections['report_db'].cursor() as cursor1:
                for i in random.sample(range(1, 9000), 10):
                    value_id=i
                    value_title=fake.name()
                    query_va="INSERT INTO todosdetails(content,todos_id) VALUES(%s,%s) RETURNING *"
                    cursor1.execute(query_va,([value_title],id)) 
                    id1 = cursor1.fetchone()[0]
                    print("todosdetails----", id1) 
    return x + y 


    

@shared_task
def sub(x, y):
    # logger.info("send review email")
    email = EmailMessage('Subject 2', 'Body 2', to=['scandra36@email.com','scandra36@email.com','scandra36@email.com'])
    email.send()
    return x+y    