# Generated by Django 2.0.4 on 2018-05-24 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0007_auto_20180523_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='license_number',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Номер удостоверения'),
        ),
        migrations.AddField(
            model_name='employee',
            name='license_valid_thru',
            field=models.DateField(blank=True, null=True, verbose_name='Удостоверение действительно до'),
        ),
    ]