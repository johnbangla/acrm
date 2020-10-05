# Generated by Django 3.1.2 on 2020-10-01 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20201001_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('eat', 'eat'), ('play', 'play'), ('study', 'study'), ('positive emotion', 'positive emotion'), ('negative emotion', 'negative emotion')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Food', 'Food'), ('Out Door', 'Out Door'), ('In Door', 'In Door'), ('swim', 'swim'), ('writing', 'writing'), ('Reading', 'Reading'), ('Play', 'Play')], max_length=200, null=True),
        ),
    ]
