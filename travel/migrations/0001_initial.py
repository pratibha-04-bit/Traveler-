# Generated by Django 2.0.5 on 2020-09-12 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Travel_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now_add=True)),
                ('from_date', models.DateField()),
                ('no_people', models.IntegerField()),
                ('adult', models.IntegerField()),
                ('children', models.IntegerField()),
            ],
            options={
                'db_table': 'travel',
            },
        ),
    ]
