# Generated by Django 5.1.1 on 2024-10-24 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_rename_course_list_coursemodel_course_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursemodel',
            name='course_link',
            field=models.CharField(default='https://www.youtube.com/watch?v=qY90Gi1XrSA', max_length=400),
        ),
    ]
