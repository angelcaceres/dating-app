# Generated by Django 4.1 on 2022-09-22 02:00

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciudad', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Drinking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Instagram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_instagram', models.BooleanField(default=False)),
                ('token', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='InterestCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Kids',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LookingFor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('municipio', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PoliticalView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Religion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Smoking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Spotify',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_spotify', models.BooleanField(default=False)),
                ('token', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ZodiacSign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='height_in_cm',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(220), django.core.validators.MinValueValidator(99)]),
        ),
        migrations.AddField(
            model_name='user',
            name='is_paid_profile',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='middle_name',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_app.interestcategory')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='city_of_origin',
            field=models.ManyToManyField(default=None, to='api_app.city'),
        ),
        migrations.AddField(
            model_name='user',
            name='drinking',
            field=models.ManyToManyField(default=None, to='api_app.drinking'),
        ),
        migrations.AddField(
            model_name='user',
            name='education',
            field=models.ManyToManyField(default=None, to='api_app.education'),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.ManyToManyField(default=None, to='api_app.gender'),
        ),
        migrations.AddField(
            model_name='user',
            name='instagram',
            field=models.ManyToManyField(default=None, to='api_app.instagram'),
        ),
        migrations.AddField(
            model_name='user',
            name='interests',
            field=models.ManyToManyField(default=None, to='api_app.interest'),
        ),
        migrations.AddField(
            model_name='user',
            name='kids',
            field=models.ManyToManyField(default=None, to='api_app.kids'),
        ),
        migrations.AddField(
            model_name='user',
            name='languages',
            field=models.ManyToManyField(default=None, to='api_app.languages'),
        ),
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.ManyToManyField(default=None, to='api_app.municipio'),
        ),
        migrations.AddField(
            model_name='user',
            name='looking_for',
            field=models.ManyToManyField(default=None, to='api_app.lookingfor'),
        ),
        migrations.AddField(
            model_name='user',
            name='political_views',
            field=models.ManyToManyField(default=None, to='api_app.politicalview'),
        ),
        migrations.AddField(
            model_name='user',
            name='questions',
            field=models.ManyToManyField(default=None, to='api_app.question'),
        ),
        migrations.AddField(
            model_name='user',
            name='religion',
            field=models.ManyToManyField(default=None, to='api_app.religion'),
        ),
        migrations.AddField(
            model_name='user',
            name='smoking',
            field=models.ManyToManyField(default=None, to='api_app.smoking'),
        ),
        migrations.AddField(
            model_name='user',
            name='spotify',
            field=models.ManyToManyField(default=None, to='api_app.spotify'),
        ),
        migrations.AddField(
            model_name='user',
            name='workout',
            field=models.ManyToManyField(default=None, to='api_app.workout'),
        ),
        migrations.AddField(
            model_name='user',
            name='zodiac_sign',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='api_app.zodiacsign'),
        ),
    ]
