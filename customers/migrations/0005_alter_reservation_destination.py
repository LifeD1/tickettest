# Generated by Django 5.0.1 on 2024-02-11 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_alter_reservation_number_of_persons_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='destination',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
