# Generated by Django 4.2.5 on 2023-09-29 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0002_rename_title_articles_title1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='title2',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
