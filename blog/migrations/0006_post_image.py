# Generated by Django 2.2.1 on 2019-07-05 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190704_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='not set', upload_to=''),
            preserve_default=False,
        ),
    ]