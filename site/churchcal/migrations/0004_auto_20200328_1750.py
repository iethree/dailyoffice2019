# Generated by Django 2.2.8 on 2020-03-28 21:50

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [("churchcal", "0003_massreading")]

    operations = [
        migrations.CreateModel(
            name="Common",
            fields=[
                ("uuid", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("abbreviation", models.CharField(max_length=256)),
                ("name", models.CharField(max_length=256)),
                ("collect", models.TextField(blank=True, null=True)),
                ("alternate_collect", models.TextField(blank=True, null=True)),
                ("calendar", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="churchcal.Calendar")),
            ],
            options={"abstract": False},
        ),
        migrations.AddField(
            model_name="massreading",
            name="common",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="churchcal.Common"
            ),
        ),
    ]
