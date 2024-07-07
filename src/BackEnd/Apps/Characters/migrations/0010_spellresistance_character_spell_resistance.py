# Generated by Django 5.0.6 on 2024-07-07 20:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Characters', '0009_capability_class_equip_feats_game_inventory_spell_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpellResistance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(blank=True, max_length=100, null=True)),
                ('saving_throw_CD', models.CharField(blank=True, max_length=100, null=True)),
                ('daily_spells', models.CharField(blank=True, max_length=100, null=True)),
                ('extra_spells', models.CharField(blank=True, max_length=100, null=True)),
                ('known_spells', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='spell_resistance',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Characters.spellresistance'),
        ),
    ]
