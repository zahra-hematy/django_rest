# Generated by Django 5.0.2 on 2024-04-05 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_comment_parent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='imgs',
            new_name='img',
        ),
    ]