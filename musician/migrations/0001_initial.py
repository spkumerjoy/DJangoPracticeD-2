# Generated by Django 5.1.1 on 2024-11-30 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('instrument_type', models.CharField(choices=[('guitar', 'Guitar'), ('drums', 'Drums'), ('bass', 'Bass'), ('piano', 'Piano'), ('violin', 'Violin'), ('vocals', 'Vocals')], max_length=50)),
            ],
        ),
    ]