# Generated by Django 5.0.2 on 2024-02-23 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_contact_alter_author_options_alter_book_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='date_of_birth',
            field=models.DateField(verbose_name='Date of birth'),
        ),
    ]