# Generated by Django 3.2.6 on 2021-08-26 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kedia', '0005_booking_new_transaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('img_src', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=2000)),
            ],
        ),
    ]
