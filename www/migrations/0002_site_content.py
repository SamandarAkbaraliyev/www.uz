# Generated by Django 4.2.7 on 2024-03-09 10:52

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("www", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="site",
            name="content",
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
    ]