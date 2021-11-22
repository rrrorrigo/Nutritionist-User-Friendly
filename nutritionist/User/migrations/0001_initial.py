# Generated by Django 3.2.9 on 2021-11-22 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nutritionist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('username', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=320)),
                ('password', models.CharField(max_length=33)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('username', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=320)),
                ('password', models.CharField(max_length=33)),
                ('weight', models.IntegerField(default=0)),
                ('height', models.IntegerField(default=0)),
                ('objective', models.CharField(max_length=250)),
                ('diet', models.CharField(max_length=250)),
                ('nextConsultantion', models.DateField()),
                ('nutritionistId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.nutritionist')),
            ],
        ),
    ]
