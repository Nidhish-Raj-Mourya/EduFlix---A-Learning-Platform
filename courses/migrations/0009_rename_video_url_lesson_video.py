# Generated by Django 3.2.2 on 2021-05-20 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_alter_lesson_video_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='video_url',
            new_name='video',
        ),
    ]
