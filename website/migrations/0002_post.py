# Generated by Django 2.2 on 2021-02-06 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.EmailField(max_length=254)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('img', models.CharField(max_length=500)),
            ],
        ),
    ]
