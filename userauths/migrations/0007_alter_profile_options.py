# Generated by Django 4.2.5 on 2023-11-02 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0006_remove_profile_following_remove_profile_slug_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['-date']},
        ),
    ]