# Generated by Django 2.2a1 on 2019-10-20 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20191020_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='idea',
            field=models.TextField(max_length=1000),
        ),
    ]