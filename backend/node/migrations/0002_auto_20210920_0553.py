# Generated by Django 3.2.7 on 2021-09-20 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('node', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='node',
            name='tree',
        ),
        migrations.DeleteModel(
            name='Tree',
        ),
    ]