# Generated by Django 3.2.5 on 2021-07-25 10:37

import articles.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=40, null=True, verbose_name='Text')),
                ('name', models.CharField(blank=True, max_length=5000, null=True, verbose_name='Name')),
                ('category', models.CharField(blank=True, max_length=50, null=True, verbose_name='Category')),
                ('photo', models.ImageField(blank=True, null=True, upload_to=articles.models.get_photo_path, verbose_name='Photo')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tecx', models.CharField(blank=True, max_length=5000, null=True, verbose_name='Name')),
                ('user', models.CharField(max_length=40, verbose_name='User')),
                ('article', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='articles.article')),
            ],
        ),
    ]
