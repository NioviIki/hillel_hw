# Generated by Django 4.1.6 on 2023-02-22 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaveLogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method_of_request', models.CharField(max_length=4)),
                ('path_of_request', models.CharField(max_length=100)),
                ('query_data', models.JSONField()),
                ('body_data', models.JSONField()),
                ('date_and_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
