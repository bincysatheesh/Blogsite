# Generated by Django 4.2.4 on 2023-08-21 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogpost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(blank=True, upload_to='images/')),
                ('dat', models.DateField()),
                ('mt', models.CharField(max_length=50)),
                ('st', models.CharField(max_length=80)),
                ('desc', models.CharField(max_length=250)),
                ('authorname', models.CharField(max_length=50)),
                ('count', models.IntegerField()),
            ],
        ),
    ]
