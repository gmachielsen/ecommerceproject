# Generated by Django 2.2.7 on 2020-01-08 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='billingAddress1',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
