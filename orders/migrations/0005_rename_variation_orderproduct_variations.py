# Generated by Django 5.0.6 on 2024-05-14 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_rename_variations_orderproduct_variation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderproduct',
            old_name='variation',
            new_name='variations',
        ),
    ]
