# Generated by Django 5.0.6 on 2024-05-16 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_alter_company_happy_clients_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='description',
            new_name='message',
        ),
        migrations.AlterField(
            model_name='featuredclient',
            name='logo',
            field=models.ImageField(upload_to='media/clients/'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(upload_to='media/portfolio/'),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='photo',
            field=models.ImageField(upload_to='media/team/'),
        ),
    ]