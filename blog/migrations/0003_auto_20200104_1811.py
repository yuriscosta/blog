# Generated by Django 3.0.2 on 2020-01-04 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='update',
            new_name='updated',
        ),
    ]
