# Generated by Django 3.0.8 on 2020-07-16 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=200, unique=True)),
                ('status', models.CharField(blank=True, choices=[('active', 'active'), ('', 'default')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.TextField()),
                ('rank', models.IntegerField()),
                ('status', models.CharField(blank=True, choices=[('active', 'active'), ('', 'default')], max_length=100)),
                ('upper_part', models.CharField(max_length=300)),
                ('lower_part', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=200, unique=True)),
                ('status', models.CharField(blank=True, choices=[('active', 'active'), ('', 'default')], max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('price', models.IntegerField()),
                ('discounted_price', models.IntegerField(default=0)),
                ('image', models.TextField()),
                ('description', models.TextField(blank=True)),
                ('slug', models.CharField(max_length=300, unique=True)),
                ('brand', models.CharField(max_length=200)),
                ('stock', models.CharField(choices=[('In-stock', 'In-stock'), ('Out-of-stock', 'Out-of-stock')], max_length=200)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.Category')),
                ('subcategory', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.Subcategory')),
            ],
        ),
    ]