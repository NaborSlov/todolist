# Generated by Django 4.0.1 on 2022-12-12 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_alter_tguser_chat_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='tguser',
            name='verification_code',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Код верификации'),
        ),
    ]