# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UserManagementUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class UserManagementRole(models.Model):
    id = models.BigAutoField(primary_key=True)
    role_name = models.CharField(unique=True, max_length=288)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey('UserManagementUser', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('UserManagementUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_management_role'


class UserManagementRolepermission(models.Model):
    id = models.BigAutoField(primary_key=True)
    permission_name = models.CharField(max_length=288)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    role = models.ForeignKey(UserManagementRole, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_management_rolepermission'


class UserManagementUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    username = models.CharField(unique=True, max_length=288)
    role_name = models.CharField(max_length=288, blank=True, null=True)
    email = models.CharField(max_length=288)
    user_type = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    is_staff = models.BooleanField()
    is_superuser = models.BooleanField()
    is_password_reset = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    is_active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'user_management_user'


class UserManagementUser2(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=200)
    role_name = models.CharField(max_length=200)
    role_name1 = models.CharField(max_length=200)
    email = models.CharField(max_length=254)
    cat = models.CharField(max_length=200)
    cat3 = models.CharField(max_length=200)
    cat4 = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'user_management_user2'


class UserManagementUser4(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=200)
    role_name = models.CharField(max_length=200)
    role_name1 = models.CharField(max_length=200)
    email = models.CharField(max_length=254)
    cat = models.CharField(max_length=200)
    cat3 = models.CharField(max_length=200)
    cat4 = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'user_management_user4'


class UserManagementUser5(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=200)
    role_name = models.CharField(max_length=200)
    role_name1 = models.CharField(max_length=200)
    email = models.CharField(max_length=254)
    cat = models.CharField(max_length=200)
    cat3 = models.CharField(max_length=200)
    cat4 = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'user_management_user5'


class UserManagementUser6(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=200)
    role_name = models.CharField(max_length=200)
    role_name1 = models.CharField(max_length=200)
    email = models.CharField(max_length=254)
    cat = models.CharField(max_length=200)
    cat3 = models.CharField(max_length=200)
    cat4 = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'user_management_user6'


class UserManagementUserGroups(models.Model):
    user = models.ForeignKey(UserManagementUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_management_user_groups'
        unique_together = (('user', 'group'),)


class UserManagementUserUserPermissions(models.Model):
    user = models.ForeignKey(UserManagementUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_management_user_user_permissions'
        unique_together = (('user', 'permission'),)


class UserManagementUserprofiledetails(models.Model):
    id = models.UUIDField(primary_key=True)
    mobile_num = models.CharField(unique=True, max_length=50)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    present_address = models.JSONField()
    permanent_address = models.JSONField()
    other_details = models.JSONField(blank=True, null=True)
    crated_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    ops_profile = models.OneToOneField(UserManagementUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_management_userprofiledetails'
