# Generated by Django 5.1.3 on 2024-11-30 19:07

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0012_alter_forummodel_forumimage'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Topic',
            new_name='ForumSectionModel',
        ),
    ]
