# Generated by Django 3.1 on 2021-04-24 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hero_name', models.CharField(max_length=250)),
                ('full_name', models.CharField(max_length=250)),
                ('universe', models.CharField(max_length=10)),
                ('isbn', models.CharField(max_length=13)),
            ],
        ),
    ]
