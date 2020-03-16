# Generated by Django 3.0.4 on 2020-03-16 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core_learn_race', '0002_auto_20200312_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='race',
            name='total_score',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='player',
            name='raseId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='core_learn_race.Race'),
        ),
    ]
