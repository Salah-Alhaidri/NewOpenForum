# Generated by Django 5.1.3 on 2024-11-30 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0007_rename_board_forummodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='board',
            new_name='forumboard',
        ),
    ]
