# Generated by Django 4.1.2 on 2023-02-12 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_remove_cartitem_books_alter_cartitem_quantity_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='books',
            new_name='Books',
        ),
    ]
