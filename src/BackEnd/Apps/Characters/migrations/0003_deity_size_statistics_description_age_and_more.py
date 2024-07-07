# Generated by Django 5.0.6 on 2024-07-07 12:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Characters', '0002_remove_character_level_remove_character_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('info', models.CharField(blank=True, max_length=30, null=True)),
                ('alignment', models.CharField(blank=True, choices=[('Legal Bueno', 'Legal Bueno'), ('Legal Neutral', 'Legal Neutral'), ('Legal Maligno', 'Legal Maligno'), ('Neutral Bueno', 'Neutral Bueno'), ('Neutral Neutral', 'Neutral Neutral'), ('Neutral Maligno', 'Neutral Maligno'), ('Caótico Bueno', 'Caótico Bueno'), ('Caótico Neutral', 'Caótico Neutral'), ('Caótico Maligno', 'Caótico Maligno')], max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('Multa', 'Multa'), ('Diminutivo', 'Diminutivo'), ('Enano', 'Enano'), ('Pequeño', 'Pequeño'), ('Medio', 'Medio'), ('Grande', 'Grande'), ('Enorme', 'Enorme'), ('Gargantúa', 'Gargantúa'), ('Colosal', 'Colosal')], max_length=15)),
                ('modifier', models.CharField(editable=False, max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strength', models.IntegerField(blank=True, null=True)),
                ('strength_mod', models.IntegerField(blank=True, null=True)),
                ('strength_temporal', models.IntegerField(blank=True, null=True)),
                ('strength_mod_temporal', models.IntegerField(blank=True, null=True)),
                ('dexterity', models.IntegerField(blank=True, null=True)),
                ('dexterity_mod', models.IntegerField(blank=True, null=True)),
                ('dexterity_temporal', models.IntegerField(blank=True, null=True)),
                ('dexterity_mod_temporal', models.IntegerField(blank=True, null=True)),
                ('constitution', models.IntegerField(blank=True, null=True)),
                ('constitution_mod', models.IntegerField(blank=True, null=True)),
                ('constitution_temporal', models.IntegerField(blank=True, null=True)),
                ('constitution_mod_temporal', models.IntegerField(blank=True, null=True)),
                ('intelligence', models.IntegerField(blank=True, null=True)),
                ('intelligence_mod', models.IntegerField(blank=True, null=True)),
                ('intelligence_temporal', models.IntegerField(blank=True, null=True)),
                ('intelligence_mod_temporal', models.IntegerField(blank=True, null=True)),
                ('wisdom', models.IntegerField(blank=True, null=True)),
                ('wisdom_mod', models.IntegerField(blank=True, null=True)),
                ('wisdom_temporal', models.IntegerField(blank=True, null=True)),
                ('wisdom_mod_temporal', models.IntegerField(blank=True, null=True)),
                ('charisma', models.IntegerField(blank=True, null=True)),
                ('charisma_mod', models.IntegerField(blank=True, null=True)),
                ('charisma_temporal', models.IntegerField(blank=True, null=True)),
                ('charisma_mod_temporal', models.IntegerField(blank=True, null=True)),
                ('hit_points', models.IntegerField(blank=True, null=True)),
                ('armour_class', models.IntegerField(blank=True, null=True)),
                ('armour_class_armor', models.IntegerField(blank=True, null=True)),
                ('armour_class_shield', models.IntegerField(blank=True, null=True)),
                ('armour_class_natural_armor', models.IntegerField(blank=True, null=True)),
                ('armour_class_deflex', models.IntegerField(blank=True, null=True)),
                ('armour_class_other', models.IntegerField(blank=True, null=True)),
                ('speed', models.IntegerField(blank=True, null=True)),
                ('touch_armour_class', models.IntegerField(blank=True, null=True)),
                ('unaware_armour_class', models.IntegerField(blank=True, null=True)),
                ('initiative', models.IntegerField(blank=True, null=True)),
                ('initiative_other', models.IntegerField(blank=True, null=True)),
                ('base_attack', models.IntegerField(blank=True, null=True)),
                ('size_mod', models.IntegerField(blank=True, null=True)),
                ('grapple', models.IntegerField(blank=True, null=True)),
                ('grapple_other', models.IntegerField(blank=True, null=True)),
                ('spell_resistance', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='description',
            name='age',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='description',
            name='alignment',
            field=models.CharField(blank=True, choices=[('Legal Bueno', 'Legal Bueno'), ('Legal Neutral', 'Legal Neutral'), ('Legal Maligno', 'Legal Maligno'), ('Neutral Bueno', 'Neutral Bueno'), ('Neutral Neutral', 'Neutral Neutral'), ('Neutral Maligno', 'Neutral Maligno'), ('Caótico Bueno', 'Caótico Bueno'), ('Caótico Neutral', 'Caótico Neutral'), ('Caótico Maligno', 'Caótico Maligno')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='description',
            name='eyes',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='description',
            name='genre',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='description',
            name='hair',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='description',
            name='hight',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='description',
            name='skin',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='description',
            name='weight',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='description',
            name='deity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Characters.deity'),
        ),
        migrations.AddField(
            model_name='description',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Characters.size'),
        ),
        migrations.AddField(
            model_name='character',
            name='statistics',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Characters.statistics'),
        ),
    ]
