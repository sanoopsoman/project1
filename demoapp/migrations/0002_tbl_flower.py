# Generated by Django 4.1.3 on 2023-07-03 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_flower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('img', models.CharField(max_length=500)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
