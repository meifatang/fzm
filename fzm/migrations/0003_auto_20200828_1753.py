# Generated by Django 3.1 on 2020-08-28 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fzm', '0002_remove_type_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stockoperate',
            old_name='quantity',
            new_name='operate_quantity',
        ),
    ]
