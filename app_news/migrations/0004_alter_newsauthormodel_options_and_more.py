# Generated by Django 5.1.5 on 2025-02-01 14:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0003_newsauthormodel_newstagmodel_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsauthormodel',
            options={'verbose_name': 'News author', 'verbose_name_plural': 'News authors'},
        ),
        migrations.AlterModelOptions(
            name='newscategorymodel',
            options={'verbose_name': 'News Category', 'verbose_name_plural': 'News Categories'},
        ),
        migrations.AlterModelOptions(
            name='newstagmodel',
            options={'verbose_name': 'News title', 'verbose_name_plural': 'News titles'},
        ),
        migrations.CreateModel(
            name='NewsCommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('message', models.TextField()),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='app_news.newsmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
    ]
