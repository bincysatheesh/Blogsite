# Generated by Django 4.2.4 on 2023-08-22 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_blogpost_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='desc',
            field=models.TextField(max_length=200),
        ),
    ]
