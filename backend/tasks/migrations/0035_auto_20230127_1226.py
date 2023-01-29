# Generated by Django 3.2.16 on 2023-01-27 12:26


from django.db import migrations, models
from django.db.models import Q
from tasks.models import Annotation, Task
from tasks.views import SentenceOperationViewSet


def change_task_status(apps, schema_editor):
    # tasks objects status update
    tasks = apps.get_model("tasks", "Task")
    proj = apps.get_model("projects","Project")
    db_alias = schema_editor.connection.alias
    taskobj = tasks.objects.using(db_alias).all()
    task1 = taskobj.filter(
        task_status__in=["unlabeled", "skipped", "draft", "to_be_revised"]
    )

    proj_rev_en = proj.objects.using(db.alias).filter(enable_task_reviews=True)
    proj_rev_dis = proj.objects.using(db.alias).filter(enable_task_reviews=False)

    task1_list = []
    for tas1 in task1:
        setattr(tas1, "task_status", "incomplete")
        task1_list.append(tas1)
    Task.objects.bulk_update(task1_list, ["task_status"], 512)

    task2 = taskobj.filter(task_status="labeled")
    task2_list = []
    for tas2 in task2:
        setattr(tas2, "task_status", "annotated")
        task2_list.append(tas2)
    Task.objects.bulk_update(task2_list, ["task_status"], 512)


    

    task_rev_en = taskobj.filter(task_status__in=["accepted", "accepted_with_changes"], project_id__in=proj_rev_en)
    task_rev_dis = taskobj.filter(task_status__in=["accepted", "accepted_with_changes"], project_id__in=proj_rev_dis)

    task_rev_en_list = []
    task_rev_dis_list = []

    for tas_rev_en in task_rev_en:
        setattr(tas_rev_en, "task_status", "reviewed")
        task_rev_en_list.append(tas_rev_en)
    Task.objects.bulk_update(task_rev_en_list, ["task_status"], 512)

    for tas_rev_dis in task_rev_dis:
        setattr(tas_rev_dis, "task_status", "annotated")
        task_rev_dis_list.append(tas_rev_dis)

    Task.objects.bulk_update(task_rev_dis_list, ["task_status"], 512)


    task_orphans = Task.objects.filter(task_status__in=["accepted", "accepted_with_changes"])

    task_orphan_list = []

    for tas in task_orphans:
        setattr(tas, "task_status", "annotated")
        task_orphan_list.append(tas)
    Task.objects.bulk_update(task_orphan_list, ["task_status"], 512)


    task4 = taskobj.filter(task_status="freezed")
    task4_list = []
    for tas4 in task4:
        setattr(tas4, "task_status", "freezed")
        task4_list.append(tas4)
    Task.objects.bulk_update(task4_list, ["task_status"], 512)


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0034_auto_20230127_1221"),
    ]
    operations = [
        migrations.RunPython(change_task_status),
        migrations.AlterField(
            model_name="task",
            name="task_status",
            field=models.CharField(
                choices=[
                    ("incomplete", "incomplete"),
                    ("annotated", "annotated"),
                    ("reviewed", "reviewed"),
                    ("exported", "exported"),
                    ("freezed", "freezed"),
                ],
                default="incomplete",
                max_length=100,
                verbose_name="task_status",
            ),
        ),
    ]
