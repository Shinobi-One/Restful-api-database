# Generated by Django 4.1.2 on 2023-02-01 08:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_alter_collection_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
