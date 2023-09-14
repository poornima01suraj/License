# Generated by Django 4.2.4 on 2023-08-04 08:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("project_b", "0006_alter_license_validity_months"),
    ]

    operations = [
        migrations.AlterField(
            model_name="license",
            name="validity_months",
            field=models.PositiveIntegerField(
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(12),
                ]
            ),
        ),
    ]
