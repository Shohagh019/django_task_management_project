# Generated by Django 5.1.2 on 2024-11-15 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category_app', '0001_initial'),
        ('task_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='task_name',
            field=models.ManyToManyField(blank=True, related_name='categories', to='task_app.task'),
        ),
    ]
