# Generated by Django 4.0.6 on 2022-07-29 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
