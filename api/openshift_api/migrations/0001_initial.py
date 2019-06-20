# Generated by Django 2.1.2 on 2019-02-26 07:23

import common.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ansible_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('project_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ansible_api.Project')),
                ('template', models.CharField(blank=True, default='', max_length=64)),
                ('current_task_id', models.CharField(blank=True, default='', max_length=128)),
                ('is_super', models.BooleanField(default=False)),
            ],
            bases=('ansible_api.project',),
        ),
        migrations.CreateModel(
            name='DeployExecution',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('timedelta', models.FloatField(default=0.0, null=True, verbose_name='Time')),
                ('state', models.CharField(choices=[('PENDING', 'Pending'), ('STARTED', 'Started'), ('SUCCESS', 'Success'), ('FAILURE', 'Failure'), ('RETRY', 'Retry')], default='PENDING', max_length=16)),
                ('num', models.IntegerField(default=1)),
                ('result_summary', common.models.JsonDictTextField(blank=True, default={}, null=True, verbose_name='Result summary')),
                ('result_raw', common.models.JsonDictTextField(blank=True, default={}, null=True, verbose_name='Result raw')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Create time')),
                ('date_start', models.DateTimeField(null=True, verbose_name='Start time')),
                ('date_end', models.DateTimeField(null=True, verbose_name='End time')),
                ('operation', models.CharField(blank=True, choices=[('install', 'install'), ('upgrade', 'upgrade'), ('uninstall', 'uninstall')], default='install', max_length=128)),
                ('current_task', models.CharField(blank=True, default=None, max_length=128, null=True)),
                ('progress', models.FloatField(blank=True, default=0.0, max_length=64, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ansible_api.Project')),
            ],
            options={
                'ordering': ('-date_created',),
                'get_latest_by': 'date_created',
            },
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('name', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator(message='Enter a valid name consisting of Unicode letters, numbers, underscores, or hyphens, or dot', regex='^[a-zA-Z0-9_\\-\\.]+$')])),
                ('ip', models.GenericIPAddressField(null=True)),
                ('port', models.IntegerField(default=22)),
                ('username', models.CharField(default='root', max_length=256)),
                ('password', common.models.EncryptCharField(blank=True, max_length=4096, null=True)),
                ('private_key', common.models.EncryptCharField(blank=True, max_length=8192, null=True)),
                ('vars', common.models.JsonDictTextField(default={})),
                ('meta', common.models.JsonDictTextField(default={})),
                ('comment', models.TextField(blank=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('memory', models.BigIntegerField(default=0)),
                ('os', models.CharField(default='', max_length=128)),
                ('os_version', models.CharField(default='', max_length=128)),
                ('cpu_core', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('host_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ansible_api.Host')),
                ('host', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='host', to='openshift_api.Host')),
            ],
            options={
                'abstract': False,
            },
            bases=('ansible_api.host',),
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='Name')),
                ('meta', common.models.JsonTextField(blank=True, null=True, verbose_name='Meta')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
            ],
            options={
                'verbose_name': 'Package',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('ansible_api.group',),
        ),
        migrations.AddField(
            model_name='host',
            name='node',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='node', to='openshift_api.Node'),
        ),
        migrations.AddField(
            model_name='cluster',
            name='package',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='openshift_api.Package'),
        ),
    ]