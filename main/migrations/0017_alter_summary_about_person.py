# Generated by Django 3.2 on 2022-04-09 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_professional_experience_about_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summary',
            name='about_person',
            field=models.TextField(),
        ),
    ]