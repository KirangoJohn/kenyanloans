# Generated by Django 2.1.5 on 2019-02-01 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0005_auto_20190127_1215'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loantype',
            old_name='laon_name',
            new_name='loan_name',
        ),
    ]
