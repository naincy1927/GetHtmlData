# Generated by Django 4.1.7 on 2023-04-05 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='about',
            field=models.TextField(default='not given', max_length=100),
        ),
    ]
