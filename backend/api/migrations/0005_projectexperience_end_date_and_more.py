# Generated by Django 5.1.6 on 2025-06-02 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_educationexperience_bullet_points_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectexperience',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectexperience',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
