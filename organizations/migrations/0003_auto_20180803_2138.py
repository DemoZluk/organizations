# Generated by Django 2.1 on 2018-08-03 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0002_auto_20180803_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='products',
            field=models.ManyToManyField(through='organizations.PriceList', to='organizations.Product'),
        ),
        migrations.RemoveField(
            model_name='pricelist',
            name='organization',
        ),
        migrations.AddField(
            model_name='pricelist',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='organizations.Organization'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='pricelist',
            name='product',
        ),
        migrations.AddField(
            model_name='pricelist',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='organizations.Product'),
            preserve_default=False,
        ),
    ]
