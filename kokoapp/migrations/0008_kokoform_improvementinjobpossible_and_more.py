# Generated by Django 5.0.6 on 2024-05-20 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kokoapp', '0007_kokoform_adequatetrainingprograms_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='kokoform',
            name='ImprovementInJobPossible',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='kokoform',
            name='ReasonOfLeave',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
