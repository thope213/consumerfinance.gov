# Generated by Django 3.2.17 on 2023-03-01 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0230_rename_chinese'),
    ]

    operations = [
        migrations.AddField(
            model_name='browsefilterablepage',
            name='navigation_label',
            field=models.CharField(blank=True, help_text='Optional short label for left navigation.', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='browsepage',
            name='navigation_label',
            field=models.CharField(blank=True, help_text='Optional short label for left navigation.', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='browsefilterablepage',
            name='secondary_nav_exclude_sibling_pages',
            field=models.BooleanField(default=False, help_text="Don't show siblings of this page in the left navigation."),
        ),
        migrations.AlterField(
            model_name='browsepage',
            name='secondary_nav_exclude_sibling_pages',
            field=models.BooleanField(default=False, help_text="Don't show siblings of this page in the left navigation."),
        ),
    ]
