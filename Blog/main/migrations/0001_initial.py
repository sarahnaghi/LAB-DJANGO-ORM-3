# Generated by Django 4.2.4 on 2023-08-26 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=2048)),
                ('category', models.CharField(max_length=256)),
                ('content', models.TextField()),
                ('publish_date', models.DateTimeField()),
            ],
        ),
    ]
