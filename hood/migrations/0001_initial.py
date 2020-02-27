# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-02-27 07:10
from __future__ import unicode_literals

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
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=100, unique=True)),
                ('business_email', models.EmailField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100, null=True)),
                ('posted_by', models.CharField(max_length=100, null=True)),
                ('count', models.CharField(max_length=100)),
                ('police', models.CharField(max_length=100)),
                ('police_department_address', models.CharField(max_length=100)),
                ('health', models.CharField(max_length=100)),
                ('health_department_address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=70)),
                ('post_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('categories', models.CharField(max_length=70)),
                ('time_created', models.DateTimeField(auto_now=True, null=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hood.Neighborhood')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(default='images/christine.jpg', upload_to='images/')),
                ('bio', models.TextField()),
                ('neighborhood', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='population', to='hood.Neighborhood')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hood.Profile'),
        ),
        migrations.AddField(
            model_name='business',
            name='business_neighborhood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hood.Neighborhood'),
        ),
        migrations.AddField(
            model_name='business',
            name='business_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
