# Generated by Django 4.2.4 on 2023-08-04 05:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("project_b", "0002_alter_license_validity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="license",
            name="server_ip",
            field=models.CharField(max_length=100),
        ),
    ]