# Generated by Django 3.2.4 on 2021-06-21 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0007_auto_20210622_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autem',
            name='time',
            field=models.DateTimeField(max_length=10, verbose_name='Время добавления'),
        ),
        migrations.AlterField(
            model_name='spring',
            name='time',
            field=models.DateTimeField(max_length=10, verbose_name='Время добавления'),
        ),
        migrations.AlterField(
            model_name='summer',
            name='time',
            field=models.DateTimeField(max_length=10, verbose_name='Время добавления'),
        ),
        migrations.AlterField(
            model_name='winter',
            name='time',
            field=models.DateTimeField(max_length=10, verbose_name='Время добавления'),
        ),
    ]
