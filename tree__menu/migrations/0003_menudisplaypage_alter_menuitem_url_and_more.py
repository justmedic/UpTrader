# Generated by Django 5.0.2 on 2024-02-21 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree__menu', '0002_alter_menuitem_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuDisplayPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255, unique=True, verbose_name='URL страницы')),
            ],
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='URL'),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='display_on_pages',
            field=models.ManyToManyField(blank=True, to='tree__menu.menudisplaypage', verbose_name='Показывать на страницах'),
        ),
    ]
