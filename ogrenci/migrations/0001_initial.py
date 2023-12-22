# Generated by Django 5.0 on 2023-12-18 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ogrenci',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('surname', models.CharField(max_length=150)),
                ('tel', models.CharField(max_length=150)),
                ('mail', models.CharField(max_length=150)),
                ('register_date', models.DateTimeField(auto_now_add=True)),
                ('average', models.IntegerField()),
                ('still_student', models.BooleanField(default=True)),
            ],
        ),
    ]