# Generated by Django 3.2 on 2021-04-15 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_auto_20210414_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodsinfo',
            name='goodssubmit',
            field=models.CharField(default='0', max_length=10),
        ),
    ]