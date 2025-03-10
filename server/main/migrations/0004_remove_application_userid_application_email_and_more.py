# Generated by Django 5.1.6 on 2025-03-06 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_application_resume'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='userID',
        ),
        migrations.AddField(
            model_name='application',
            name='email',
            field=models.EmailField(default='example@gmail.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='firstName',
            field=models.CharField(default='john', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='lastName',
            field=models.CharField(default='Doe', max_length=100),
            preserve_default=False,
        ),
    ]
