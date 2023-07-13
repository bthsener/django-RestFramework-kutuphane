# Generated by Django 4.2.3 on 2023-07-13 07:01

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kitaplar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kitap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=120)),
                ('yazar', models.CharField(max_length=120)),
                ('aciklama', models.TextField()),
                ('yaratilma_tarihi', models.DateTimeField(auto_now_add=True)),
                ('guncellenme_tarihi', models.DateTimeField(auto_now=True)),
                ('yayin_tarihi', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Yorum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yorum_sahibi', models.CharField(max_length=120)),
                ('yorum', models.TextField()),
                ('yaratilma_tarihi', models.DateTimeField(auto_now_add=True)),
                ('guncellenme_tarihi', models.DateTimeField(auto_now=True)),
                ('degerlendirme', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('kitap', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yorumlar', to='kitaplar.kitap')),
            ],
        ),
        migrations.DeleteModel(
            name='Kitaplar',
        ),
        migrations.DeleteModel(
            name='Yazar',
        ),
    ]