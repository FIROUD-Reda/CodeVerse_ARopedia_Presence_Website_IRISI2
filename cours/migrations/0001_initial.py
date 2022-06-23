# Generated by Django 4.0.4 on 2022-06-19 20:20

import cours.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '__first__'),
        ('module', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapitre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=250, null=True)),
                ('image', models.ImageField(default='/img/cours/folder-files-and-folders-svgrepo-com.svg', upload_to=cours.models.upload_location)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('element_module', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='module.elementmodule')),
                ('professeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.professeur')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_image', models.CharField(default='Sans Nom', max_length=30)),
                ('is_qrcode', models.BooleanField(default=False)),
                ('path_image', models.FileField(default='NULL', upload_to=cours.models.model_image_location)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Modele3D',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre_modele3d', models.CharField(max_length=40)),
                ('path_modele3d', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Traitement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre_traitement', models.CharField(max_length=40)),
                ('label_traitement', models.CharField(blank=True, max_length=100, null=True)),
                ('type_traitement', models.CharField(max_length=25)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('chapitre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cours.chapitre')),
                ('image', models.ForeignKey(blank=True, default='NULL', null=True, on_delete=django.db.models.deletion.SET_NULL, to='cours.image')),
                ('modele3D', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cours.modele3d')),
                ('visibilite', models.ManyToManyField(to='users.professeur')),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path_file', models.FileField(max_length=255, upload_to=cours.models.file_upload_location)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('modele3D', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cours.modele3d')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=40)),
                ('type', models.CharField(max_length=20)),
                ('path', models.FileField(max_length=255, upload_to=cours.models.document_file_upload_location)),
                ('image', models.ImageField(default='NULL', upload_to=cours.models.document_image_upload_location)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('chapitre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cours.chapitre')),
            ],
        ),
    ]
