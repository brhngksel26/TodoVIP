# Generated by Django 4.0.3 on 2022-03-05 15:27

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('Manager', 'Manager'), ('Member', 'Member')], default='Member', max_length=100)),
                ('title', models.CharField(max_length=25)),
                ('created_date', models.DateTimeField(default=datetime.datetime.now)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(default=datetime.datetime.now)),
                ('created_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('orderOfImportant', models.SmallIntegerField(unique=True)),
                ('startDate', models.DateField(default=datetime.datetime.now)),
                ('finishDate', models.DateField()),
                ('complated', models.BooleanField(default=False)),
                ('member', models.ManyToManyField(to='todoApi.members')),
                ('todo', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='todoApi.todo')),
            ],
        ),
    ]
