# Generated by Django 3.1.1 on 2020-09-11 00:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classifier', '0004_uploadfile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadfile',
            old_name='upload',
            new_name='file',
        ),
    ]
