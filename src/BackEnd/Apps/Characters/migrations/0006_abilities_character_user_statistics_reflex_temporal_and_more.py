# Generated by Django 5.0.6 on 2024-07-07 18:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Characters', '0005_remove_character_saving_throws_statistics_reflex_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Abilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('class_bonus', models.BooleanField(default=False)),
                ('basic', models.BooleanField(default=False, editable=False)),
                ('modifier', models.CharField(max_length=40)),
                ('sum', models.IntegerField(blank=True, editable=False, null=True)),
                ('modifier_rank', models.IntegerField(blank=True, null=True)),
                ('rank', models.IntegerField(blank=True, null=True)),
                ('other_modifier', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='statistics',
            name='reflex_temporal',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='statistics',
            name='will_temporal',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='abilities',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Characters.abilities'),
        ),
    ]
