# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AcadPlanTblLtd(models.Model):
    institutecode = models.CharField(db_column='instituteCode', primary_key=True, max_length=10)  # Field name made lowercase.
    institute = models.CharField(max_length=50, blank=True, null=True)
    acad_plan = models.CharField(db_column='ACAD_PLAN', max_length=20)  # Field name made lowercase.
    degree = models.CharField(db_column='DEGREE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    degree_descr = models.CharField(db_column='DEGREE_DESCR', max_length=30, blank=True, null=True)  # Field name made lowercase.
    degree_long_descr = models.CharField(db_column='DEGREE_LONG_DESCR', max_length=120, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ACAD_PLAN_TBL_LTD'
        unique_together = (('institutecode', 'acad_plan'),)


class MapsAcadPlan(models.Model):
    institution = models.ForeignKey('MapsInstitutions', models.DO_NOTHING, primary_key=True)
    degree = models.CharField(max_length=10)
    level = models.CharField(max_length=10)
    degree_descr = models.CharField(max_length=150, blank=True, null=True)
    level_descr = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MAPS_ACAD_PLAN'
        unique_together = (('institution', 'degree', 'level'),)


class MapsCrseCatalog(models.Model):
    course_id = models.CharField(primary_key=True, max_length=7)
    eff_date = models.DateField()
    institute = models.ForeignKey('MapsInstitutions', models.DO_NOTHING, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    subject = models.CharField(max_length=7, blank=True, null=True)
    catalog = models.CharField(max_length=10, blank=True, null=True)
    descr = models.CharField(max_length=50, blank=True, null=True)
    min_units = models.CharField(max_length=7, blank=True, null=True)
    max_units = models.CharField(max_length=7, blank=True, null=True)
    designation = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MAPS_CRSE_CATALOG'
        unique_together = (('course_id', 'eff_date'),)


class MapsDmapsLists(models.Model):
    map = models.ForeignKey('MapsDmapsMeta', models.DO_NOTHING, primary_key=True)
    semester_num = models.IntegerField()
    course1 = models.ForeignKey(MapsCrseCatalog,  models.DO_NOTHING, related_name='course1', db_column='course1', blank=True, null=True)
    course2 = models.ForeignKey(MapsCrseCatalog,  models.DO_NOTHING, related_name='course2', db_column='course2', blank=True, null=True)
    course3 = models.ForeignKey(MapsCrseCatalog,  models.DO_NOTHING, related_name='course3', db_column='course3', blank=True, null=True)
    course4 = models.ForeignKey(MapsCrseCatalog,  models.DO_NOTHING, related_name='course4', db_column='course4', blank=True, null=True)
    course5 = models.ForeignKey(MapsCrseCatalog,  models.DO_NOTHING, related_name='course5', db_column='course5', blank=True, null=True)
    course6 = models.ForeignKey(MapsCrseCatalog,  models.DO_NOTHING, related_name='course6', db_column='course6', blank=True, null=True)
    course7 = models.ForeignKey(MapsCrseCatalog,  models.DO_NOTHING, related_name='course7', db_column='course7', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MAPS_DMAPS_LISTS'
        unique_together = (('map', 'semester_num'),)


class MapsDmapsMeta(models.Model):
    map_id = models.AutoField(primary_key=True)
    map_name = models.CharField(max_length=50, blank=True, null=True)
    degree = models.CharField(max_length=20, blank=True, null=True)
    start_year = models.CharField(max_length=7, blank=True, null=True)
    active_status = models.CharField(max_length=1)
    institution = models.ForeignKey('MapsInstitutions', models.DO_NOTHING, blank=True, null=True)
    submit_id = models.CharField(max_length=8, blank=True, null=True)
    submit_time = models.DateTimeField(blank=True, null=True)
    last_update = models.CharField(max_length=8, blank=True, null=True)
    last_update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MAPS_DMAPS_META'


class MapsInstitutions(models.Model):
    code = models.CharField(max_length=10, blank=True, null=True)
    descr = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MAPS_INSTITUTIONS'


class PsCrseCatalog(models.Model):
    crse_id = models.CharField(db_column='CRSE_ID', max_length=6)  # Field name made lowercase.
    effdt = models.DateTimeField(db_column='EFFDT')  # Field name made lowercase.
    eff_status = models.CharField(db_column='EFF_STATUS', max_length=1)  # Field name made lowercase.
    descr = models.CharField(db_column='DESCR', max_length=30)  # Field name made lowercase.
    equiv_crse_id = models.CharField(db_column='EQUIV_CRSE_ID', max_length=5)  # Field name made lowercase.
    consent = models.CharField(db_column='CONSENT', max_length=1)  # Field name made lowercase.
    allow_mult_enroll = models.CharField(db_column='ALLOW_MULT_ENROLL', max_length=1)  # Field name made lowercase.
    units_minimum = models.DecimalField(db_column='UNITS_MINIMUM', max_digits=5, decimal_places=2)  # Field name made lowercase.
    units_maximum = models.DecimalField(db_column='UNITS_MAXIMUM', max_digits=5, decimal_places=2)  # Field name made lowercase.
    units_acad_prog = models.DecimalField(db_column='UNITS_ACAD_PROG', max_digits=5, decimal_places=2)  # Field name made lowercase.
    units_finaid_prog = models.DecimalField(db_column='UNITS_FINAID_PROG', max_digits=5, decimal_places=2)  # Field name made lowercase.
    crse_repeatable = models.CharField(db_column='CRSE_REPEATABLE', max_length=1)  # Field name made lowercase.
    units_repeat_limit = models.DecimalField(db_column='UNITS_REPEAT_LIMIT', max_digits=5, decimal_places=2)  # Field name made lowercase.
    crse_repeat_limit = models.DecimalField(db_column='CRSE_REPEAT_LIMIT', max_digits=38, decimal_places=0)  # Field name made lowercase.
    grading_basis = models.CharField(db_column='GRADING_BASIS', max_length=3)  # Field name made lowercase.
    grade_roster_print = models.CharField(db_column='GRADE_ROSTER_PRINT', max_length=1)  # Field name made lowercase.
    ssr_component = models.CharField(db_column='SSR_COMPONENT', max_length=3)  # Field name made lowercase.
    course_title_long = models.CharField(db_column='COURSE_TITLE_LONG', max_length=100)  # Field name made lowercase.
    lst_mult_trm_crs = models.CharField(db_column='LST_MULT_TRM_CRS', max_length=1)  # Field name made lowercase.
    crse_contact_hrs = models.DecimalField(db_column='CRSE_CONTACT_HRS', max_digits=5, decimal_places=2)  # Field name made lowercase.
    rqmnt_designtn = models.CharField(db_column='RQMNT_DESIGNTN', max_length=4)  # Field name made lowercase.
    crse_count = models.DecimalField(db_column='CRSE_COUNT', max_digits=4, decimal_places=2)  # Field name made lowercase.
    instructor_edit = models.CharField(db_column='INSTRUCTOR_EDIT', max_length=2)  # Field name made lowercase.
    fees_exist = models.CharField(db_column='FEES_EXIST', max_length=1)  # Field name made lowercase.
    component_primary = models.CharField(db_column='COMPONENT_PRIMARY', max_length=3)  # Field name made lowercase.
    enrl_un_ld_clc_typ = models.CharField(db_column='ENRL_UN_LD_CLC_TYP', max_length=1)  # Field name made lowercase.
    ssr_drop_consent = models.CharField(db_column='SSR_DROP_CONSENT', max_length=1)  # Field name made lowercase.
    scc_row_add_oprid = models.CharField(db_column='SCC_ROW_ADD_OPRID', max_length=30)  # Field name made lowercase.
    scc_row_add_dttm = models.DateTimeField(db_column='SCC_ROW_ADD_DTTM', blank=True, null=True)  # Field name made lowercase.
    scc_row_upd_oprid = models.CharField(db_column='SCC_ROW_UPD_OPRID', max_length=30)  # Field name made lowercase.
    scc_row_upd_dttm = models.DateTimeField(db_column='SCC_ROW_UPD_DTTM', blank=True, null=True)  # Field name made lowercase.
    descrlong = models.TextField(db_column='DESCRLONG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PS_CRSE_CATALOG'
        unique_together = (('crse_id', 'effdt'),)


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


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CrseCatalogLtd(models.Model):
    institute_code = models.CharField(max_length=10, blank=True, null=True)
    institute_desc = models.CharField(max_length=30, blank=True, null=True)
    course_id = models.CharField(db_column='course_ID', max_length=6, blank=True, null=True)  # Field name made lowercase.
    eff_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    subject = models.CharField(max_length=7, blank=True, null=True)
    catalog = models.CharField(max_length=10, blank=True, null=True)
    descr = models.CharField(max_length=50, blank=True, null=True)
    min_units = models.CharField(max_length=7, blank=True, null=True)
    max_units = models.CharField(max_length=7, blank=True, null=True)
    designation = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crse_catalog_ltd'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

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
