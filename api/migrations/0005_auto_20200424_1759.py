# Generated by Django 3.0.3 on 2020-04-24 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200423_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jog',
            name='date',
            field=models.DateField(db_index=True),
        ),
    ]
