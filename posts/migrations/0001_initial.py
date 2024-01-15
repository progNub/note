# Generated by Django 5.0.1 on 2024-01-15 19:49

import django.db.models.deletion
import posts.models
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, unique=True, verbose_name='Название тега')),
            ],
            options={
                'verbose_name': 'Тэг',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('mod_time', models.DateTimeField(default=None, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=posts.models.upload_to, verbose_name='Изображение')),
                ('autor', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notes', to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(blank=True, related_name='notes', to='posts.tag', verbose_name='Теги')),
            ],
            options={
                'verbose_name': 'Запись',
                'verbose_name_plural': 'Записи',
                'ordering': ('-created_at',),
                'indexes': [models.Index(fields=['created_at'], name='created_at_index'), models.Index(fields=['mod_time'], name='mod_time_index')],
            },
        ),
    ]
