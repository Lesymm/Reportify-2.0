# Generated by Django 4.2.10 on 2024-03-22 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_report_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='notes',
            field=models.TextField(blank=True, default='', verbose_name='Administrator Notes'),
        ),
    ]