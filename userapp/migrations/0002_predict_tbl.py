# Generated by Django 4.0.5 on 2022-07-12 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Predict_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField(max_length='10')),
                ('headline', models.TextField(max_length=100)),
                ('result', models.CharField(max_length=100)),
                ('dt', models.DateField(auto_now=True)),
            ],
        ),
    ]
