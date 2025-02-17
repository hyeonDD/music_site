# Generated by Django 3.2.9 on 2022-02-25 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='album',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='music',
            name='genre',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='music',
            name='lyricists',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='music',
            name='lyrics',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='music',
            name='release_date',
            field=models.DateField(null=True),
        ),
    ]
