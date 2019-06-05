# Generated by Django 2.2 on 2019-05-17 16:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ModeratedObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1000, null=True, verbose_name='description')),
                ('verified', models.BooleanField(default=False, verbose_name='verified')),
                ('status', models.CharField(choices=[('P', 'Pending'), ('A', 'Approved'), ('R', 'Rejected')], default='P', max_length=5)),
                ('object_audit_snapshot', models.TextField(verbose_name='object_audit_snapshot')),
                ('object_type', models.CharField(choices=[('P', 'Post'), ('PC', 'Post Comment'), ('C', 'Community'), ('U', 'User')], max_length=5)),
                ('object_id', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ModeratedObjectDescriptionChangedLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('changed_from', models.CharField(max_length=1000, verbose_name='changed from')),
                ('changed_to', models.CharField(max_length=1000, verbose_name='changed to')),
            ],
        ),
        migrations.CreateModel(
            name='ModeratedObjectStatusChangedLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('changed_from', models.CharField(choices=[('P', 'Pending'), ('A', 'Approved'), ('R', 'Rejected')], max_length=5, verbose_name='changed from')),
                ('changed_to', models.CharField(max_length=5, verbose_name='changed to')),
            ],
        ),
        migrations.CreateModel(
            name='ModeratedObjectSubmittedChangedLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('changed_from', models.BooleanField(verbose_name='changed from')),
                ('changed_to', models.BooleanField(verbose_name='changed to')),
            ],
        ),
        migrations.CreateModel(
            name='ModeratedObjectVerifiedChangedLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('changed_from', models.BooleanField(verbose_name='changed from')),
                ('changed_to', models.BooleanField(verbose_name='changed to')),
            ],
        ),
        migrations.CreateModel(
            name='ModerationCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='name')),
                ('title', models.CharField(max_length=64, verbose_name='title')),
                ('title_es', models.CharField(max_length=64, null=True, verbose_name='title')),
                ('title_en', models.CharField(max_length=64, null=True, verbose_name='title')),
                ('description', models.CharField(max_length=255, verbose_name='description')),
                ('description_es', models.CharField(max_length=255, null=True, verbose_name='description')),
                ('description_en', models.CharField(max_length=255, null=True, verbose_name='description')),
                ('created', models.DateTimeField(db_index=True, editable=False)),
                ('severity', models.CharField(choices=[('C', 'Critical'), ('H', 'High'), ('M', 'Medium'), ('L', 'Low')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='ModerationReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1000, null=True, verbose_name='description')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='openbook_moderation.ModerationCategory')),
                ('moderated_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='openbook_moderation.ModeratedObject')),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moderation_reports', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ModerationPenalty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.DurationField(null=True)),
                ('type', models.CharField(choices=[('S', 'Suspension')], max_length=5)),
                ('moderated_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='penalties', to='openbook_moderation.ModeratedObject')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moderation_penalties', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ModeratedObjectLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('DC', 'Description Changed'), ('AC', 'Approved Changed'), ('TC', 'Type Changed'), ('SC', 'Submitted Changed'), ('VC', 'Verified Changed'), ('CC', 'Category Changed')], max_length=5)),
                ('object_id', models.PositiveIntegerField()),
                ('created', models.DateTimeField(db_index=True, editable=False)),
                ('actor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('moderated_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='openbook_moderation.ModeratedObject')),
            ],
        ),
        migrations.CreateModel(
            name='ModeratedObjectCategoryChangedLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('changed_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='openbook_moderation.ModerationCategory')),
                ('changed_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='openbook_moderation.ModerationCategory')),
            ],
        ),
        migrations.AddField(
            model_name='moderatedobject',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moderated_objects', to='openbook_moderation.ModerationCategory'),
        ),
        migrations.AddField(
            model_name='moderatedobject',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
        migrations.AddConstraint(
            model_name='moderationreport',
            constraint=models.UniqueConstraint(fields=('reporter', 'moderated_object'), name='reporter_moderated_object_constraint'),
        ),
        migrations.AddConstraint(
            model_name='moderatedobject',
            constraint=models.UniqueConstraint(fields=('object_type', 'object_id'), name='reporter_moderated_object_constraint'),
        ),
    ]