# Generated by Django 4.2.4 on 2023-08-22 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_blogpost_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='desc',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='descriptions',
            field=models.TextField(default='nothing', max_length=200),
        ),
    ]