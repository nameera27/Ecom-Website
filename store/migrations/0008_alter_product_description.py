# Generated by Django 4.2 on 2023-05-11 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_order_email_order_name_alter_order_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(default='', max_length=20000, null=True),
        ),
    ]