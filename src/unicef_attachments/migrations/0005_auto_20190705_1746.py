# Generated by Django 2.2 on 2019-07-05 17:46

from django.db import migrations


def update_group(apps, schema_editor):
    FileType = apps.get_model("unicef_attachments", "filetype")
    for file_type in FileType.objects.all():
        file_type.group = [file_type.code]
        file_type.save()


def reverse_update(apps, schema_editor):
    FileType = apps.get_model("unicef_attachments", "filetype")
    for file_type in FileType.objects.all():
        file_type.group = []
        file_type.save()


class Migration(migrations.Migration):

    dependencies = [
        ('unicef_attachments', '0004_filetype_group'),
    ]

    operations = [
        migrations.RunPython(update_group, reverse_code=reverse_update)
    ]
