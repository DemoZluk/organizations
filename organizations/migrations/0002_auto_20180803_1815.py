# Generated by Django 2.1 on 2018-08-03 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organization',
            old_name='district_id',
            new_name='district',
        ),
        migrations.RenameField(
            model_name='pricelist',
            old_name='organization_id',
            new_name='organization',
        ),
        migrations.RenameField(
            model_name='pricelist',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='category_id',
            new_name='category',
        ),
    ]
