# Generated by Django 4.0.4 on 2022-05-06 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0003_alter_profile_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='amount_of_water',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='weight',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]