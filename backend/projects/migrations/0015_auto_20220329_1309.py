# Generated by Django 3.1.14 on 2022-03-29 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_merge_20220328_0807'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='metadata_json',
            field=models.JSONField(blank=True, null=True, verbose_name='metadata json'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_type',
            field=models.CharField(choices=[('MonolingualTranslation', 'MonolingualTranslation'), ('TranslationEditing', 'TranslationEditing'), ('OCRAnnotation', 'OCRAnnotation'), ('MonolingualCollection', 'MonolingualCollection'), ('SentenceSplitting', 'SentenceSplitting')], max_length=100),
        ),
    ]