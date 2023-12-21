# Generated by Django 4.2.7 on 2023-11-29 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='repository_link',
            new_name='url',
        ),
        migrations.RemoveField(
            model_name='project',
            name='description',
        ),
        migrations.RemoveField(
            model_name='project',
            name='technologies',
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='projects/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
