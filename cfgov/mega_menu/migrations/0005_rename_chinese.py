# Generated by Django 3.2.17 on 2023-03-01 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mega_menu', '0004_deprecate_zh_hans'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='language',
            field=models.CharField(choices=[('ar', 'Arabic'), ('zh-Hant', 'Chinese'), ('en', 'English'), ('ht', 'Haitian Creole'), ('ko', 'Korean'), ('ru', 'Russian'), ('es', 'Spanish'), ('tl', 'Tagalog'), ('vi', 'Vietnamese')], max_length=100, primary_key=True, serialize=False),
        ),
    ]
