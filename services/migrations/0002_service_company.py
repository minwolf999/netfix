# Generated by Django 3.2.12 on 2023-12-14 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.company'),
        ),
    ]