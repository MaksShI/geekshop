# Generated by Django 3.2.3 on 2021-08-31 15:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_product_is_active'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('basketapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.product', verbose_name='продукт'),
        ),
        migrations.AlterField(
            model_name='basket',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='basket', to=settings.AUTH_USER_MODEL),
        ),
    ]
