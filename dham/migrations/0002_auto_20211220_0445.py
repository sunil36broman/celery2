# Generated by Django 3.2.10 on 2021-12-20 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dham', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Distributor',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='place',
        ),
        migrations.RemoveField(
            model_name='waiter',
            name='restaurant',
        ),
        migrations.DeleteModel(
            name='Place',
        ),
        migrations.DeleteModel(
            name='Restaurant',
        ),
        migrations.DeleteModel(
            name='Waiter',
        ),
    ]