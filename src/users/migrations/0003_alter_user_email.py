# Generated by Django 4.0.6 on 2022-07-29 17:46

import django.contrib.postgres.fields.citext
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_name_company_identifier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=django.contrib.postgres.fields.citext.CIEmailField(max_length=254, unique=True, verbose_name='Email Address'),
        ),
    ]
