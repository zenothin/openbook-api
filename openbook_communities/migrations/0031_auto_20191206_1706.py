# Generated by Django 2.2.5 on 2019-12-06 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_communities', '0030_communitynotificationssubscription_new_posts_notifications'),
    ]

    operations = [
        migrations.RenameField(
            model_name='communitynotificationssubscription',
            old_name='new_posts_notifications',
            new_name='new_posts_notifications_enabled',
        ),
    ]