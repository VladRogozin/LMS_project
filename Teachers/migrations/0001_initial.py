# Generated by Django 4.1.5 on 2023-02-20 14:24

from django.db import migrations, models
import students.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(db_column='f_name', max_length=50, verbose_name='First name')),
                ('last_name', models.CharField(db_column='l_name', max_length=50, verbose_name='Last name')),
                ('birthday', models.DateField(blank=True, default='2023-01-01')),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(max_length=254, validators=[students.validators.validate_unique_email])),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('salary', models.PositiveIntegerField(default=10000)),
            ],
            options={
                'db_table': 'teachers',
            },
        ),
    ]
