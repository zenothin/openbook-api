# Generated by Django 2.1.3 on 2018-11-19 17:57

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('openbook_posts', '0010_auto_20181119_1520'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='postreaction',
            unique_together={('reactor', 'post')},
        ),
    ]
