# Generated by Django 4.1 on 2023-04-05 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer_details',
            name='contact_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
