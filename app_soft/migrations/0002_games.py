# Generated by Django 5.1.6 on 2025-03-13 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_soft', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='games/')),
            ],
        ),
    ]
