# Generated by Django 4.0.1 on 2022-12-01 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0003_remove_goal_category_goal_category_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goalcomment',
            options={'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.RenameField(
            model_name='goalcomment',
            old_name='text_comment',
            new_name='text',
        ),
    ]
