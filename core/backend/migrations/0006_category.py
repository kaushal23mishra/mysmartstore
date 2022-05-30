# Generated by Django 4.0.2 on 2022-03-27 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_remove_passwordresettoken_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('position', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='categories/')),
            ],
        ),
    ]