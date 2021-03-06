# Generated by Django 3.1.3 on 2020-12-05 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='price', serialize=False, to='products.product')),
                ('original', models.DecimalField(decimal_places=2, max_digits=10)),
                ('current', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='features', to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='colors', to='products.product')),
            ],
        ),
    ]
