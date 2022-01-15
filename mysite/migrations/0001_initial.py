# Generated by Django 4.0 on 2022-01-15 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(max_length=300)),
                ('created', models.DateField(default='2022-01-15')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
