# Generated by Django 4.0 on 2021-12-29 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0003_alter_siteaccess_unique_together_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='last_verified',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]