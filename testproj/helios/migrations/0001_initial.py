# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-05 16:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='helios.AuthGroup')),
            ],
            options={
                'db_table': 'auth_group_permissions',
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=30, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='helios.AuthGroup')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='helios.AuthUser')),
            ],
            options={
                'db_table': 'auth_user_groups',
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='helios.AuthPermission')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='helios.AuthUser')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
            },
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('original_instid', models.CharField(blank=True, max_length=3, null=True)),
                ('instcode', models.CharField(blank=True, max_length=10, null=True)),
                ('instname', models.CharField(blank=True, max_length=71, null=True)),
                ('federation_instname', models.CharField(blank=True, max_length=71, null=True)),
                ('instaddress1', models.CharField(blank=True, max_length=30, null=True)),
                ('instaddress2', models.CharField(blank=True, max_length=30, null=True)),
                ('instaddress3', models.CharField(blank=True, max_length=24, null=True)),
                ('instcity', models.CharField(blank=True, max_length=21, null=True)),
                ('instcounty', models.CharField(blank=True, max_length=24, null=True)),
                ('instpostcode', models.CharField(blank=True, max_length=10, null=True)),
                ('primary_scope', models.CharField(blank=True, max_length=30, null=True)),
                ('ukbcodes', models.CharField(blank=True, max_length=10, null=True)),
                ('ukbdoc', models.CharField(blank=True, max_length=10, null=True)),
                ('links', models.CharField(blank=True, max_length=3, null=True)),
                ('notes', models.CharField(blank=True, max_length=554, null=True)),
                ('sdssnotes', models.CharField(blank=True, max_length=400, null=True)),
                ('csa', models.CharField(blank=True, max_length=10, null=True)),
                ('itype', models.CharField(blank=True, max_length=9, null=True)),
                ('ccusers', models.CharField(blank=True, max_length=13, null=True)),
                ('group_name', models.CharField(blank=True, max_length=29, null=True)),
                ('submitter', models.CharField(blank=True, max_length=15, null=True)),
                ('create_date', models.CharField(blank=True, max_length=29, null=True)),
                ('last_modified', models.CharField(blank=True, max_length=18, null=True)),
                ('modified_date', models.CharField(blank=True, max_length=29, null=True)),
                ('athens', models.CharField(blank=True, max_length=5, null=True)),
                ('joindate', models.CharField(blank=True, max_length=19, null=True)),
                ('parentid', models.CharField(blank=True, max_length=5, null=True)),
                ('instcountry', models.CharField(blank=True, max_length=24, null=True)),
                ('fedstatus', models.CharField(blank=True, max_length=13, null=True)),
                ('jiscband', models.CharField(blank=True, max_length=2, null=True)),
            ],
            options={
                'db_table': 'institution',
            },
        ),
        migrations.CreateModel(
            name='Licence',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('invoicedate', models.DateField(blank=True, null=True)),
                ('original_instlicenceid', models.CharField(blank=True, max_length=4, null=True)),
                ('original_instid', models.CharField(blank=True, max_length=3, null=True)),
                ('original_serviceid', models.CharField(blank=True, max_length=2, null=True)),
                ('institution', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inst', to='helios.Institution')),
            ],
            options={
                'db_table': 'licence',
            },
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uun', models.CharField(blank=True, default=None, max_length=8, null=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('telephone', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('department', models.CharField(blank=True, default=None, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('servicename', models.CharField(blank=True, max_length=36, null=True)),
                ('resource_name', models.CharField(blank=True, max_length=23, null=True)),
                ('activeflag', models.IntegerField(blank=True, null=True)),
                ('licence_flag', models.IntegerField(blank=True, null=True)),
                ('service_code', models.CharField(blank=True, max_length=21, null=True)),
                ('servicecode_shibb', models.CharField(blank=True, max_length=18, null=True)),
                ('shibb_enabled', models.CharField(blank=True, max_length=5, null=True)),
                ('stats_file_name', models.CharField(blank=True, max_length=10, null=True)),
                ('is_free_service', models.CharField(blank=True, max_length=5, null=True)),
                ('my_athens_description', models.CharField(blank=True, max_length=504, null=True)),
                ('my_athens_title', models.CharField(blank=True, max_length=46, null=True)),
                ('my_athens_url', models.CharField(blank=True, max_length=40, null=True)),
                ('omit_from_call_list', models.CharField(blank=True, max_length=5, null=True)),
                ('service_owner', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='so', to='helios.People')),
            ],
            options={
                'db_table': 'service',
            },
        ),
        migrations.AddField(
            model_name='licence',
            name='service',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='serv', to='helios.Service'),
        ),
        migrations.AlterUniqueTogether(
            name='djangocontenttype',
            unique_together=set([('app_label', 'model')]),
        ),
        migrations.AddField(
            model_name='djangoadminlog',
            name='content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='helios.DjangoContentType'),
        ),
        migrations.AddField(
            model_name='djangoadminlog',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='helios.AuthUser'),
        ),
        migrations.AddField(
            model_name='authpermission',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='helios.DjangoContentType'),
        ),
        migrations.AddField(
            model_name='authgrouppermissions',
            name='permission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='helios.AuthPermission'),
        ),
        migrations.AlterUniqueTogether(
            name='authuseruserpermissions',
            unique_together=set([('user', 'permission')]),
        ),
        migrations.AlterUniqueTogether(
            name='authusergroups',
            unique_together=set([('user', 'group')]),
        ),
        migrations.AlterUniqueTogether(
            name='authpermission',
            unique_together=set([('content_type', 'codename')]),
        ),
        migrations.AlterUniqueTogether(
            name='authgrouppermissions',
            unique_together=set([('group', 'permission')]),
        ),
    ]
