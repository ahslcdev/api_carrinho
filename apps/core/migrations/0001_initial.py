# Generated by Django 4.2 on 2024-05-18 00:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name='Data de atualizado')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome do item')),
                ('preco', models.IntegerField(verbose_name='Valor do item')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Itens',
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name='Data de atualizado')),
                ('id_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
        migrations.CreateModel(
            name='PedidoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name='Data de atualizado')),
                ('quantidade', models.IntegerField(default=1, verbose_name='Quantidade de itens')),
                ('id_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.item', verbose_name='Item')),
                ('id_pedido', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.pedido', verbose_name='Pedido')),
            ],
            options={
                'verbose_name': 'Pedido e Item',
                'verbose_name_plural': 'Pedidos e Itens',
            },
        ),
    ]
