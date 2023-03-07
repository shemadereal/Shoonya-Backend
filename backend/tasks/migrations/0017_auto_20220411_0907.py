# Generated by Django 3.1.14 on 2022-04-11 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0016_tasklock"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="correct_annotation",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="correct_annotation",
                to="tasks.annotation",
            ),
        ),
    ]
