# Generated by Django 3.1.7 on 2021-05-07 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CateringService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=50)),
                ('cat_type', models.CharField(blank=True, choices=[('', ''), ('Veg', 'Veg'), ('Non-Veg', 'Non Veg'), ('Pure Veg', 'Pure Veg')], max_length=30)),
                ('cat_phone', models.CharField(max_length=30)),
                ('cat_location', models.CharField(max_length=30)),
                ('cat_office', models.CharField(blank=True, max_length=30)),
                ('rate', models.CharField(max_length=30)),
                ('cat_desc', models.CharField(blank=True, max_length=300)),
                ('cat_log', models.DateTimeField(auto_now_add=True)),
                ('cat_picture', models.ImageField(blank=True, upload_to='Catering')),
            ],
        ),
        migrations.CreateModel(
            name='MakeupArtist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mua_name', models.CharField(max_length=50)),
                ('mua_phone', models.CharField(max_length=30)),
                ('mua_location', models.CharField(max_length=30)),
                ('mua_office', models.CharField(blank=True, max_length=30)),
                ('package', models.CharField(max_length=30)),
                ('specification', models.CharField(blank=True, choices=[('', ''), ('MAC', 'MAC'), ('Noramal', 'Noramal')], max_length=30)),
                ('mu_desc', models.CharField(blank=True, max_length=300)),
                ('mua_log', models.DateTimeField(auto_now_add=True)),
                ('picture', models.ImageField(blank=True, upload_to='MUAs')),
            ],
        ),
        migrations.CreateModel(
            name='MakeupType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
                ('type_desc', models.CharField(blank=True, max_length=300)),
                ('mtype_log', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.AddField(
            model_name='makeupartist',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baseApp.makeuptype'),
        ),
    ]