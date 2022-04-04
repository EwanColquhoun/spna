# Generated by Django 4.0.3 on 2022-04-04 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_document_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='category',
            field=models.CharField(choices=[('1', 'Media Releases'), ('2', 'Media Mentions'), ('3', 'Letters to and responses from Government')], default=False, max_length=20),
        ),
    ]
