# Generated by Django 2.1.3 on 2018-12-27 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='clientes_photos'),
        ),
    ]
