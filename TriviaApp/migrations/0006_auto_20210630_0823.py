# Generated by Django 3.0.3 on 2021-06-30 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TriviaApp', '0005_test_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, max_length=100, null=True),
        ),
    ]
