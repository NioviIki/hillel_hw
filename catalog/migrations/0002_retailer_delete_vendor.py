# Generated by Django 4.1.6 on 2023-02-11 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Retailer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=30)),
                ('city', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='catalog.city')),
            ],
        ),
        migrations.DeleteModel(
            name='Vendor',
        ),
    ]
