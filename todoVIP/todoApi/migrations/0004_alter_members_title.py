# Generated by Django 4.0.3 on 2022-03-05 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoApi', '0003_missiongroups_alter_members_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='title',
            field=models.CharField(choices=[('IK', 'IK'), ('Yazılım', 'Yazılım'), ('Üretim', 'Üretim')], max_length=25),
        ),
    ]