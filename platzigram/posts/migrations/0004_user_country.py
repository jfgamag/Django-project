# Generated by Django 3.2.6 on 2021-08-09 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_rename_fist_name_user_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(default='Colombia', max_length=30),
        ),
    ]
