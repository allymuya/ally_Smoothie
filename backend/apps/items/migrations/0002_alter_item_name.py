# Generated by Django 3.2.7 on 2022-01-18 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(db_index=True, default='Anonymous', max_length=30, verbose_name='Name'),
        ),
    ]
