# Generated by Django 4.0.4 on 2022-06-05 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imageapp', '0005_delete_sizedimage_remove_tier_thumbnail_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='SizedImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='sizedImages',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sizedimage_image', to='imageapp.sizedimage'),
        ),
    ]
