# Generated by Django 3.0.6 on 2020-06-30 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment_name', models.CharField(max_length=200)),
                ('equipment_model', models.CharField(max_length=200)),
                ('purchase_date', models.DateTimeField()),
                ('expiration_date', models.DateTimeField()),
                ('quantity', models.IntegerField(default='0')),
            ],
        ),
    ]
