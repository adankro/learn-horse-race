# Generated by Django 3.0.4 on 2020-03-12 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('value', models.IntegerField()),
                ('category', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Rase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=10)),
                ('state', models.BooleanField(default=True)),
                ('subjects', models.CharField(max_length=50)),
                ('categories', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('score', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('winner', models.BooleanField(default=False)),
                ('raseId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_learn_race.Rase')),
            ],
        ),
    ]
