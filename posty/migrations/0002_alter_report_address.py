# Generated by Django 5.1.3 on 2024-11-28 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posty', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='address',
            field=models.CharField(max_length=50),
        ),
    ]