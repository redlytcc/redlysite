# Generated by Django 2.1.3 on 2018-11-20 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redweb', '0005_auto_20181120_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='visible',
            field=models.IntegerField(default=1),
        ),
    ]
