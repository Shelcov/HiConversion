# Generated by Django 2.0.1 on 2018-01-19 11:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InviteUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(default=None, max_length=128, verbose_name='Инвайт')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name_plural': 'Отправленные инвайты',
                'verbose_name': 'Отправленный инвайт',
            },
        ),
        migrations.AlterModelOptions(
            name='invite',
            options={'verbose_name': 'Приглашенный', 'verbose_name_plural': 'Приглашенные'},
        ),
        migrations.AlterField(
            model_name='invite',
            name='user_invite',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='invite_to', to=settings.AUTH_USER_MODEL, verbose_name='Приглашенный'),
        ),
    ]
