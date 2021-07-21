# Generated by Django 3.1.7 on 2021-05-16 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0021_auto_20210516_2247'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnniSpecial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrengement_name', models.CharField(blank=True, choices=[('Anniversary special decor', 'decor'), ('Anniversary special dinner', 'dinner'), ('Anniversary special Floatel party', 'Floatel party')], max_length=100)),
                ('organizer', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
                ('package', models.CharField(max_length=30)),
                ('desc', models.CharField(blank=True, max_length=500)),
                ('log', models.DateTimeField(auto_now_add=True)),
                ('picture', models.ImageField(blank=True, upload_to='Ani')),
                ('servicefor', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='baseApp.servicefor')),
            ],
        ),
    ]