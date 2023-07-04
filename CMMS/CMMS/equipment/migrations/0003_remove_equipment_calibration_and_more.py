# Generated by Django 4.1.3 on 2023-04-09 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0002_rename_type_equipment_caltype_weeklymonitor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipment',
            name='calibration',
        ),
        migrations.AddField(
            model_name='calibration',
            name='equipment_id',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, to='equipment.equipment'),
            preserve_default=False,
        ),
    ]