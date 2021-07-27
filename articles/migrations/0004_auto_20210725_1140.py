# Generated by Django 3.2.5 on 2021-07-25 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20210725_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_author',
            field=models.CharField(max_length=40, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_text',
            field=models.TextField(blank=True, max_length=50000, null=True, verbose_name='Text'),
        ),
    ]
