# Generated by Django 5.0.3 on 2024-04-03 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api_menu", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="menu",
        ),
        migrations.DeleteModel(
            name="Menu",
        ),
    ]