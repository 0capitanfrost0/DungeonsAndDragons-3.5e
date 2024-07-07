# Generated by Django 5.0.6 on 2024-07-07 20:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Characters', '0008_remove_characterabilities_statistics'),
    ]

    operations = [
        migrations.CreateModel(
            name='Capability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Class',
                'verbose_name_plural': 'Classes',
            },
        ),
        migrations.CreateModel(
            name='Equip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('armor_bonus', models.CharField(blank=True, max_length=100, null=True)),
                ('dex_cap', models.CharField(blank=True, max_length=100, null=True)),
                ('weight', models.CharField(blank=True, max_length=100, null=True)),
                ('type', models.CharField(blank=True, max_length=100, null=True)),
                ('speed_cap', models.CharField(blank=True, max_length=100, null=True)),
                ('penalizer', models.CharField(blank=True, max_length=100, null=True)),
                ('spell_cap', models.CharField(blank=True, max_length=100, null=True)),
                ('note', models.CharField(blank=True, max_length=100, null=True)),
                ('special_properties', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('requirements', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('quantity', models.CharField(blank=True, max_length=100, null=True)),
                ('weight', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Spell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('school', models.CharField(blank=True, max_length=100, null=True)),
                ('subschool', models.CharField(blank=True, max_length=100, null=True)),
                ('descriptor', models.CharField(blank=True, max_length=100, null=True)),
                ('level', models.IntegerField(blank=True, null=True)),
                ('class_list', models.CharField(blank=True, max_length=100, null=True)),
                ('components', models.CharField(blank=True, max_length=100, null=True)),
                ('casting_time', models.CharField(blank=True, max_length=50, null=True)),
                ('range', models.CharField(blank=True, max_length=100, null=True)),
                ('tarjet', models.CharField(blank=True, max_length=100, null=True)),
                ('efect', models.CharField(blank=True, max_length=100, null=True)),
                ('duration', models.CharField(blank=True, max_length=50, null=True)),
                ('saving_throw', models.CharField(blank=True, max_length=100, null=True)),
                ('spell_resistance', models.CharField(blank=True, max_length=100, null=True)),
                ('short_descriptive_text', models.TextField(blank=True, null=True)),
                ('complete_descriptive_text', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Spell',
                'verbose_name_plural': 'Spells',
            },
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('attack_bonus', models.CharField(blank=True, max_length=100, null=True)),
                ('damage', models.CharField(blank=True, max_length=100, null=True)),
                ('critic', models.CharField(blank=True, max_length=100, null=True)),
                ('type', models.CharField(blank=True, max_length=100, null=True)),
                ('range', models.CharField(blank=True, max_length=100, null=True)),
                ('note', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='imagen',
            field=models.URLField(blank=True, default='https://www.shutterstock.com/image-vector/error-500-page-empty-symbol-260nw-1711106146.jpg', null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='type',
            field=models.CharField(blank=True, choices=[('Personaje Jugable', 'Personaje Jugable'), ('Personaje No Jugable', 'Personaje No Jugable')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='description',
            name='lenguages',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='capability',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Characters.capability'),
        ),
        migrations.AddField(
            model_name='character',
            name='class_info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Characters.class'),
        ),
        migrations.AddField(
            model_name='character',
            name='equiped_objects',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Characters.equip'),
        ),
        migrations.AddField(
            model_name='character',
            name='feats',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Characters.feats'),
        ),
        migrations.AddField(
            model_name='character',
            name='game',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Characters.game'),
        ),
        migrations.AddField(
            model_name='character',
            name='inventory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Characters.inventory'),
        ),
        migrations.AddField(
            model_name='class',
            name='class_spell_list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Characters.spell'),
        ),
        migrations.AddField(
            model_name='character',
            name='weapons',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Characters.weapon'),
        ),
    ]
