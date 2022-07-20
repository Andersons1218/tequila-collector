# Generated by Django 4.0.6 on 2022-07-20 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_rims_date_alter_rims_rim'),
    ]

    operations = [
        migrations.CreateModel(
            name='Taste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='drinking time')),
                ('rims', models.CharField(choices=[('S', 'Salt'), ('SG', 'Sugar'), ('NO', 'No Rim')], default='S', max_length=2)),
                ('tequila', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.tequila')),
            ],
        ),
        migrations.DeleteModel(
            name='Rims',
        ),
    ]
