# Generated by Django 4.2.4 on 2023-08-31 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_latestpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('un', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fn', models.CharField(max_length=60)),
                ('ln', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=100)),
                ('usn', models.CharField(max_length=60)),
                ('pwd', models.CharField(max_length=25)),
                ('cp', models.CharField(max_length=25)),
            ],
        ),
    ]