# Generated by Django 4.0.1 on 2022-12-03 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0004_alter_goalcomment_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goals', to='goals.goalcategory', verbose_name='Категория'),
        ),
    ]
