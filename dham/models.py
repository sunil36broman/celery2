from django.db import models

# class Distributor(models.Model):
       
    
#         username = models.CharField(unique=True, max_length=100)
        
#         email = models.CharField(max_length=100)
#         user_type = models.CharField(max_length=50)
#         description = models.TextField(blank=True, null=True)
        

#         class Meta:
#             # managed = True
#             db_table = 'user_management_user51'
#             default_permissions = () 




# class Place(models.Model):
#     name = models.CharField(max_length=50)
#     address = models.CharField(max_length=80)

#     def __str__(self):
#         return "%s the place" % self.name

# class Restaurant(models.Model):
#     place = models.OneToOneField(
#         Place,
#         on_delete=models.CASCADE,
#         primary_key=True,
#     )
#     serves_hot_dogs = models.BooleanField(default=False)
#     serves_pizza = models.BooleanField(default=False)

#     def __str__(self):
#         return "%s the restaurant" % self.place.name

# class Waiter(models.Model):
#     restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50)

#     def __str__(self):
#         return "%s the waiter at %s" % (self.name, self.restaurant)
	
# class Distributor22(models.Model):
       
    
#         username = models.CharField(unique=True, max_length=100)
        
#         email = models.CharField(max_length=100)
#         user_type = models.CharField(max_length=50)
#         description = models.TextField(blank=True, null=True)
        

#         class Meta:
#             # managed = False
#             db_table = 'user_management_user22'
#             default_permissions = () 

# class Distributor23(models.Model):
       
    
#         username = models.CharField(unique=True, max_length=100)
        
#         email = models.CharField(max_length=100)
#         user_type = models.CharField(max_length=50)
#         description = models.TextField(blank=True, null=True)
#         description2 = models.TextField(blank=True, null=True)
        

#         class Meta:
#             # managed = False
#             db_table = 'user_management_user23'
#             default_permissions = ()             