# Generated by Django 3.1.3 on 2020-11-05 13:51

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainBlog', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]