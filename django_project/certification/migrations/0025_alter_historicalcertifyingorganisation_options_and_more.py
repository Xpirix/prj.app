# Generated by Django 4.2.13 on 2024-05-23 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certification', '0024_auto_20220605_0612'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalcertifyingorganisation',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical certifying organisation', 'verbose_name_plural': 'historical certifying organisations'},
        ),
        migrations.AlterModelOptions(
            name='historicalcertifyingorganisationcertificate',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical certifying organisation certificate', 'verbose_name_plural': 'historical certifying organisation certificates'},
        ),
        migrations.AlterModelOptions(
            name='historicalchecklist',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical checklist', 'verbose_name_plural': 'historical checklists'},
        ),
        migrations.AlterField(
            model_name='historicalcertifyingorganisation',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalcertifyingorganisationcertificate',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalchecklist',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
    ]