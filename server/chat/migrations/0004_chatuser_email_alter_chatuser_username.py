# Generated by Django 4.1 on 2023-07-11 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_chatuser_alter_chatmessage_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatuser',
            name='email',
            field=models.CharField(blank=True, default='testuser@gmail.com', max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='chatuser',
            name='username',
            field=models.CharField(blank=True, default='testuser', max_length=256, null=True),
        ),
    ]