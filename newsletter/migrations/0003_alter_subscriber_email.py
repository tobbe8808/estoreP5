# Generated by Django 3.2 on 2022-07-06 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_alter_subscriber_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='email',
            field=models.EmailField(max_length=255),
        ),
    ]