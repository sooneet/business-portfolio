# Generated by Django 3.2 on 2022-04-11 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_alter_contact_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_message',
            field=models.TextField(),
        ),
    ]