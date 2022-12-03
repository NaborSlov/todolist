# Generated by Django 4.0.1 on 2022-12-01 14:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goals', '0002_rename_create_goalcategory_created_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goal',
            name='category',
        ),
        migrations.AddField(
            model_name='goal',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='goals.goalcategory', verbose_name='Категория'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='goal',
            name='due_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дедлайн'),
        ),
        migrations.CreateModel(
            name='GoalComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(verbose_name='Дата создания')),
                ('updated', models.DateTimeField(verbose_name='Дата последнего обновления')),
                ('text_comment', models.TextField(verbose_name='Текст')),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goals.goal', verbose_name='Цель')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарий',
            },
        ),
    ]