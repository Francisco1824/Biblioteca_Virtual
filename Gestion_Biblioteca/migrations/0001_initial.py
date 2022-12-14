# Generated by Django 4.1.2 on 2022-10-21 19:49

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
            name='Bibliotecas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=100)),
                ('Imagen', models.ImageField(default='', upload_to='imagenes_libros')),
                ('Autor', models.CharField(max_length=150)),
                ('Tipo', models.CharField(max_length=50)),
                ('Genero', models.CharField(max_length=35)),
                ('Resumen', models.CharField(max_length=2000)),
                ('FechaPublicacion', models.DateField()),
                ('Nacionalidad', models.CharField(max_length=50)),
                ('Estado', models.BooleanField(default=True)),
                ('PrecioNeto', models.FloatField()),
                ('PrecioVenta', models.FloatField()),
                ('PrecioSuscripcion', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Nombres', models.CharField(max_length=70)),
                ('Apellidos', models.CharField(max_length=70)),
                ('Edad', models.SmallIntegerField(default='18')),
                ('DNI', models.CharField(default='Cedula', max_length=20)),
                ('NumeroDNI', models.BigIntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Pais', models.CharField(max_length=50)),
                ('Ciudad', models.CharField(max_length=50)),
                ('Direccion', models.CharField(max_length=70)),
                ('Telefono', models.BigIntegerField()),
                ('Fecha_Registro', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('idProveedor', models.AutoField(primary_key=True, serialize=False)),
                ('Nombres', models.CharField(max_length=70)),
                ('NIT', models.BigIntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Direccion', models.CharField(max_length=70)),
                ('Telefono', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Suscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'suscripcion',
                'verbose_name_plural': 'suscripciones',
                'db_table': 'suscripciones',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Revistas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=100)),
                ('Imagen', models.ImageField(default='', upload_to='imagenes_revista')),
                ('Autor', models.CharField(max_length=150)),
                ('Tipo', models.CharField(max_length=50)),
                ('Genero', models.CharField(max_length=35)),
                ('Resumen', models.CharField(max_length=2000)),
                ('FechaPublicacion', models.DateField()),
                ('Nacionalidad', models.CharField(max_length=50)),
                ('Estado', models.BooleanField(default=True)),
                ('PrecioNeto', models.FloatField()),
                ('PrecioVenta', models.FloatField()),
                ('PrecioSuscripcion', models.FloatField()),
                ('Proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion_Biblioteca.proveedores')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
                'db_table': 'pedidos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='lineasuscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default='1')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Gestion_Biblioteca.revistas')),
                ('suscripcion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Gestion_Biblioteca.suscripcion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'lineasuscripcion',
                'verbose_name_plural': 'lineasuscripciones',
                'db_table': 'lineasuscripciones',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='lineapedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default='1')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('pedido', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Gestion_Biblioteca.pedido')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion_Biblioteca.bibliotecas')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Lineapedido',
                'verbose_name_plural': 'Lineapedidos',
                'db_table': 'lineapedidos',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='bibliotecas',
            name='Proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion_Biblioteca.proveedores'),
        ),
    ]
