# Generated by Django 5.0.1 on 2024-02-11 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_alter_reservation_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='number_of_persons',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='seat_number',
            field=models.CharField(max_length=10),
        ),
    ]