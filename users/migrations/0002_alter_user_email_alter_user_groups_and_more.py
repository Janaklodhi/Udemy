# Generated by Django 5.1.4 on 2025-01-05 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(help_text='A unique email address for the user.', max_length=254, unique=True, verbose_name='Email Address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='custom_user_set', to='auth.group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='custom_user_permissions', to='auth.permission', verbose_name='user permissions'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(help_text='A unique identifier for the user.', max_length=50, unique=True, verbose_name='Username'),
        ),
    ]
