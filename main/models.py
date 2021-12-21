# from django.db import models
# from dham.models import Place
# # Create your models here.
# class Table1(models.Model):
#     # place = models.ForeignKey(Place, on_delete=models.DO_NOTHING, db_constraint=False)
#     descr = models.CharField(max_length=50) 


# class TableA(models.Model):
#     id = models.AutoField(primary_key=True)
#     # some other fields
#     # relations = models.ManyToManyField(Place, through='Throughtable')

# class Throughtable(models.Model):
#     id = models.AutoField(primary_key=True)
#     a_id = models.ForeignKey(TableA, on_delete=models.DO_NOTHING, to_field='id')
#     # b_id = SpanningForeignKey(Place, db_constraint=False, to_field='id')


# class DistributorContentTypePermission(models.Model):
            
#     class Meta:
        
#         managed = False  # No database table creation or deletion  \
#                          # operations will be performed for this model. 
                
#         default_permissions = () # disable "add", "change", "delete"
#                                  # and "view" default permissions

#         permissions = ( 
#             ('distributor_report_list', 'Distributor report list'),  
#             ('distributor_report_download', 'Distributor report download'), 
#             ('distributor_report_download2', 'Distributor report download2'), 
#             ('distributor_report_download3', 'Distributor report download3'), 
#             ('distributor_report_download4', 'Distributor report download4'), 
#             ('distributor_report_download5', 'Distributor report download5'), 
           
#         )  