# Generated by Django 5.1 on 2024-09-11 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0008_remove_producto_id_producto_id_producto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='id_producto',
        ),
        migrations.AddField(
            model_name='producto',
            name='id',
            field=models.BigAutoField(auto_created=True, default='2024-09-08 14:00:00', primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
