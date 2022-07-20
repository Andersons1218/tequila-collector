# Generated by Django 4.0.6 on 2022-07-20 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rims',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('rim', models.CharField(choices=[('S', 'Salt'), ('SG', 'Sugar'), ('NO', 'No Rim')], default='S', max_length=1)),
            ],
        ),
    ]
