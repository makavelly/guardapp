# Generated by Django 2.0.4 on 2018-05-25 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0009_auto_20180524_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='date_of_birth',
            field=models.DateField(blank=True, error_messages={'invalid': 'this field is invalid'}, null=True, verbose_name='Дата рождения'),
        ),
    ]
