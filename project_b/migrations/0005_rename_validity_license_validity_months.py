# Generated by Django 4.2.4 on 2023-08-04 06:35

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("project_b", "0004_alter_license_validity"),
    ]

    operations = [
        migrations.RenameField(
            model_name="license",
            old_name="validity",
            new_name="validity_months",
        ),
    ]