# Generated by Django 4.2.2 on 2023-06-16 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0003_remove_orderautopart_auto_part_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('service', models.CharField(max_length=250)),
                ('date', models.CharField(max_length=250)),
                ('comment', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='OrderAutoPart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('auto_part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.autopart')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
            ],
        ),
    ]
