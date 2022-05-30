# Generated by Django 4.0.2 on 2022-03-27 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='categories/')),
            ],
        ),
    ]
