# Generated by Django 3.1.3 on 2020-12-04 05:20

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('video_url', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('transcript', models.TextField(blank=True, null=True)),
                ('publish_date', models.DateTimeField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('thumbnail_image', models.ImageField(upload_to='tutorial/images')),
                ('permalink', models.CharField(max_length=200)),
                ('free', models.BooleanField(default=True)),
                ('difficulty', models.CharField(max_length=100)),
                ('difficulties', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50), size=3)),
            ],
        ),
    ]