# Generated by Django 3.0.8 on 2020-08-27 14:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('part2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_level', models.CharField(blank=True, max_length=225)),
                ('question', models.CharField(blank=True, max_length=255)),
                ('option_A', models.CharField(blank=True, max_length=255)),
                ('option_B', models.CharField(blank=True, max_length=255)),
                ('option_C', models.CharField(blank=True, max_length=255)),
                ('option_D', models.CharField(blank=True, max_length=255)),
                ('correct_answer', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='register',
            name='level',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='register',
            name='total_score',
            field=models.IntegerField(default=0),
        ),
    ]