# Generated by Django 2.0.2 on 2018-02-13 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_comment_belong_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='best_comment',
            field=models.BooleanField(default=False),
        ),
    ]
