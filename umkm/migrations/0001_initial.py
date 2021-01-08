# Generated by Django 3.1.5 on 2021-01-04 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='umkm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('photo_main', models.ImageField(upload_to='photos/%Y%m/%d/')),
                ('photo_1', models.ImageField(upload_to='photos/%Y%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y%m/%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y%m/%d/')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%Y%m/%d/')),
            ],
        ),
    ]
