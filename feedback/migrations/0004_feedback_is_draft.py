# Generated by Django 4.0.3 on 2022-04-30 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0003_feedback_date_submitted_feedback_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='is_draft',
            field=models.BooleanField(default=False),
        ),
    ]