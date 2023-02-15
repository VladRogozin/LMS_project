# Generated by Django 4.1.5 on 2023-02-15 18:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groups', '0003_alter_group_group_start'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(db_column='c_name', max_length=50, verbose_name='course name')),
                ('course_start', models.DateField(default=datetime.date.today)),
                ('course_text', models.TextField(blank=True, null=True)),
                ('course_group', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course_group', to='groups.group')),
            ],
            options={
                'db_table': 'courses',
            },
        ),
    ]
