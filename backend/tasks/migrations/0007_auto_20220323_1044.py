# Generated by Django 3.1.14 on 2022-03-23 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("dataset", "0006_auto_20220319_1023"),
        ("tasks", "0006_auto_20220323_1043"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="output_data",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="output_data_id",
                to="dataset.datasetbase",
                verbose_name="output_data_id",
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="input_data",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="input_data_id",
                to="dataset.datasetbase",
                verbose_name="input_data_id",
            ),
        ),
    ]
