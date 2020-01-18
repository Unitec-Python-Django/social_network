# Generated by Django 2.2.9 on 2020-01-18 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkPlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55, null=True)),
                ('address', models.CharField(max_length=100)),
                ('telephone_number', models.CharField(max_length=15)),
                ('ceo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.User')),
            ],
        ),
    ]
