# Generated by Django 2.0.4 on 2018-06-13 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0013_chief'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='chief',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='staff.Chief'),
        ),
    ]
