# Generated by Django 4.1.5 on 2023-01-10 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="dishes_info",
            field=models.CharField(max_length=3000, null=True),
        ),
    ]
