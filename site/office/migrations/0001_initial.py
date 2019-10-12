# Generated by Django 2.2.6 on 2019-10-10 01:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="OfficeDay",
            fields=[
                ("uuid", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("month", models.IntegerField()),
                ("day", models.IntegerField()),
                ("holy_day", models.CharField(blank=True, max_length=255, null=True)),
                ("mp_psalms", models.CharField(max_length=255)),
                ("mp_psalms_text", models.TextField(blank=True, null=True)),
                ("mp_reading_1", models.CharField(max_length=255)),
                ("mp_reading_1_text", models.TextField(blank=True, null=True)),
                ("mp_reading_1_abbreviated", models.CharField(blank=True, max_length=255, null=True)),
                ("mp_reading_1_abbreviated_text", models.TextField(blank=True, null=True)),
                ("mp_reading_2", models.CharField(max_length=255)),
                ("mp_reading_2_text", models.TextField(blank=True, null=True)),
                ("ep_psalms", models.CharField(max_length=255)),
                ("ep_psalms_text", models.TextField(blank=True, null=True)),
                ("ep_reading_1", models.CharField(max_length=255)),
                ("ep_reading_1_text", models.TextField(blank=True, null=True)),
                ("ep_reading_1_abbreviated", models.CharField(blank=True, max_length=255, null=True)),
                ("ep_reading_1_abbreviated_text", models.TextField(blank=True, null=True)),
                ("ep_reading_2", models.CharField(max_length=255)),
                ("ep_reading_2_text", models.TextField(blank=True, null=True)),
            ],
            options={"abstract": False},
        )
    ]
