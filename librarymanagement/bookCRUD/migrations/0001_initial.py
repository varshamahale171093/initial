# Generated by Django 4.0.2 on 2022-02-13 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bookInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BookName', models.CharField(max_length=100)),
                ('Publication', models.CharField(max_length=100)),
                ('Qty', models.PositiveIntegerField()),
                ('IssueDate', models.DateField()),
                ('subject', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RollNo', models.PositiveIntegerField()),
                ('studentname', models.CharField(max_length=100)),
                ('standard', models.CharField(max_length=50)),
                ('book_id', models.ManyToManyField(to='bookCRUD.bookInfo')),
            ],
        ),
    ]
