# Generated by Django 4.0.4 on 2022-06-05 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imageapp', '0007_remove_image_sizedimages_image_sizedimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_tier', to='imageapp.tier'),
        ),
    ]