# Generated by Django 3.0.7 on 2020-06-09 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caller', '0002_auto_20200608_2333'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactdetail',
            name='name',
            field=models.CharField(default='Unknown', max_length=100),
        ),
    ]
