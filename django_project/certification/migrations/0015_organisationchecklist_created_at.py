# Generated by Django 2.2.18 on 2022-04-12 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certification', '0014_organisationchecklist'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisationchecklist',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]