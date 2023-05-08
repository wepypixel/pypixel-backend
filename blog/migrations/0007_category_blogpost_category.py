# Generated by Django 4.2 on 2023-04-30 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_blogpost_tags"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name="blogpost",
            name="category",
            field=models.ForeignKey(
                default=12,
                on_delete=django.db.models.deletion.CASCADE,
                to="blog.category",
            ),
            preserve_default=False,
        ),
    ]
