# Generated by Django 3.1.5 on 2021-01-16 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('desc', models.CharField(max_length=800)),
                ('cost', models.PositiveSmallIntegerField()),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000)),
                ('rating', models.PositiveIntegerField()),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_author', to='accounts.profile')),
                ('class_for', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.class')),
                ('user_for', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_reviewed', to='accounts.profile')),
            ],
        ),
    ]
