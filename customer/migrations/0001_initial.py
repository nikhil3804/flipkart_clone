# Generated by Django 3.1.7 on 2021-10-13 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='d1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('address', models.CharField(max_length=122)),
                ('mobile', models.CharField(max_length=122)),
            ],
        ),
    ]