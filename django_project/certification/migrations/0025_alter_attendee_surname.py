# Generated by Django 3.2.13 on 2024-11-12 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certification', '0024_auto_20220605_0612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendee',
            name='surname',
            field=models.CharField(blank=True, help_text='Surname of the attendee.', max_length=200, null=True),
        ),
    ]