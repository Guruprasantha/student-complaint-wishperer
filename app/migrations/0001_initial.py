# Generated by Django 4.2.1 on 2023-06-15 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uname', models.CharField(max_length=20)),
                ('mobno', models.IntegerField(null=True)),
                ('email', models.CharField(max_length=20)),
                ('pwrd', models.CharField(max_length=20)),
            ],
        ),
    ]
