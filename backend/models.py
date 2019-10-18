# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Admin(models.Model):
    cuny_id = models.CharField(db_column='CUNY_ID', primary_key=True, max_length=8)  # Field name made lowercase.
    username = models.CharField(db_column='USERNAME', unique=True, max_length=20)  # Field name made lowercase.
    passwd = models.CharField(db_column='PASSWD', max_length=30)  # Field name made lowercase.
    first_name = models.CharField(db_column='FIRST_NAME', max_length=50)  # Field name made lowercase.
    last_name = models.CharField(db_column='LAST_NAME', max_length=50)  # Field name made lowercase.
    college_name = models.CharField(db_column='COLLEGE_NAME', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ADMIN'


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


class PsCrseOffer(models.Model):
    crse_id = models.CharField(db_column='CRSE_ID', max_length=6)  # Field name made lowercase.
    effdt = models.DateTimeField(db_column='EFFDT')  # Field name made lowercase.
    crse_offer_nbr = models.DecimalField(db_column='CRSE_OFFER_NBR', max_digits=38, decimal_places=0)  # Field name made lowercase.
    institution = models.CharField(db_column='INSTITUTION', max_length=5)  # Field name made lowercase.
    acad_group = models.CharField(db_column='ACAD_GROUP', max_length=5)  # Field name made lowercase.
    subject = models.CharField(db_column='SUBJECT', max_length=8)  # Field name made lowercase.
    catalog_nbr = models.CharField(db_column='CATALOG_NBR', max_length=10)  # Field name made lowercase.
    course_approved = models.CharField(db_column='COURSE_APPROVED', max_length=1)  # Field name made lowercase.
    campus = models.CharField(db_column='CAMPUS', max_length=5)  # Field name made lowercase.
    schedule_print = models.CharField(db_column='SCHEDULE_PRINT', max_length=1)  # Field name made lowercase.
    catalog_print = models.CharField(db_column='CATALOG_PRINT', max_length=1)  # Field name made lowercase.
    sched_print_instr = models.CharField(db_column='SCHED_PRINT_INSTR', max_length=1)  # Field name made lowercase.
    acad_org = models.CharField(db_column='ACAD_ORG', max_length=10)  # Field name made lowercase.
    acad_career = models.CharField(db_column='ACAD_CAREER', max_length=4)  # Field name made lowercase.
    split_owner = models.CharField(db_column='SPLIT_OWNER', max_length=1)  # Field name made lowercase.
    sched_term_roll = models.CharField(db_column='SCHED_TERM_ROLL', max_length=1)  # Field name made lowercase.
    rqrmnt_group = models.CharField(db_column='RQRMNT_GROUP', max_length=6)  # Field name made lowercase.
    cip_code = models.CharField(db_column='CIP_CODE', max_length=13)  # Field name made lowercase.
    hegis_code = models.CharField(db_column='HEGIS_CODE', max_length=8)  # Field name made lowercase.
    use_blind_grading = models.CharField(db_column='USE_BLIND_GRADING', max_length=1)  # Field name made lowercase.
    rcv_from_item_type = models.CharField(db_column='RCV_FROM_ITEM_TYPE', max_length=1)  # Field name made lowercase.
    ap_bus_unit = models.CharField(db_column='AP_BUS_UNIT', max_length=5)  # Field name made lowercase.
    ap_ledger = models.CharField(db_column='AP_LEDGER', max_length=10)  # Field name made lowercase.
    ap_account = models.CharField(db_column='AP_ACCOUNT', max_length=10)  # Field name made lowercase.
    ap_deptid = models.CharField(db_column='AP_DEPTID', max_length=10)  # Field name made lowercase.
    ap_proj_id = models.CharField(db_column='AP_PROJ_ID', max_length=15)  # Field name made lowercase.
    ap_product = models.CharField(db_column='AP_PRODUCT', max_length=6)  # Field name made lowercase.
    ap_fund_code = models.CharField(db_column='AP_FUND_CODE', max_length=5)  # Field name made lowercase.
    ap_prog_code = models.CharField(db_column='AP_PROG_CODE', max_length=5)  # Field name made lowercase.
    ap_class_fld = models.CharField(db_column='AP_CLASS_FLD', max_length=5)  # Field name made lowercase.
    ap_affiliate = models.CharField(db_column='AP_AFFILIATE', max_length=5)  # Field name made lowercase.
    ap_op_unit = models.CharField(db_column='AP_OP_UNIT', max_length=8)  # Field name made lowercase.
    ap_altacct = models.CharField(db_column='AP_ALTACCT', max_length=10)  # Field name made lowercase.
    ap_bud_ref = models.CharField(db_column='AP_BUD_REF', max_length=8)  # Field name made lowercase.
    ap_cf1 = models.CharField(db_column='AP_CF1', max_length=10)  # Field name made lowercase.
    ap_cf2 = models.CharField(db_column='AP_CF2', max_length=10)  # Field name made lowercase.
    ap_cf3 = models.CharField(db_column='AP_CF3', max_length=10)  # Field name made lowercase.
    ap_aff_int1 = models.CharField(db_column='AP_AFF_INT1', max_length=10)  # Field name made lowercase.
    ap_aff_int2 = models.CharField(db_column='AP_AFF_INT2', max_length=10)  # Field name made lowercase.
    writeoff_bus_unit = models.CharField(db_column='WRITEOFF_BUS_UNIT', max_length=5)  # Field name made lowercase.
    writeoff_ledger = models.CharField(db_column='WRITEOFF_LEDGER', max_length=10)  # Field name made lowercase.
    writeoff_account = models.CharField(db_column='WRITEOFF_ACCOUNT', max_length=10)  # Field name made lowercase.
    writeoff_deptid = models.CharField(db_column='WRITEOFF_DEPTID', max_length=10)  # Field name made lowercase.
    writeoff_proj_id = models.CharField(db_column='WRITEOFF_PROJ_ID', max_length=15)  # Field name made lowercase.
    writeoff_product = models.CharField(db_column='WRITEOFF_PRODUCT', max_length=6)  # Field name made lowercase.
    writeoff_fund_code = models.CharField(db_column='WRITEOFF_FUND_CODE', max_length=5)  # Field name made lowercase.
    writeoff_prog_code = models.CharField(db_column='WRITEOFF_PROG_CODE', max_length=5)  # Field name made lowercase.
    writeoff_class_fld = models.CharField(db_column='WRITEOFF_CLASS_FLD', max_length=5)  # Field name made lowercase.
    writeoff_affiliate = models.CharField(db_column='WRITEOFF_AFFILIATE', max_length=5)  # Field name made lowercase.
    writeoff_op_unit = models.CharField(db_column='WRITEOFF_OP_UNIT', max_length=8)  # Field name made lowercase.
    writeoff_altacct = models.CharField(db_column='WRITEOFF_ALTACCT', max_length=10)  # Field name made lowercase.
    writeoff_bud_ref = models.CharField(db_column='WRITEOFF_BUD_REF', max_length=8)  # Field name made lowercase.
    writeoff_cf1 = models.CharField(db_column='WRITEOFF_CF1', max_length=10)  # Field name made lowercase.
    writeoff_cf2 = models.CharField(db_column='WRITEOFF_CF2', max_length=10)  # Field name made lowercase.
    writeoff_cf3 = models.CharField(db_column='WRITEOFF_CF3', max_length=10)  # Field name made lowercase.
    writeoff_aff_int1 = models.CharField(db_column='WRITEOFF_AFF_INT1', max_length=10)  # Field name made lowercase.
    writeoff_aff_int2 = models.CharField(db_column='WRITEOFF_AFF_INT2', max_length=10)  # Field name made lowercase.
    ext_writeoff = models.CharField(db_column='EXT_WRITEOFF', max_length=50)  # Field name made lowercase.
    gl_interface_req = models.CharField(db_column='GL_INTERFACE_REQ', max_length=1)  # Field name made lowercase.
    sel_group = models.CharField(db_column='SEL_GROUP', max_length=10)  # Field name made lowercase.
    schedule_course = models.CharField(db_column='SCHEDULE_COURSE', max_length=1)  # Field name made lowercase.
    dyn_class_data = models.CharField(db_column='DYN_CLASS_DATA', max_length=10)  # Field name made lowercase.
    oee_ind = models.CharField(db_column='OEE_IND', max_length=1)  # Field name made lowercase.
    oee_dyn_date_rule = models.CharField(db_column='OEE_DYN_DATE_RULE', max_length=10)  # Field name made lowercase.
    ssr_crse_typoff_cd = models.CharField(db_column='SSR_CRSE_TYPOFF_CD', max_length=10)  # Field name made lowercase.
    ssr_ac_exam_only = models.CharField(db_column='SSR_AC_EXAM_ONLY', max_length=1)  # Field name made lowercase.
    scc_row_add_oprid = models.CharField(db_column='SCC_ROW_ADD_OPRID', max_length=30)  # Field name made lowercase.
    scc_row_add_dttm = models.DateTimeField(db_column='SCC_ROW_ADD_DTTM', blank=True, null=True)  # Field name made lowercase.
    scc_row_upd_oprid = models.CharField(db_column='SCC_ROW_UPD_OPRID', max_length=30)  # Field name made lowercase.
    scc_row_upd_dttm = models.DateTimeField(db_column='SCC_ROW_UPD_DTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PS_CRSE_OFFER'
        unique_together = (('crse_id', 'effdt', 'crse_offer_nbr'),)


class PsInstitutionTbl(models.Model):
    institution = models.CharField(db_column='INSTITUTION', max_length=5)  # Field name made lowercase.
    effdt = models.DateTimeField(db_column='EFFDT')  # Field name made lowercase.
    eff_status = models.CharField(db_column='EFF_STATUS', max_length=1)  # Field name made lowercase.
    descr = models.CharField(db_column='DESCR', max_length=30)  # Field name made lowercase.
    descrshort = models.CharField(db_column='DESCRSHORT', max_length=10)  # Field name made lowercase.
    descrformal = models.CharField(db_column='DESCRFORMAL', max_length=50)  # Field name made lowercase.
    country = models.CharField(db_column='COUNTRY', max_length=3)  # Field name made lowercase.
    address1 = models.CharField(db_column='ADDRESS1', max_length=55)  # Field name made lowercase.
    address2 = models.CharField(db_column='ADDRESS2', max_length=55)  # Field name made lowercase.
    address3 = models.CharField(db_column='ADDRESS3', max_length=55)  # Field name made lowercase.
    address4 = models.CharField(db_column='ADDRESS4', max_length=55)  # Field name made lowercase.
    city = models.CharField(db_column='CITY', max_length=30)  # Field name made lowercase.
    num1 = models.CharField(db_column='NUM1', max_length=6)  # Field name made lowercase.
    num2 = models.CharField(db_column='NUM2', max_length=6)  # Field name made lowercase.
    house_type = models.CharField(db_column='HOUSE_TYPE', max_length=2)  # Field name made lowercase.
    addr_field1 = models.CharField(db_column='ADDR_FIELD1', max_length=2)  # Field name made lowercase.
    addr_field2 = models.CharField(db_column='ADDR_FIELD2', max_length=4)  # Field name made lowercase.
    addr_field3 = models.CharField(db_column='ADDR_FIELD3', max_length=4)  # Field name made lowercase.
    county = models.CharField(db_column='COUNTY', max_length=30)  # Field name made lowercase.
    state = models.CharField(db_column='STATE', max_length=6)  # Field name made lowercase.
    postal = models.CharField(db_column='POSTAL', max_length=12)  # Field name made lowercase.
    geo_code = models.CharField(db_column='GEO_CODE', max_length=11)  # Field name made lowercase.
    in_city_limit = models.CharField(db_column='IN_CITY_LIMIT', max_length=1)  # Field name made lowercase.
    grading_scheme = models.CharField(db_column='GRADING_SCHEME', max_length=3)  # Field name made lowercase.
    grading_basis = models.CharField(db_column='GRADING_BASIS', max_length=3)  # Field name made lowercase.
    grading_basis_sch = models.CharField(db_column='GRADING_BASIS_SCH', max_length=3)  # Field name made lowercase.
    campus = models.CharField(db_column='CAMPUS', max_length=5)  # Field name made lowercase.
    stdnt_spec_perm = models.CharField(db_column='STDNT_SPEC_PERM', max_length=1)  # Field name made lowercase.
    auto_enrl_waitlist = models.CharField(db_column='AUTO_ENRL_WAITLIST', max_length=1)  # Field name made lowercase.
    residency_req = models.CharField(db_column='RESIDENCY_REQ', max_length=1)  # Field name made lowercase.
    fa_wdcan_rsn = models.CharField(db_column='FA_WDCAN_RSN', max_length=3)  # Field name made lowercase.
    enrl_action_reason = models.CharField(db_column='ENRL_ACTION_REASON', max_length=4)  # Field name made lowercase.
    facility_conflict = models.CharField(db_column='FACILITY_CONFLICT', max_length=1)  # Field name made lowercase.
    nslc_agd_rule = models.CharField(db_column='NSLC_AGD_RULE', max_length=1)  # Field name made lowercase.
    nslc_month_factor = models.DecimalField(db_column='NSLC_MONTH_FACTOR', max_digits=38, decimal_places=0)  # Field name made lowercase.
    stdnt_attr_cohort = models.CharField(db_column='STDNT_ATTR_COHORT', max_length=4)  # Field name made lowercase.
    class_mtg_atnd_typ = models.CharField(db_column='CLASS_MTG_ATND_TYP', max_length=4)  # Field name made lowercase.
    fice_cd = models.CharField(db_column='FICE_CD', max_length=6)  # Field name made lowercase.
    load_calc_apply = models.CharField(db_column='LOAD_CALC_APPLY', max_length=1)  # Field name made lowercase.
    fulltime_limit_pct = models.DecimalField(db_column='FULLTIME_LIMIT_PCT', max_digits=5, decimal_places=2)  # Field name made lowercase.
    fulltim_limit_warn = models.DecimalField(db_column='FULLTIM_LIMIT_WARN', max_digits=5, decimal_places=2)  # Field name made lowercase.
    parttime_limit_pct = models.DecimalField(db_column='PARTTIME_LIMIT_PCT', max_digits=5, decimal_places=2)  # Field name made lowercase.
    parttim_limit_warn = models.DecimalField(db_column='PARTTIM_LIMIT_WARN', max_digits=5, decimal_places=2)  # Field name made lowercase.
    assign_type = models.CharField(db_column='ASSIGN_TYPE', max_length=3)  # Field name made lowercase.
    instructor_class = models.CharField(db_column='INSTRUCTOR_CLASS', max_length=6)  # Field name made lowercase.
    crse_cntct_hrs_pct = models.DecimalField(db_column='CRSE_CNTCT_HRS_PCT', max_digits=38, decimal_places=0)  # Field name made lowercase.
    units_acad_prg_pct = models.DecimalField(db_column='UNITS_ACAD_PRG_PCT', max_digits=38, decimal_places=0)  # Field name made lowercase.
    lms_file_type = models.CharField(db_column='LMS_FILE_TYPE', max_length=3)  # Field name made lowercase.
    phone_type = models.CharField(db_column='PHONE_TYPE', max_length=4)  # Field name made lowercase.
    addr_usage = models.CharField(db_column='ADDR_USAGE', max_length=10)  # Field name made lowercase.
    repeat_enrl_ctl = models.CharField(db_column='REPEAT_ENRL_CTL', max_length=1)  # Field name made lowercase.
    repeat_enrl_susp = models.CharField(db_column='REPEAT_ENRL_SUSP', max_length=1)  # Field name made lowercase.
    repeat_grd_ck = models.CharField(db_column='REPEAT_GRD_CK', max_length=1)  # Field name made lowercase.
    repeat_grd_susp = models.CharField(db_column='REPEAT_GRD_SUSP', max_length=1)  # Field name made lowercase.
    grad_name_chg = models.CharField(db_column='GRAD_NAME_CHG', max_length=1)  # Field name made lowercase.
    print_nid = models.CharField(db_column='PRINT_NID', max_length=1)  # Field name made lowercase.
    repeat_chk_topic = models.CharField(db_column='REPEAT_CHK_TOPIC', max_length=1)  # Field name made lowercase.
    scc_aus_dest = models.CharField(db_column='SCC_AUS_DEST', max_length=1)  # Field name made lowercase.
    scc_can_gov_rpt = models.CharField(db_column='SCC_CAN_GOV_RPT', max_length=1)  # Field name made lowercase.
    scc_nzl_enr = models.CharField(db_column='SCC_NZL_ENR', max_length=1)  # Field name made lowercase.
    scc_nzl_nzqa = models.CharField(db_column='SCC_NZL_NZQA', max_length=1)  # Field name made lowercase.
    ssr_use_weeks = models.CharField(db_column='SSR_USE_WEEKS', max_length=1)  # Field name made lowercase.
    ssr_enbl_acad_prog = models.CharField(db_column='SSR_ENBL_ACAD_PROG', max_length=1)  # Field name made lowercase.
    ssr_class_canc_enr = models.CharField(db_column='SSR_CLASS_CANC_ENR', max_length=1)  # Field name made lowercase.
    ssr_class_canc_non = models.CharField(db_column='SSR_CLASS_CANC_NON', max_length=1)  # Field name made lowercase.
    ext_userid_opt = models.CharField(db_column='EXT_USERID_OPT', max_length=1)  # Field name made lowercase.
    lms_provider = models.CharField(db_column='LMS_PROVIDER', max_length=30)  # Field name made lowercase.
    e_addr_type = models.CharField(db_column='E_ADDR_TYPE', max_length=4)  # Field name made lowercase.
    scc_he_used_nld = models.CharField(db_column='SCC_HE_USED_NLD', max_length=1)  # Field name made lowercase.
    ssr_rpt_match_opt = models.CharField(db_column='SSR_RPT_MATCH_OPT', max_length=1)  # Field name made lowercase.
    ssr_rpt_trf_opt = models.CharField(db_column='SSR_RPT_TRF_OPT', max_length=1)  # Field name made lowercase.
    sad_sl_participant = models.CharField(db_column='SAD_SL_PARTICIPANT', max_length=1)  # Field name made lowercase.
    saa_aarpt_type = models.CharField(db_column='SAA_AARPT_TYPE', max_length=5)  # Field name made lowercase.
    saa_plnrrpt_type = models.CharField(db_column='SAA_PLNRRPT_TYPE', max_length=5)  # Field name made lowercase.
    saa_whifrpt_type = models.CharField(db_column='SAA_WHIFRPT_TYPE', max_length=5)  # Field name made lowercase.
    saa_whrpt_typ_prem = models.CharField(db_column='SAA_WHRPT_TYP_PREM', max_length=5)  # Field name made lowercase.
    saa_whrpt_typ_advr = models.CharField(db_column='SAA_WHRPT_TYP_ADVR', max_length=5)  # Field name made lowercase.
    saa_whifxfr_type = models.CharField(db_column='SAA_WHIFXFR_TYPE', max_length=5)  # Field name made lowercase.
    saa_whxfr_typ_prem = models.CharField(db_column='SAA_WHXFR_TYP_PREM', max_length=5)  # Field name made lowercase.
    ssr_rpt_date_enrl = models.CharField(db_column='SSR_RPT_DATE_ENRL', max_length=1)  # Field name made lowercase.
    ssr_rpt_date_proc = models.CharField(db_column='SSR_RPT_DATE_PROC', max_length=1)  # Field name made lowercase.
    sad_uc_hesa_ucas = models.CharField(db_column='SAD_UC_HESA_UCAS', max_length=1)  # Field name made lowercase.
    sad_pb_pbi = models.CharField(db_column='SAD_PB_PBI', max_length=1)  # Field name made lowercase.
    ssr_grad_chrg_fee = models.CharField(db_column='SSR_GRAD_CHRG_FEE', max_length=1)  # Field name made lowercase.
    ssr_grad_elig_only = models.CharField(db_column='SSR_GRAD_ELIG_ONLY', max_length=1)  # Field name made lowercase.
    ssr_grad_pay_req = models.CharField(db_column='SSR_GRAD_PAY_REQ', max_length=1)  # Field name made lowercase.
    fee_code = models.CharField(db_column='FEE_CODE', max_length=6)  # Field name made lowercase.
    prog_reason = models.CharField(db_column='PROG_REASON', max_length=4)  # Field name made lowercase.
    ssr_use_grad_track = models.CharField(db_column='SSR_USE_GRAD_TRACK', max_length=1)  # Field name made lowercase.
    ssr_grad_alwadupd = models.CharField(db_column='SSR_GRAD_ALWADUPD', max_length=1)  # Field name made lowercase.
    ssr_grad_alwnmupd = models.CharField(db_column='SSR_GRAD_ALWNMUPD', max_length=1)  # Field name made lowercase.
    ssr_grad_status = models.CharField(db_column='SSR_GRAD_STATUS', max_length=4)  # Field name made lowercase.
    ssr_grad_show_honr = models.CharField(db_column='SSR_GRAD_SHOW_HONR', max_length=1)  # Field name made lowercase.
    ssr_grad_show_mlst = models.CharField(db_column='SSR_GRAD_SHOW_MLST', max_length=1)  # Field name made lowercase.
    ssr_grad_show_note = models.CharField(db_column='SSR_GRAD_SHOW_NOTE', max_length=1)  # Field name made lowercase.
    ssr_grad_show_otcr = models.CharField(db_column='SSR_GRAD_SHOW_OTCR', max_length=1)  # Field name made lowercase.
    ssr_grad_show_sgpa = models.CharField(db_column='SSR_GRAD_SHOW_SGPA', max_length=1)  # Field name made lowercase.
    ssr_grad_show_stat = models.CharField(db_column='SSR_GRAD_SHOW_STAT', max_length=1)  # Field name made lowercase.
    ssr_grad_show_trcr = models.CharField(db_column='SSR_GRAD_SHOW_TRCR', max_length=1)  # Field name made lowercase.
    ssr_grad_show_tscr = models.CharField(db_column='SSR_GRAD_SHOW_TSCR', max_length=1)  # Field name made lowercase.
    ssr_grad_updmsg = models.CharField(db_column='SSR_GRAD_UPDMSG', max_length=254)  # Field name made lowercase.
    ssr_grad_updname = models.CharField(db_column='SSR_GRAD_UPDNAME', max_length=1)  # Field name made lowercase.
    ssr_grad_name_lbl = models.CharField(db_column='SSR_GRAD_NAME_LBL', max_length=30)  # Field name made lowercase.
    ssr_grad_ndt = models.CharField(db_column='SSR_GRAD_NDT', max_length=30)  # Field name made lowercase.
    ssr_grad_name_type = models.CharField(db_column='SSR_GRAD_NAME_TYPE', max_length=3)  # Field name made lowercase.
    ssr_grad_updaddr = models.CharField(db_column='SSR_GRAD_UPDADDR', max_length=1)  # Field name made lowercase.
    ssr_grad_addr_lbl = models.CharField(db_column='SSR_GRAD_ADDR_LBL', max_length=30)  # Field name made lowercase.
    ssr_grad_addrusage = models.CharField(db_column='SSR_GRAD_ADDRUSAGE', max_length=10)  # Field name made lowercase.
    ssr_grad_stat_ag = models.CharField(db_column='SSR_GRAD_STAT_AG', max_length=50)  # Field name made lowercase.
    ssr_grad_stat_ap = models.CharField(db_column='SSR_GRAD_STAT_AP', max_length=50)  # Field name made lowercase.
    ssr_grad_stat_aw = models.CharField(db_column='SSR_GRAD_STAT_AW', max_length=50)  # Field name made lowercase.
    ssr_grad_stat_dn = models.CharField(db_column='SSR_GRAD_STAT_DN', max_length=50)  # Field name made lowercase.
    ssr_grad_stat_eg = models.CharField(db_column='SSR_GRAD_STAT_EG', max_length=50)  # Field name made lowercase.
    ssr_grad_stat_ir = models.CharField(db_column='SSR_GRAD_STAT_IR', max_length=50)  # Field name made lowercase.
    ssr_grad_stat_pn = models.CharField(db_column='SSR_GRAD_STAT_PN', max_length=50)  # Field name made lowercase.
    ssr_grad_stat_wd = models.CharField(db_column='SSR_GRAD_STAT_WD', max_length=50)  # Field name made lowercase.
    ssr_apt_lvl = models.CharField(db_column='SSR_APT_LVL', max_length=1)  # Field name made lowercase.
    sad_br_use_nld = models.CharField(db_column='SAD_BR_USE_NLD', max_length=1)  # Field name made lowercase.
    ssr_enrl_crs_mlstn = models.CharField(db_column='SSR_ENRL_CRS_MLSTN', max_length=1)  # Field name made lowercase.
    ssr_am_enable = models.CharField(db_column='SSR_AM_ENABLE', max_length=1)  # Field name made lowercase.
    ssr_acm_defactv = models.CharField(db_column='SSR_ACM_DEFACTV', max_length=1)  # Field name made lowercase.
    ssr_ac_dflt_lvl = models.CharField(db_column='SSR_AC_DFLT_LVL', max_length=1)  # Field name made lowercase.
    ssr_bron_ho_nld = models.CharField(db_column='SSR_BRON_HO_NLD', max_length=1)  # Field name made lowercase.
    ssr_rslt_type = models.CharField(db_column='SSR_RSLT_TYPE', max_length=20)  # Field name made lowercase.
    ssr_iam_enevnt_opt = models.CharField(db_column='SSR_IAM_ENEVNT_OPT', max_length=1)  # Field name made lowercase.
    ssr_iam_btcrte_opt = models.CharField(db_column='SSR_IAM_BTCRTE_OPT', max_length=1)  # Field name made lowercase.
    ssr_use_shift = models.CharField(db_column='SSR_USE_SHIFT', max_length=1)  # Field name made lowercase.
    ssr_use_shift_term = models.CharField(db_column='SSR_USE_SHIFT_TERM', max_length=1)  # Field name made lowercase.
    ssr_acwc_calc = models.CharField(db_column='SSR_ACWC_CALC', max_length=1)  # Field name made lowercase.
    ssr_acwc_asgn = models.CharField(db_column='SSR_ACWC_ASGN', max_length=1)  # Field name made lowercase.
    ssr_iam_rslt_post = models.CharField(db_column='SSR_IAM_RSLT_POST', max_length=1)  # Field name made lowercase.
    ssr_stenrl_grd_exs = models.CharField(db_column='SSR_STENRL_GRD_EXS', max_length=1)  # Field name made lowercase.
    saa_acd_prg_sm_fl = models.CharField(db_column='SAA_ACD_PRG_SM_FL', max_length=5)  # Field name made lowercase.
    saa_acad_prog_fl = models.CharField(db_column='SAA_ACAD_PROG_FL', max_length=5)  # Field name made lowercase.
    saa_crs_req_alt_fl = models.CharField(db_column='SAA_CRS_REQ_ALT_FL', max_length=5)  # Field name made lowercase.
    saa_max_gpa_fl = models.DecimalField(db_column='SAA_MAX_GPA_FL', max_digits=3, decimal_places=1)  # Field name made lowercase.
    saa_base_chart_fl = models.CharField(db_column='SAA_BASE_CHART_FL', max_length=1)  # Field name made lowercase.
    saa_crse_weight_fl = models.DecimalField(db_column='SAA_CRSE_WEIGHT_FL', max_digits=6, decimal_places=3)  # Field name made lowercase.
    ssr_iam_nonupd_opt = models.CharField(db_column='SSR_IAM_NONUPD_OPT', max_length=1)  # Field name made lowercase.
    ssr_iam_nondel_opt = models.CharField(db_column='SSR_IAM_NONDEL_OPT', max_length=1)  # Field name made lowercase.
    ssr_iam_penupd_opt = models.CharField(db_column='SSR_IAM_PENUPD_OPT', max_length=1)  # Field name made lowercase.
    ssr_iam_pendel_opt = models.CharField(db_column='SSR_IAM_PENDEL_OPT', max_length=1)  # Field name made lowercase.
    ssr_iam_rstupd_opt = models.CharField(db_column='SSR_IAM_RSTUPD_OPT', max_length=1)  # Field name made lowercase.
    ssr_iam_rstdel_opt = models.CharField(db_column='SSR_IAM_RSTDEL_OPT', max_length=1)  # Field name made lowercase.
    ssr_iam_calupd_opt = models.CharField(db_column='SSR_IAM_CALUPD_OPT', max_length=1)  # Field name made lowercase.
    ssr_iam_caldel_opt = models.CharField(db_column='SSR_IAM_CALDEL_OPT', max_length=1)  # Field name made lowercase.
    ssr_blind_graded = models.CharField(db_column='SSR_BLIND_GRADED', max_length=1)  # Field name made lowercase.
    ssr_anid_arr_def = models.CharField(db_column='SSR_ANID_ARR_DEF', max_length=4)  # Field name made lowercase.
    ssr_anid_wkc_def = models.CharField(db_column='SSR_ANID_WKC_DEF', max_length=4)  # Field name made lowercase.
    ssr_anid_iam_def = models.CharField(db_column='SSR_ANID_IAM_DEF', max_length=4)  # Field name made lowercase.
    ssr_iam_pe_postopt = models.CharField(db_column='SSR_IAM_PE_POSTOPT', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PS_INSTITUTION_TBL'
        unique_together = (('institution', 'effdt'),)


class PsSaTcmpRelTbl(models.Model):
    test_id = models.CharField(db_column='TEST_ID', max_length=11)  # Field name made lowercase.
    effdt = models.DateTimeField(db_column='EFFDT')  # Field name made lowercase.
    test_component = models.CharField(db_column='TEST_COMPONENT', max_length=5)  # Field name made lowercase.
    descr = models.CharField(db_column='DESCR', max_length=30)  # Field name made lowercase.
    descrshort = models.CharField(db_column='DESCRSHORT', max_length=10)  # Field name made lowercase.
    max_score = models.DecimalField(db_column='MAX_SCORE', max_digits=6, decimal_places=2)  # Field name made lowercase.
    min_score = models.DecimalField(db_column='MIN_SCORE', max_digits=6, decimal_places=2)  # Field name made lowercase.
    edi_speede_tst_cd = models.CharField(db_column='EDI_SPEEDE_TST_CD', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PS_SA_TCMP_REL_TBL'
        unique_together = (('test_id', 'effdt', 'test_component'),)


class PsSaTestTbl(models.Model):
    test_id = models.CharField(db_column='TEST_ID', max_length=11)  # Field name made lowercase.
    effdt = models.DateTimeField(db_column='EFFDT')  # Field name made lowercase.
    eff_status = models.CharField(db_column='EFF_STATUS', max_length=1)  # Field name made lowercase.
    descr = models.CharField(db_column='DESCR', max_length=30)  # Field name made lowercase.
    descrshort = models.CharField(db_column='DESCRSHORT', max_length=10)  # Field name made lowercase.
    testing_agency = models.CharField(db_column='TESTING_AGENCY', max_length=3)  # Field name made lowercase.
    scc_entity_id = models.CharField(db_column='SCC_ENTITY_ID', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PS_SA_TEST_TBL'
        unique_together = (('test_id', 'effdt'),)


class PsTermValTbl(models.Model):
    strm = models.CharField(db_column='STRM', unique=True, max_length=4)  # Field name made lowercase.
    descr = models.CharField(db_column='DESCR', max_length=30)  # Field name made lowercase.
    descrshort = models.CharField(db_column='DESCRSHORT', max_length=10)  # Field name made lowercase.
    next_class_no = models.IntegerField(db_column='NEXT_CLASS_NO')  # Field name made lowercase.
    ssr_sscls_std_bdt = models.DateTimeField(db_column='SSR_SSCLS_STD_BDT')  # Field name made lowercase.
    ssr_sscls_std_edt = models.DateTimeField(db_column='SSR_SSCLS_STD_EDT')  # Field name made lowercase.
    ssr_sscls_insr_bdt = models.DateTimeField(db_column='SSR_SSCLS_INSR_BDT')  # Field name made lowercase.
    ssr_sscls_insr_edt = models.DateTimeField(db_column='SSR_SSCLS_INSR_EDT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PS_TERM_VAL_TBL'


class PsTrnsfrComp(models.Model):
    institution = models.CharField(db_column='INSTITUTION', max_length=5)  # Field name made lowercase.
    trnsfr_src_id = models.CharField(db_column='TRNSFR_SRC_ID', max_length=11)  # Field name made lowercase.
    comp_subject_area = models.CharField(db_column='COMP_SUBJECT_AREA', max_length=16)  # Field name made lowercase.
    effdt = models.DateTimeField(db_column='EFFDT')  # Field name made lowercase.
    trnsfr_eqvlncy_cmp = models.CharField(db_column='TRNSFR_EQVLNCY_CMP', max_length=4)  # Field name made lowercase.
    descr = models.CharField(db_column='DESCR', max_length=30)  # Field name made lowercase.
    ext_term_type = models.CharField(db_column='EXT_TERM_TYPE', max_length=4)  # Field name made lowercase.
    trnsfr_crse_fl = models.CharField(db_column='TRNSFR_CRSE_FL', max_length=1)  # Field name made lowercase.
    trnsfr_priority = models.DecimalField(db_column='TRNSFR_PRIORITY', max_digits=38, decimal_places=0)  # Field name made lowercase.
    cntngnt_crdt_fl = models.CharField(db_column='CNTNGNT_CRDT_FL', max_length=1)  # Field name made lowercase.
    inp_crse_cnt = models.DecimalField(db_column='INP_CRSE_CNT', max_digits=38, decimal_places=0)  # Field name made lowercase.
    unt_trnsfr_src = models.CharField(db_column='UNT_TRNSFR_SRC', max_length=1)  # Field name made lowercase.
    xs_crse_fl = models.CharField(db_column='XS_CRSE_FL', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PS_TRNSFR_COMP'
        unique_together = (('institution', 'trnsfr_src_id', 'comp_subject_area', 'effdt', 'trnsfr_eqvlncy_cmp'),)


class PsTrnsfrFrom(models.Model):
    institution = models.CharField(db_column='INSTITUTION', max_length=5)  # Field name made lowercase.
    trnsfr_src_id = models.CharField(db_column='TRNSFR_SRC_ID', max_length=11)  # Field name made lowercase.
    comp_subject_area = models.CharField(db_column='COMP_SUBJECT_AREA', max_length=16)  # Field name made lowercase.
    effdt = models.DateTimeField(db_column='EFFDT')  # Field name made lowercase.
    trnsfr_eqvlncy_cmp = models.CharField(db_column='TRNSFR_EQVLNCY_CMP', max_length=4)  # Field name made lowercase.
    trnsfr_cmp_seq = models.DecimalField(db_column='TRNSFR_CMP_SEQ', max_digits=38, decimal_places=0)  # Field name made lowercase.
    wildcard_ind = models.CharField(db_column='WILDCARD_IND', max_length=1)  # Field name made lowercase.
    school_subject = models.CharField(db_column='SCHOOL_SUBJECT', max_length=8)  # Field name made lowercase.
    school_crse_nbr = models.CharField(db_column='SCHOOL_CRSE_NBR', max_length=10)  # Field name made lowercase.
    crse_id = models.CharField(db_column='CRSE_ID', max_length=6)  # Field name made lowercase.
    crse_offer_nbr = models.DecimalField(db_column='CRSE_OFFER_NBR', max_digits=38, decimal_places=0)  # Field name made lowercase.
    units_minimum = models.DecimalField(db_column='UNITS_MINIMUM', max_digits=5, decimal_places=2)  # Field name made lowercase.
    units_maximum = models.DecimalField(db_column='UNITS_MAXIMUM', max_digits=5, decimal_places=2)  # Field name made lowercase.
    grade_pts_min = models.DecimalField(db_column='GRADE_PTS_MIN', max_digits=9, decimal_places=3)  # Field name made lowercase.
    grade_pts_max = models.DecimalField(db_column='GRADE_PTS_MAX', max_digits=9, decimal_places=3)  # Field name made lowercase.
    ssr_max_age = models.DecimalField(db_column='SSR_MAX_AGE', max_digits=38, decimal_places=0)  # Field name made lowercase.
    begin_dt = models.DateTimeField(db_column='BEGIN_DT')  # Field name made lowercase.
    end_dt = models.DateTimeField(db_column='END_DT')  # Field name made lowercase.
    trnsfr_grade_fl = models.CharField(db_column='TRNSFR_GRADE_FL', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PS_TRNSFR_FROM'
        unique_together = (('institution', 'trnsfr_src_id', 'comp_subject_area', 'effdt', 'trnsfr_eqvlncy_cmp', 'trnsfr_cmp_seq'),)


class PsTrnsfrSubj(models.Model):
    institution = models.CharField(db_column='INSTITUTION', max_length=5)  # Field name made lowercase.
    trnsfr_src_id = models.CharField(db_column='TRNSFR_SRC_ID', max_length=11)  # Field name made lowercase.
    comp_subject_area = models.CharField(db_column='COMP_SUBJECT_AREA', max_length=16)  # Field name made lowercase.
    effdt = models.DateTimeField(db_column='EFFDT')  # Field name made lowercase.
    eff_status = models.CharField(db_column='EFF_STATUS', max_length=1)  # Field name made lowercase.
    descr = models.CharField(db_column='DESCR', max_length=30)  # Field name made lowercase.
    tc_catlg_org_type = models.CharField(db_column='TC_CATLG_ORG_TYPE', max_length=1)  # Field name made lowercase.
    catalog_org = models.CharField(db_column='CATALOG_ORG', max_length=11)  # Field name made lowercase.
    trnsfr_grade_fl = models.CharField(db_column='TRNSFR_GRADE_FL', max_length=1)  # Field name made lowercase.
    ext_term_type = models.CharField(db_column='EXT_TERM_TYPE', max_length=4)  # Field name made lowercase.
    grade_pts_min = models.DecimalField(db_column='GRADE_PTS_MIN', max_digits=9, decimal_places=3)  # Field name made lowercase.
    grade_pts_max = models.DecimalField(db_column='GRADE_PTS_MAX', max_digits=9, decimal_places=3)  # Field name made lowercase.
    units_minimum = models.DecimalField(db_column='UNITS_MINIMUM', max_digits=5, decimal_places=2)  # Field name made lowercase.
    units_maximum = models.DecimalField(db_column='UNITS_MAXIMUM', max_digits=5, decimal_places=2)  # Field name made lowercase.
    unt_trnsfr_src = models.CharField(db_column='UNT_TRNSFR_SRC', max_length=1)  # Field name made lowercase.
    crse_id = models.CharField(db_column='CRSE_ID', max_length=6)  # Field name made lowercase.
    rqmnt_designtn = models.CharField(db_column='RQMNT_DESIGNTN', max_length=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PS_TRNSFR_SUBJ'
        unique_together = (('institution', 'trnsfr_src_id', 'comp_subject_area', 'effdt'),)


class PsTrnsfrTo(models.Model):
    institution = models.CharField(db_column='INSTITUTION', max_length=5)  # Field name made lowercase.
    trnsfr_src_id = models.CharField(db_column='TRNSFR_SRC_ID', max_length=11)  # Field name made lowercase.
    comp_subject_area = models.CharField(db_column='COMP_SUBJECT_AREA', max_length=16)  # Field name made lowercase.
    effdt = models.DateTimeField(db_column='EFFDT')  # Field name made lowercase.
    trnsfr_eqvlncy_cmp = models.CharField(db_column='TRNSFR_EQVLNCY_CMP', max_length=4)  # Field name made lowercase.
    crse_id = models.CharField(db_column='CRSE_ID', max_length=6)  # Field name made lowercase.
    crse_offer_nbr = models.DecimalField(db_column='CRSE_OFFER_NBR', max_digits=38, decimal_places=0)  # Field name made lowercase.
    unt_taken = models.DecimalField(db_column='UNT_TAKEN', max_digits=5, decimal_places=2)  # Field name made lowercase.
    ssr_tr_def_grd_typ = models.CharField(db_column='SSR_TR_DEF_GRD_TYP', max_length=1)  # Field name made lowercase.
    ssr_tr_def_grd_seq = models.CharField(db_column='SSR_TR_DEF_GRD_SEQ', max_length=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PS_TRNSFR_TO'
        unique_together = (('institution', 'trnsfr_src_id', 'comp_subject_area', 'effdt', 'trnsfr_eqvlncy_cmp', 'crse_id'),)


class PsTstCreditComp(models.Model):
    institution = models.CharField(db_column='INSTITUTION', max_length=5)  # Field name made lowercase.
    tst_eqvlncy = models.CharField(db_column='TST_EQVLNCY', max_length=6)  # Field name made lowercase.
    effdt = models.DateTimeField(db_column='EFFDT')  # Field name made lowercase.
    test_id = models.CharField(db_column='TEST_ID', max_length=11)  # Field name made lowercase.
    test_component = models.CharField(db_column='TEST_COMPONENT', max_length=5)  # Field name made lowercase.
    trnsfr_eqvlncy_cmp = models.CharField(db_column='TRNSFR_EQVLNCY_CMP', max_length=4)  # Field name made lowercase.
    descr = models.CharField(db_column='DESCR', max_length=30)  # Field name made lowercase.
    trnsfr_priority = models.DecimalField(db_column='TRNSFR_PRIORITY', max_digits=38, decimal_places=0)  # Field name made lowercase.
    min_score = models.DecimalField(db_column='MIN_SCORE', max_digits=6, decimal_places=2)  # Field name made lowercase.
    max_score = models.DecimalField(db_column='MAX_SCORE', max_digits=6, decimal_places=2)  # Field name made lowercase.
    percentile = models.DecimalField(db_column='PERCENTILE', max_digits=38, decimal_places=0)  # Field name made lowercase.
    begin_dt = models.DateTimeField(db_column='BEGIN_DT', blank=True, null=True)  # Field name made lowercase.
    end_dt = models.DateTimeField(db_column='END_DT', blank=True, null=True)  # Field name made lowercase.
    ssr_max_age = models.DecimalField(db_column='SSR_MAX_AGE', max_digits=38, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PS_TST_CREDIT_COMP'
        unique_together = (('institution', 'tst_eqvlncy', 'effdt', 'test_id', 'test_component', 'trnsfr_eqvlncy_cmp'),)


class PsTstCreditCrse(models.Model):
    institution = models.CharField(db_column='INSTITUTION', max_length=5)  # Field name made lowercase.
    tst_eqvlncy = models.CharField(db_column='TST_EQVLNCY', max_length=6)  # Field name made lowercase.
    effdt = models.DateTimeField(db_column='EFFDT')  # Field name made lowercase.
    test_id = models.CharField(db_column='TEST_ID', max_length=11)  # Field name made lowercase.
    test_component = models.CharField(db_column='TEST_COMPONENT', max_length=5)  # Field name made lowercase.
    trnsfr_eqvlncy_cmp = models.CharField(db_column='TRNSFR_EQVLNCY_CMP', max_length=4)  # Field name made lowercase.
    crse_id = models.CharField(db_column='CRSE_ID', max_length=6)  # Field name made lowercase.
    crse_offer_nbr = models.DecimalField(db_column='CRSE_OFFER_NBR', max_digits=38, decimal_places=0)  # Field name made lowercase.
    unt_taken = models.DecimalField(db_column='UNT_TAKEN', max_digits=5, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PS_TST_CREDIT_CRSE'
        unique_together = (('institution', 'tst_eqvlncy', 'effdt', 'test_id', 'test_component', 'trnsfr_eqvlncy_cmp', 'crse_id'),)


class DjangoContentType(models.Model):
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Tirsttable(models.Model):
    bubu = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tirsttable'
