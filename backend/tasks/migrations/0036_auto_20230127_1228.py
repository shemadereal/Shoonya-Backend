# Generated by Django 3.2.16 on 2023-01-27 12:28


from django.db import migrations, models
from projects.utils import no_of_words
from dataset.models import DatasetInstance
from dataset import models as dataset_models
from tasks.models import Task
from tqdm import tqdm


def add_word_count(apps, schema_editor):
    tasks = apps.get_model("tasks", "Task")
    db_alias = schema_editor.connection.alias
    taskobj = tasks.objects.using(db_alias).all()
    taskobj_list = []
    for tas in tqdm(taskobj):
        data = tas.data
        try:
            if "word_count" in tas.data.keys():
                pass
            else:
                if "input_text" in tas.data.keys():
                    try:
                        data["word_count"] = no_of_words(tas.data["input_text"])
                    except TypeError:
                        pass
                    except:
                        data["word_count"] = 0
                elif "text" in tas.data.keys():
                    try:
                        data["word_count"] = no_of_words(tas.data["text"])
                    except TypeError:
                        pass
                    except:
                        data["word_count"] = 0
                setattr(tas, "data", data)
                taskobj_list.append(tas)
        except:
            pass

    Task.objects.bulk_update(taskobj_list, ["data"], 512)


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0035_auto_20230127_1226"),
    ]

    operations = [
        migrations.RunPython(add_word_count),
    ]
