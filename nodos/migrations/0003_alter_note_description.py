# Generated by Django 4.1.1 on 2022-09-18 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodos', '0002_alter_note_done'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='description',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
