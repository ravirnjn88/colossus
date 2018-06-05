# Generated by Django 2.0.6 on 2018-06-05 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Sent'), (2, 'Scheduled'), (3, 'Draft'), (4, 'Trashed')], default=3, verbose_name='status'),
        ),
    ]
