# Generated by Django 5.1 on 2024-08-16 16:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("emp_app", "0002_rename_employess_employes"),
    ]

    operations = [
        migrations.AddField(
            model_name="employes",
            name="phone",
            field=models.IntegerField(default=0),
        ),
    ]
