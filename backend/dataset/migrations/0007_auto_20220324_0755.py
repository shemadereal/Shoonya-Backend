# Generated by Django 3.1.14 on 2022-03-24 07:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dataset", "0006_auto_20220319_1007"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ocrdocument",
            name="annotation_json",
        ),
        migrations.RemoveField(
            model_name="ocrdocument",
            name="prediction_json",
        ),
        migrations.AddField(
            model_name="ocrdocument",
            name="annotation_bboxes",
            field=models.JSONField(
                blank=True, null=True, verbose_name="annotation_bboxes"
            ),
        ),
        migrations.AddField(
            model_name="ocrdocument",
            name="annotation_labels",
            field=models.JSONField(
                blank=True, null=True, verbose_name="annotation_labels"
            ),
        ),
        migrations.AddField(
            model_name="ocrdocument",
            name="annotation_transcripts",
            field=models.JSONField(
                blank=True, null=True, verbose_name="annotation_transcripts"
            ),
        ),
        migrations.AlterField(
            model_name="datasetinstance",
            name="dataset_type",
            field=models.CharField(
                choices=[
                    ("sentence_text", "SentenceText"),
                    ("translation_pair", "TranslationPair"),
                    ("OCRDocument", "OCRDocument"),
                ],
                max_length=100,
                verbose_name="dataset_type",
            ),
        ),
    ]
