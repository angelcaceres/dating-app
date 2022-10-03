# Generated by Django 4.1 on 2022-10-03 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0003_remove_user_zodiac_sign_user_zodiac_sign'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zodiacsign',
            name='lang',
        ),
        migrations.RemoveField(
            model_name='user',
            name='city_of_origin',
        ),
        migrations.RemoveField(
            model_name='user',
            name='location',
        ),
        migrations.AlterField(
            model_name='zodiacsign',
            name='name',
            field=models.CharField(choices=[('Aries', 'Aries'), ('Tauro', 'Taurus'), ('Geminis', 'Gemini'), ('Cancer', 'Cancer'), ('Leo', 'Leo'), ('Virgo', 'Virgo'), ('Libra', 'Libra'), ('Escorpio', 'Escorpio'), ('Sagitario', 'Sagitario'), ('Capricornio', 'Capricornio'), ('Acuario', 'Acuario'), ('Piscis', 'Piscis')], max_length=11),
        ),
        migrations.AddField(
            model_name='user',
            name='city_of_origin',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='city_origin', to='api_app.city'),
        ),
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='api_app.city'),
        ),
    ]
