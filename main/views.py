# from django.shortcuts import render

# Create your views here.

#./todo/views.py

from django.shortcuts import render
from rest_framework.response import Response
from django.http.response import HttpResponse
from rest_framework.views import APIView
# from . models import Distributor
from django.db import connections
# from . serializers import TodoSerializer
# from rest_framework.views import APIView
# from django.contrib.auth.decorators import permission_required
# from rest_framework.permissions import IsAuthenticated
# from django.utils.decorators import method_decorator
from .tasks import add
import json
import uuid
import random
# Create your views here.
from django_celery_beat.models import PeriodicTask, CrontabSchedule
from faker import Faker
fake = Faker()


import datetime
# import the logging library
import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)



class BooksListAPIView1(APIView):
    # permission_classes = [IsAuthenticated]
    # pass
    # @method_decorator(login_required)
    # @method_decorator(permission_required('todo.view_todo', raise_exception=True))
    # @method_decorator(permission_required(('todo.view_todo','todo.change_todo'), raise_exception=True))
    # @method_decorator(permission_required('todo.view_todo', raise_exception=True))
    def dictfetchall(self, cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

    def get(self,request):
        print("previous celery")
        # add.delay(23,9)
        # logger.info('Homepage was accessed at '+str(datetime.datetime.now())+' hours!')
        # print("after celery")
        # return Response({'data':"value"})


        # books = Distributor.objects.all()
        # category = Category.objects.all()
        # tags = Tag.objects.all()
        # bookAuthor = BookAuthor.objects.all()
        # customerr = Customer.objects.all()
        
        # print("model data==============",books)
        # print("category--",category)
        # print("tags--",tags)
        # print("bookAuthor--",bookAuthor)
        # print("customerr--",customerr)
        

        

        # with connections['books_db'].cursor() as cursor:
        #     cursor.execute("SELECT * FROM department")
        #     data=self.dictfetchall(cursor)
        #     print(data)

        with connections['dham_db'].cursor() as cursor:
            cursor.execute("SELECT * FROM products")
            data=self.dictfetchall(cursor)
        return Response({'data':data})
        # print("connection.cursor=============",data)    
        # serializer = TodoSerializer(todos, many=True)


class BooksListAPIView11(APIView):
    # permission_classes = [IsAuthenticated]
    # pass
    # @method_decorator(login_required)
    # @method_decorator(permission_required('todo.view_todo', raise_exception=True))
    # @method_decorator(permission_required(('todo.view_todo','todo.change_todo'), raise_exception=True))
    # @method_decorator(permission_required('todo.view_todo', raise_exception=True))
    def dictfetchall(self, cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

    def get(self,request):
        print("previous celery")
        add.delay(23,9)
        # logger.info('Homepage was accessed at '+str(datetime.datetime.now())+' hours!')
        # print("after celery")
        # return Response({'data':"value"})


        # books = Distributor.objects.all()
        # category = Category.objects.all()
        # tags = Tag.objects.all()
        # bookAuthor = BookAuthor.objects.all()
        # customerr = Customer.objects.all()
        
        # print("model data==============",books)
        # print("category--",category)
        # print("tags--",tags)
        # print("bookAuthor--",bookAuthor)
        # print("customerr--",customerr)
        

        

        # with connections['books_db'].cursor() as cursor:
        #     cursor.execute("SELECT * FROM department")
        #     data=self.dictfetchall(cursor)
        #     print(data)
        # INSERT INTO product(product_id, product_name, category_id) VALUES (1, 'customer1',10);
        # INSERT INTO categories(category_id, category_name) VALUES (1, 'customer1');
        
        # with connections['report_db'].cursor() as cursor:
        #     for i in random.sample(range(1, 9000), 3):
        #         value_id=i
        #         value_title=fake.name()
        #         query_va="INSERT INTO categories(category_id, category_name) VALUES(%s,%s)"
        #         cursor.execute(query_va,(value_id,value_title))
                # cursor.execute(query_va,(value_id,value_title))
                # print("llllllast----", cursor.lastrowid)
                # cursor.execute(query_va)
                # data=self.dictfetchall(cursor)



        # with connections['dham_db'].cursor() as cursor:
        #     for i in random.sample(range(1, 9000), 100):
        #         value_id=i
        #         value_title=fake.name()
        #         query_va="INSERT INTO todos(content) VALUES(%s) RETURNING *"
        #         cursor.execute(query_va,([value_title])) 
        #         id = cursor.fetchone()[0]
        #         print("todos----", id) 

        #         with connections['report_db'].cursor() as cursor1:
        #             for i in random.sample(range(1, 9000), 100):
        #                 value_id=i
        #                 value_title=fake.name()
        #                 query_va="INSERT INTO todosdetails(content,todos_id) VALUES(%s,%s) RETURNING *"
        #                 cursor1.execute(query_va,([value_title],id)) 
        #                 id1 = cursor1.fetchone()[0]
        #                 print("todosdetails----", id1) 




            # cursor.execute("DELETE FROM categories")
        # return Response({'data':"done"})




       
            # cursor.execute("DELETE FROM categories")
        return Response({'data':"done"})
        # print("connection.cursor=============",data)    
        # serializer = TodoSerializer(todos, many=True)  






        # with connections['dham_db'].cursor() as cursor:
        #     for i in random.sample(range(1, 9000), 3):
        #         value_id=i
        #         value_title=fake.name()
        #         query_va="INSERT INTO todos(content) VALUES(%s) RETURNING *"
        #         print("query show",value_title)
        #         cursor.execute(query_va,([value_title])) 
        #         id = cursor.fetchone()[0]
        #         print("llllllast----", id) 
        #     # cursor.execute("DELETE FROM categories")
        # # return Response({'data':"done"})




        # with connections['report_db'].cursor() as cursor:
        #     for i in random.sample(range(1, 9000), 3):
        #         value_id=i
        #         value_title=fake.name()
        #         query_va="INSERT INTO todosdetails(content,todos_id) VALUES(%s,%s) RETURNING *"
        #         print("query show",value_title)
        #         cursor.execute(query_va,([value_title],value_id)) 
        #         id = cursor.fetchone()[0]
        #         print("todosdetails----", id) 
        #     # cursor.execute("DELETE FROM categories")
        # return Response({'data':"done"})
        # # print("connection.cursor=============",data)    
        # # serializer = TodoSerializer(todos, many=True)        

def schedule_mail(request):
    schedule, created=CrontabSchedule.objects.get_or_create(minute='*/1')
    # task=PeriodicTask.objects.create(crontab=schedule,name="schedule_mail_task"+"3",task='main.tasks.sub', args=json.dumps([[2,3]]))
    task=PeriodicTask.objects.create(crontab=schedule, name="schedule_mail_task"+"7", task='main.tasks.sub')
    return HttpResponse("Done")

class BooksDetailAPIView1(APIView):
    pass
    # @method_decorator(permission_required('todo.view_todo', raise_exception=True))
    # def get(self,request,pk):
    #     todos = Todo.objects.get(id=pk)
    #     serializer = TodoSerializer(todos, many=False)
    #     return Response(serializer.data)

# class CreateTodoAPIView(APIView):

#     # @permission_required('todo.add_todo', raise_exception=True)
#     @method_decorator(permission_required('todo.add_todo', raise_exception=True))
#     def post(self,request):
#         serializer = TodoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

# class UpdateTodoAPIView(APIView):

#     # @permission_required('todo.change_todo', raise_exception=True)
#     @method_decorator(permission_required('todo.change_todo', raise_exception=True))
#     def post(self,request,pk):
#         todo = Todo.objects.get(id=pk)
#         serializer = TodoSerializer(instance=todo, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)

# class ApprovedTodoAPIView(APIView):

#     # @permission_required('todo.change_todo', raise_exception=True)
#     @method_decorator(permission_required('todo.todo_approved', raise_exception=True))
#     def get(self,request,pk):
#         # todo = Todo.objects.get(id=pk)
#         # serializer = TodoSerializer(instance=todo, data=request.data)
#         # if serializer.is_valid():
#         #     serializer.save()
#         return Response({"serializer.data":"ddsdsd"})

# class DeleteTodoAPIView(APIView):

#     # @permission_required('todo.delete_todo', raise_exception=True)
#     @method_decorator(permission_required('todo.delete_todo', raise_exception=True))
#     def get(self,request,pk):
#         todo = Todo.objects.get(id=pk)
#         todo_instance = Todo.objects.get(id=pk)
#         todo_instance.delete()
#         return Response('Deleted')
