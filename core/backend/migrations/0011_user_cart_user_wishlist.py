# Generated by Django 4.0.2 on 2022-03-27 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_pageitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cart',
            field=models.ManyToManyField(blank=True, related_name='cart', to='backend.ProductOption'),
        ),
        migrations.AddField(
            model_name='user',
            name='wishlist',
            field=models.ManyToManyField(blank=True, related_name='wishlist', to='backend.ProductOption'),
        ),
    ]