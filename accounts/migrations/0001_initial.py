# Generated by Django 2.1.7 on 2019-04-20 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=128)),
                ('dob', models.DateField(max_length=8)),
                ('age', models.IntegerField()),
                ('phone', models.CharField(max_length=12)),
                ('Email', models.EmailField(blank=True, max_length=70)),
                ('Speciality', models.CharField(choices=[('dermetalogy', 'dermetalogy'), ('Cardiology', 'Cardiology'), ('ENT', 'ENT'), ('oncology', 'oncology'), ('neurology', 'neurology'), ('pediatrics', 'pediatrics'), ('gynecology', 'gynecology')], max_length=128)),
            ],
        ),
    ]
