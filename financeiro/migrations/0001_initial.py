# Generated by Django 5.1.2 on 2024-10-19 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gasto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('tipo_gasto', models.CharField(max_length=50)),
                ('tipo_local', models.CharField(max_length=50)),
                ('tipo_quem', models.CharField(max_length=50)),
                ('entrada_saida', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=20)),
                ('observacao', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
