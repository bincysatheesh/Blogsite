# Generated by Django 4.2.4 on 2023-08-23 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_blogpost_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='latestpost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='images1')),
                ('dat', models.DateField()),
                ('mt', models.CharField(max_length=50)),
                ('st', models.CharField(max_length=80)),
            ],
        ),
    ]
