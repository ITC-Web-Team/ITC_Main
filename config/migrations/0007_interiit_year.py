# Generated by Django 5.1.1 on 2024-10-20 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0006_interiit_subtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='interiit',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]