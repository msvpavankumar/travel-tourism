# Generated by Django 2.1.7 on 2020-04-14 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_appointment_appointment_catogory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctors', models.CharField(max_length=50)),
            ],
        ),
    ]
