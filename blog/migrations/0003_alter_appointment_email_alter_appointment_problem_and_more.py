# Generated by Django 4.2.4 on 2023-09-03 15:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_appointment_alter_post_content_alter_post_publish_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointment",
            name="email",
            field=models.EmailField(max_length=50, verbose_name="Email address"),
        ),
        migrations.AlterField(
            model_name="appointment",
            name="problem",
            field=models.TextField(max_length=500, verbose_name="Problem text"),
        ),
        migrations.AlterField(
            model_name="review",
            name="content",
            field=models.TextField(max_length=3000, verbose_name="Review text"),
        ),
    ]
