# Generated by Django 4.2.4 on 2023-08-15 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_number', models.CharField(max_length=155)),
                ('vehicle_type', models.CharField(choices=[('two wheelers', 'Two wheelers'), ('three wheelers', 'Three wheelers'), ('four Wheelers', 'Four wheelers')], default=None, max_length=20)),
                ('vehicle_model', models.CharField(max_length=155)),
                ('vehicle_description', models.TextField()),
            ],
        ),
    ]