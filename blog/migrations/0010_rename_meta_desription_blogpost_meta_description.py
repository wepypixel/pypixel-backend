# Generated by Django 4.2 on 2023-04-30 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0009_alter_category_options_blogpost_meta_desription"),
    ]

    operations = [
        migrations.RenameField(
            model_name="blogpost",
            old_name="meta_desription",
            new_name="meta_description",
        ),
    ]
