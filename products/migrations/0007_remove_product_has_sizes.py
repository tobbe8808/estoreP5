# Generated by Django 3.2 on 2022-07-05 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_review_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='has_sizes',
        ),
    ]