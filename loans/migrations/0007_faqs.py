# Generated by Django 2.1.5 on 2019-02-02 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0006_auto_20190201_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faqs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=250)),
                ('answer', models.TextField(max_length=1000)),
                ('pub_date', models.DateField(auto_now=True)),
            ],
        ),
    ]