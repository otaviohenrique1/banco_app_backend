# Generated by Django 5.1.2 on 2024-10-16 17:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('senha', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=11, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cartao2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=4)),
                ('numero', models.CharField(max_length=4)),
                ('validade', models.CharField(max_length=10)),
                ('cvv', models.CharField(max_length=255)),
                ('tipo', models.CharField(choices=[('F', 'Fisico'), ('T', 'Temporario'), ('V', 'Virtual')], default='F', max_length=1)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banco3.cliente2')),
            ],
        ),
        migrations.CreateModel(
            name='Conta2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saldo', models.DecimalField(decimal_places=2, max_digits=20)),
                ('agencia', models.IntegerField()),
                ('banco', models.IntegerField()),
                ('conta_numero', models.IntegerField(unique=True)),
                ('nome_banco', models.CharField(max_length=255)),
                ('cliente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='conta', to='banco3.cliente2')),
            ],
        ),
    ]
