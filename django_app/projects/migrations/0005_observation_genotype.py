# Generated by Django 5.0 on 2023-12-29 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_remove_experiment_country_sample_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='observation',
            name='genotype',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
