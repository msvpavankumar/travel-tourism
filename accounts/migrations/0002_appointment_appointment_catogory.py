# Generated by Django 2.1.7 on 2020-04-11 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='Appointment_catogory',
            field=models.CharField(choices=[('first', 'First Visit'), ('follow_up', 'Follow up')], default='first', max_length=128),
        ),
    ]
