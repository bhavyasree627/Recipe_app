# Generated by Django 5.0.2 on 2024-02-13 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0006_department_studentid_student'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='deprtment',
            new_name='department',
        ),
    ]
