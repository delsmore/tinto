# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:

        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:


        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:

        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:

        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:

        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:

        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:

        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:

        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:

        db_table = 'django_session'


class Institution(models.Model):
    id = models.IntegerField(primary_key=True)
    original_instid = models.CharField(max_length=3, blank=True, null=True)
    instcode = models.CharField(max_length=10, blank=True, null=True)
    instname = models.CharField(max_length=71, blank=True, null=True)
    federation_instname = models.CharField(max_length=71, blank=True, null=True)
    instaddress1 = models.CharField(max_length=30, blank=True, null=True)
    instaddress2 = models.CharField(max_length=30, blank=True, null=True)
    instaddress3 = models.CharField(max_length=24, blank=True, null=True)
    instcity = models.CharField(max_length=21, blank=True, null=True)
    instcounty = models.CharField(max_length=24, blank=True, null=True)
    instpostcode = models.CharField(max_length=10, blank=True, null=True)
    primary_scope = models.CharField(max_length=30, blank=True, null=True)
    ukbcodes = models.CharField(max_length=10, blank=True, null=True)
    ukbdoc = models.CharField(max_length=10, blank=True, null=True)
    links = models.CharField(max_length=3, blank=True, null=True)
    notes = models.CharField(max_length=554, blank=True, null=True)
    sdssnotes = models.CharField(max_length=400, blank=True, null=True)
    csa = models.CharField(max_length=10, blank=True, null=True)
    itype = models.CharField(max_length=9, blank=True, null=True)
    ccusers = models.CharField(max_length=13, blank=True, null=True)
    group_name = models.CharField(max_length=29, blank=True, null=True)
    submitter = models.CharField(max_length=15, blank=True, null=True)
    create_date = models.CharField(max_length=29, blank=True, null=True)
    last_modified = models.CharField(max_length=18, blank=True, null=True)
    modified_date = models.CharField(max_length=29, blank=True, null=True)
    athens = models.CharField(max_length=5, blank=True, null=True)
    joindate = models.CharField(max_length=19, blank=True, null=True)
    parentid = models.CharField(max_length=5, blank=True, null=True)
    instcountry = models.CharField(max_length=24, blank=True, null=True)
    fedstatus = models.CharField(max_length=13, blank=True, null=True)
    jiscband = models.CharField(max_length=2, blank=True, null=True)

    class Meta:

        db_table = 'institution'
        ordering = ['instname']

    def __str__(self):
        return self.instname







class People(models.Model):
    uun = models.CharField(max_length=8, default=None, blank=True, null=True)
    name = models.CharField(max_length=100)
    # slug = AutoSlugField(populate_from='name', null=True)
    email = models.CharField(max_length=100, default=None, blank=True, null=True)
    telephone = models.CharField(max_length=50, default=None, blank=True, null=True)
    department = models.CharField(max_length=100, default=None, blank=True, null=True)

    # image = models.FileField(upload_to=only_filename, default=None, blank=True, null=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    id = models.IntegerField(primary_key=True)
    servicename = models.CharField(max_length=36, blank=True, null=True)
    resource_name = models.CharField(max_length=23, blank=True, null=True)
    activeflag = models.IntegerField(blank=True, null=True)
    licence_flag = models.IntegerField(blank=True, null=True)
    service_code = models.CharField(max_length=21, blank=True, null=True)
    servicecode_shibb = models.CharField(max_length=18, blank=True, null=True)
    shibb_enabled = models.CharField(max_length=5, blank=True, null=True)
    stats_file_name = models.CharField(max_length=10, blank=True, null=True)
    is_free_service = models.CharField(max_length=5, blank=True, null=True)
    my_athens_description = models.CharField(max_length=504, blank=True, null=True)
    my_athens_title = models.CharField(max_length=46, blank=True, null=True)
    my_athens_url = models.CharField(max_length=40, blank=True, null=True)
    omit_from_call_list = models.CharField(max_length=5, blank=True, null=True)
    service_owner = models.ForeignKey(People, related_name='so', on_delete=models.CASCADE, default=None, blank=True,
                                      null=True)

    class Meta:

        db_table = 'service'
        ordering = ['servicename']

    def __str__(self):
        return self.servicename


class Licence(models.Model):
    id = models.IntegerField(primary_key=True)
    institution = models.ForeignKey(Institution, related_name='inst', on_delete=models.CASCADE, default=None,blank=True, null=True)
    service = models.ForeignKey(Service, related_name='serv', on_delete=models.CASCADE, default=None, blank=True,
                                null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    invoicedate = models.DateField(blank=True, null=True)
    original_instlicenceid = models.CharField(max_length=4, blank=True, null=True)
    original_instid = models.CharField(max_length=3, blank=True, null=True)
    original_serviceid = models.CharField(max_length=2, blank=True, null=True)



    class Meta:
        db_table = 'licence'
        ordering = ['-start_date']


    def __str__(self):
        return str(self.service) + ' - ' + str(self.institution)


