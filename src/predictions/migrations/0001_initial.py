# Generated by Django 4.1.1 on 2022-09-21 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_and_d', models.DecimalField(decimal_places=4, max_digits=10000)),
                ('administration', models.DecimalField(decimal_places=4, max_digits=10000)),
                ('marketing_spend', models.DecimalField(decimal_places=4, max_digits=10000)),
            ],
        ),
    ]
