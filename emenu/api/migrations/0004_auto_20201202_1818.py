# Generated by Django 2.2.17 on 2020-12-02 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20201202_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
