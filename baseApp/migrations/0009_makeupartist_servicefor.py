# Generated by Django 3.1.7 on 2021-05-15 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0008_delete_servicefor'),
    ]

    operations = [
        migrations.AddField(
            model_name='makeupartist',
            name='servicefor',
            field=models.CharField(blank=True, choices=[('MAKEUP ARTIST', 'MAKEUP ARTIST'), ('CATERING SERVICES', 'CATERING SERVICES'), ('VENUE', 'VENUE')], default='MAKEUP ARTIST', max_length=30),
        ),
    ]
