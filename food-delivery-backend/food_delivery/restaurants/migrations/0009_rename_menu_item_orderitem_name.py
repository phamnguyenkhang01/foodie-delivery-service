# Generated by Django 5.1.4 on 2025-01-06 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0008_rename_name_orderitem_menu_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='menu_item',
            new_name='name',
        ),
    ]
