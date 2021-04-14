# Generated by Django 3.1.2 on 2021-04-14 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_user_identity'),
    ]

    operations = [
        migrations.CreateModel(
            name='goodsinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('goodsname', models.CharField(max_length=80)),
                ('goodsinfo', models.CharField(max_length=300)),
                ('goodsprice', models.FloatField(max_length=10)),
                ('goodspic', models.ImageField(default='default.jpg', upload_to='upload')),
            ],
        ),
    ]
