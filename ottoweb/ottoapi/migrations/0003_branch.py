# Generated by Django 2.2.1 on 2019-08-20 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ottoapi', '0002_driver'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=32)),
                ('postcode', models.CharField(max_length=9)),
                ('capacity', models.PositiveIntegerField(default=1))
            ],
            options={
                'ordering': ['city'],
            },
        ),
    ]
