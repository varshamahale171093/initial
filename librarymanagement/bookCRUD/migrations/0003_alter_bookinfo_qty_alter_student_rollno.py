# Generated by Django 4.0.2 on 2022-02-15 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookCRUD', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinfo',
            name='Qty',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='RollNo',
            field=models.IntegerField(),
        ),
    ]