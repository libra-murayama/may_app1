# Generated by Django 3.0.4 on 2022-09-21 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_alter_friend_id_alter_message_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='message',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]