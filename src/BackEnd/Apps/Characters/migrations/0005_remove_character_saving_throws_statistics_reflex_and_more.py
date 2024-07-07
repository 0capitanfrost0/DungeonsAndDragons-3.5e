# Generated by Django 5.0.6 on 2024-07-07 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Characters', '0004_savingthrow_alter_deity_info_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='saving_throws',
        ),
        migrations.AddField(
            model_name='statistics',
            name='reflex',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='statistics',
            name='reflex_base',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='statistics',
            name='reflex_magic',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='statistics',
            name='reflex_other',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='statistics',
            name='strength_base',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='statistics',
            name='strength_magic',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='statistics',
            name='strength_other',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='statistics',
            name='will',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='statistics',
            name='will_base',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='statistics',
            name='will_magic',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='statistics',
            name='will_other',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='strength',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
        migrations.DeleteModel(
            name='SavingThrow',
        ),
    ]