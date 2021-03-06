# Generated by Django 3.0.7 on 2020-07-20 01:21

from django.conf import settings
import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('updated_dt', models.DateTimeField(auto_now=True)),
                ('data_source', models.CharField(blank=True, max_length=64, null=True)),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('article_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('updated_dt', models.DateTimeField(auto_now=True)),
                ('data_source', models.CharField(blank=True, max_length=64, null=True)),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('component_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('component_purl', models.CharField(help_text='Package URL for this component.', max_length=1024, unique=True)),
                ('name', models.CharField(help_text='Name of the component', max_length=512)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ComponentVersion',
            fields=[
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('updated_dt', models.DateTimeField(auto_now=True)),
                ('data_source', models.CharField(blank=True, max_length=64, null=True)),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('component_version_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('version', models.CharField(blank=True, max_length=128, null=True)),
                ('description', models.TextField(null=True)),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='componentversion_set', to='oss.Component')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CPE',
            fields=[
                ('cpe_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=512, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Maintainer',
            fields=[
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('maintainer_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('names', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=128), blank=True, null=True, size=None)),
                ('emails', django.contrib.postgres.fields.ArrayField(base_field=models.EmailField(max_length=254), blank=True, null=True, size=None)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('url_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('url_type', models.CharField(choices=[('SOURCE_REPO', 'Source Code Repository'), ('PACKAGE_REPO', 'Package Repository'), ('DOCUMENTATION', 'Documentation'), ('FUNDING', 'Funding'), ('ISSUE_TRACKER', 'Issue Tracker'), ('HOME_PAGE', 'Home Page'), ('DOWNLOAD', 'Download'), ('OTHER', 'Other')], db_index=True, max_length=32)),
                ('url', models.URLField(db_index=True)),
            ],
            options={
                'verbose_name': 'URL',
                'verbose_name_plural': 'URLs',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('updated_dt', models.DateTimeField(auto_now=True)),
                ('data_source', models.CharField(blank=True, max_length=64, null=True)),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('review_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('review_type', models.CharField(choices=[('SECURITY', 'Security'), ('OTHER', 'Other')], db_index=True, max_length=32)),
                ('state', models.CharField(choices=[('DRAFT', 'Draft'), ('PUBLISHED', 'Published'), ('REMOVED', 'Removed'), ('OTEHR', 'Other')], db_index=True, max_length=32)),
                ('title', models.CharField(max_length=512)),
                ('text', models.TextField(blank=True, null=True)),
                ('published_by', models.CharField(blank=True, max_length=512, null=True)),
                ('published_dt', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('urls', models.ManyToManyField(blank=True, to='oss.Url')),
                ('versions', models.ManyToManyField(to='oss.ComponentVersion')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='CVEDatafile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('updated_dt', models.DateTimeField(auto_now=True)),
                ('data_source', models.CharField(blank=True, max_length=64, null=True)),
                ('url', models.URLField()),
                ('last_updated', models.DateTimeField(null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CVE',
            fields=[
                ('cve_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('cve_ext_id', models.CharField(db_index=True, max_length=32)),
                ('title', models.TextField(blank=True, null=True)),
                ('raw', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('cpes', models.ManyToManyField(to='oss.CPE')),
            ],
        ),
        migrations.AddField(
            model_name='componentversion',
            name='maintainers',
            field=models.ManyToManyField(to='oss.Maintainer'),
        ),
        migrations.AddField(
            model_name='componentversion',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='componentversion',
            name='urls',
            field=models.ManyToManyField(to='oss.Url'),
        ),
        migrations.CreateModel(
            name='Artifact',
            fields=[
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('artifact_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('artifact_type', models.CharField(choices=[('SOURCE', 'Source Code Artifact'), ('BINARY', 'Binary Artifact'), ('OTHER', 'Other')], max_length=128)),
                ('artifact_subtype', models.CharField(max_length=128, null=True)),
                ('filename', models.CharField(max_length=1024, null=True)),
                ('url', models.URLField(null=True)),
                ('digest', models.CharField(max_length=512, null=True)),
                ('description', models.TextField(null=True)),
                ('size', models.BigIntegerField(default=0, null=True)),
                ('download_count', models.BigIntegerField(default=0, null=True)),
                ('publish_date', models.DateTimeField(null=True)),
                ('active', models.BooleanField(default=True)),
                ('component_version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oss.ComponentVersion')),
                ('dependencies', models.ManyToManyField(to='oss.Component')),
            ],
            options={
                'verbose_name': 'Artifact',
                'verbose_name_plural': 'Artifacts',
                'ordering': ['filename'],
            },
        ),
        migrations.CreateModel(
            name='ArticleRevision',
            fields=[
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('updated_dt', models.DateTimeField(auto_now=True)),
                ('data_source', models.CharField(blank=True, max_length=64, null=True)),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('article_revision_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=1024)),
                ('content', models.TextField(blank=True, null=True)),
                ('state', models.CharField(choices=[('DRAFT', 'Draft'), ('PUBLISHED', 'Published'), ('REMOVED', 'Removed'), ('OTEHR', 'Other')], db_index=True, max_length=32)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oss.Article')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='article',
            name='current',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parent', to='oss.ArticleRevision'),
        ),
        migrations.AddField(
            model_name='article',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]
