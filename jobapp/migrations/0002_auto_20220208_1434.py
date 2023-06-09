# Generated by Django 3.2.9 on 2022-02-08 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='andidate_totalexperienced',
        ),
        migrations.AddField(
            model_name='candidate',
            name='candidate_totalexperienced',
            field=models.CharField(default=1, max_length=100, verbose_name='toexp'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='candidate',
            name='candidate_experienced',
            field=models.CharField(max_length=100, verbose_name='exp'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='candidate_lastqualification',
            field=models.CharField(max_length=100, verbose_name='lastqua'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='candidate_photo',
            field=models.FileField(upload_to='images/', verbose_name='photo:'),
        ),
    ]
