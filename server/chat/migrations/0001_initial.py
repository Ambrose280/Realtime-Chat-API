# Generated by Django 4.1 on 2023-07-10 11:01

from django.db import migrations, models
import shortuuidfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomId', shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22)),
                ('type', models.CharField(default='DM', max_length=10)),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]