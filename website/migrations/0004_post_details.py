# Generated by Django 2.2 on 2021-02-06 17:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20210206_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='details',
            field=models.CharField(default=django.utils.timezone.now, max_length=300),
            preserve_default=False,
        ),
    ]