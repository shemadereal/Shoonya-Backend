# Generated by Django 3.2.12 on 2022-03-03 13:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="project",
            name="dataset_id",
        ),
    ]
