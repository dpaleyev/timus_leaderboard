# Generated by Django 2.2a1 on 2019-10-16 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='theme',
            field=models.CharField(default='ot', max_length=30),
        ),
    ]