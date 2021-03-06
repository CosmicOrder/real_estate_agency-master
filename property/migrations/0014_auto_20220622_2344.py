# Generated by Django 2.2.24 on 2022-06-22 20:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20220622_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='flat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complaint', to='property.Flat', verbose_name='Квартира на которую пожаловались'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='who_complaint',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complaint', to=settings.AUTH_USER_MODEL, verbose_name='Кто жаловался'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='liked_by',
            field=models.ManyToManyField(blank=True, related_name='liked_by', to=settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='new_building',
            field=models.BooleanField(db_index=True, null=True),
        ),
    ]
