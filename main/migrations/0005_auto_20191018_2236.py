# Generated by Django 2.2a1 on 2019-10-18 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20191016_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='theme',
            field=models.ManyToManyField(blank=True, to='main.Theme'),
        ),
    ]
