# Generated by Django 2.2.9 on 2020-03-06 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description_en',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='description_ru',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title_en',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title_ru',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]