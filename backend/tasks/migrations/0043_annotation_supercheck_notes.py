# Generated by Django 3.2.14 on 2023-04-21 05:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0042_task_super_check_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="annotation",
            name="supercheck_notes",
            field=models.TextField(
                blank=True, null=True, verbose_name="supercheck_notes"
            ),
        ),
    ]