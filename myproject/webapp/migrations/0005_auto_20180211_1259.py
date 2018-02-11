# Generated by Django 2.0.2 on 2018-02-11 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20180205_0924'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='caselog',
            name='handleby',
            field=models.CharField(blank=True, choices=[('david', 'David'), ('andy', 'Andy')], max_length=5, null=True),
        ),
    ]
