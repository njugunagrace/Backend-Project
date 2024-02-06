# Generated by Django 4.2.5 on 2023-09-17 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0008_alter_communityhealthvolunteer_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='communityhealthvolunteer',
            name='assigned_household',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='communityhealthvolunteer',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], default=1, max_length=10),
            preserve_default=False,
        ),
    ]
