# Generated by Django 2.0.4 on 2018-05-29 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0010_auto_20180525_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='middle_name',
            field=models.CharField(default='', max_length=100, verbose_name='Отчество'),
        ),
    ]