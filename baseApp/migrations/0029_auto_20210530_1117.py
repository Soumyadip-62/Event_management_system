# Generated by Django 3.1.6 on 2021-05-30 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0028_packagemanagement_event_decor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packagemanagement',
            name='event_decor',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='baseApp.decorator'),
        ),
    ]