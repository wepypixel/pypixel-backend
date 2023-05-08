# Generated by Django 4.2 on 2023-04-29 13:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_blogpost_view_count"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpost",
            name="cover_image",
            field=models.ImageField(
                default=datetime.datetime(2023, 4, 29, 19, 3, 6, 669488),
                upload_to="coverimage/",
            ),
            preserve_default=False,
        ),
    ]