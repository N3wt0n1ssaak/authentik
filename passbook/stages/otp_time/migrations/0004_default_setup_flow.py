# Generated by Django 3.1.1 on 2020-09-25 15:36

from django.apps.registry import Apps
from django.db import migrations
from django.db.backends.base.schema import BaseDatabaseSchemaEditor

from passbook.flows.models import FlowDesignation
from passbook.stages.otp_time.models import TOTPDigits


def create_default_setup_flow(apps: Apps, schema_editor: BaseDatabaseSchemaEditor):
    Flow = apps.get_model("passbook_flows", "Flow")
    FlowStageBinding = apps.get_model("passbook_flows", "FlowStageBinding")

    OTPTimeStage = apps.get_model("passbook_stages_otp_time", "OTPTimeStage")

    db_alias = schema_editor.connection.alias

    flow, _ = Flow.objects.using(db_alias).update_or_create(
        slug="default-otp-time-configure",
        designation=FlowDesignation.STAGE_CONFIGURATION,
        defaults={"name": "Setup Two-Factor authentication"},
    )

    stage, _ = OTPTimeStage.objects.using(db_alias).update_or_create(
        name="default-otp-time-configure", defaults={"digits": TOTPDigits.SIX}
    )

    FlowStageBinding.objects.using(db_alias).update_or_create(
        target=flow, stage=stage, defaults={"order": 0}
    )


class Migration(migrations.Migration):

    dependencies = [
        ("passbook_stages_otp_time", "0003_otptimestage_configure_flow"),
    ]

    operations = [
        migrations.RunPython(create_default_setup_flow),
    ]
