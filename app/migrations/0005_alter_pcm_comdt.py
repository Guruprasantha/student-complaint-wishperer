# Generated by Django 4.2.1 on 2023-06-15 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_pcm_comdt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pcm',
            name='comdt',
            field=models.DateField(),
        ),
    ]
