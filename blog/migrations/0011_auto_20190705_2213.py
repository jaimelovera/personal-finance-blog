# Generated by Django 2.2.1 on 2019-07-06 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20190705_2108'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='main_image',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='post',
            name='article_image_1',
        ),
        migrations.RemoveField(
            model_name='post',
            name='article_image_2',
        ),
        migrations.RemoveField(
            model_name='post',
            name='article_image_3',
        ),
        migrations.RemoveField(
            model_name='post',
            name='article_image_4',
        ),
        migrations.RemoveField(
            model_name='post',
            name='article_image_5',
        ),
        migrations.RemoveField(
            model_name='post',
            name='article_image_6',
        ),
    ]
