# Generated by Django 3.2.5 on 2021-07-21 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_blog_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
