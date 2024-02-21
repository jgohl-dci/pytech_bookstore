# Generated by Django 5.0.2 on 2024-02-21 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_book_options_alter_genre_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('phone_number', models.CharField(max_length=20)),
                ('message', models.TextField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='author',
            options={'get_latest_by': 'created_on', 'ordering': ['last_name', 'first_name'], 'verbose_name': 'Author', 'verbose_name_plural': 'Authors'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['title', 'author']},
        ),
    ]