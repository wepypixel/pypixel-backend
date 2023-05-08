# Generated by Django 4.2 on 2023-04-30 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0008_remove_blogpost_tags"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "Category", "verbose_name_plural": "Categories"},
        ),
        migrations.AddField(
            model_name="blogpost",
            name="meta_desription",
            field=models.CharField(default="Meta", max_length=120),
            preserve_default=False,
        ),
    ]