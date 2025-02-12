# Generated by Django 5.1.1 on 2025-02-10 20:48

import minio_storage.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0007_interiit_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='body',
            name='logo',
            field=models.ImageField(blank=True, default='logos/default_logo.png', null=True, storage=minio_storage.storage.MinioMediaStorage(), upload_to='logos/'),
        ),
        migrations.AlterField(
            model_name='body',
            name='type',
            field=models.IntegerField(choices=[(0, 'CLUBS'), (1, 'TECH TEAM'), (2, 'COMMUNITY')]),
        ),
        migrations.AlterField(
            model_name='cabinet',
            name='image',
            field=models.ImageField(blank=True, null=True, storage=minio_storage.storage.MinioMediaStorage(), upload_to='cabinet/'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(blank=True, null=True, storage=minio_storage.storage.MinioMediaStorage(), upload_to='gallery/'),
        ),
        migrations.AlterField(
            model_name='interiit',
            name='img',
            field=models.ImageField(blank=True, null=True, storage=minio_storage.storage.MinioMediaStorage(), upload_to='interiit/'),
        ),
        migrations.AlterField(
            model_name='interiit',
            name='logo',
            field=models.ImageField(blank=True, null=True, storage=minio_storage.storage.MinioMediaStorage(), upload_to='interiit/'),
        ),
        migrations.AlterField(
            model_name='member',
            name='image',
            field=models.ImageField(blank=True, null=True, storage=minio_storage.storage.MinioMediaStorage(), upload_to='members/'),
        ),
        migrations.AlterField(
            model_name='portal',
            name='banner',
            field=models.ImageField(blank=True, null=True, storage=minio_storage.storage.MinioMediaStorage(), upload_to='banners/'),
        ),
        migrations.AlterField(
            model_name='techstack',
            name='logo',
            field=models.ImageField(blank=True, null=True, storage=minio_storage.storage.MinioMediaStorage(), upload_to='techstack/'),
        ),
        migrations.AlterField(
            model_name='workreport',
            name='image',
            field=models.ImageField(blank=True, null=True, storage=minio_storage.storage.MinioMediaStorage(), upload_to='workreports/'),
        ),
    ]
