# Generated by Django 5.0.6 on 2024-07-02 22:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0008_plan_subscription"),
    ]

    operations = [
        migrations.AddField(
            model_name="subscription",
            name="amount_due",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name="subscription",
            name="amount_paid",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name="subscription",
            name="is_paid",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="subscription",
            name="last_billed",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]