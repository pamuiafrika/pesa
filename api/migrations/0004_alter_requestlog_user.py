# Generated by Django 5.0.6 on 2024-07-02 13:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0003_requestlog"),
    ]

    operations = [
        migrations.AlterField(
            model_name="requestlog",
            name="user",
            field=models.CharField(max_length=100),
        ),
    ]
