# Generated by Django 3.0 on 2019-12-15 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_tag',
            field=models.ManyToManyField(to='blog.Tag', verbose_name='Tags'),
        ),
    ]
