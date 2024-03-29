# Generated by Django 4.0.6 on 2022-09-09 09:19

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AutherModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='full name')),
                ('image', models.ImageField(upload_to='auther_images/', verbose_name='image')),
            ],
            options={
                'verbose_name': 'auther',
                'verbose_name_plural': 'authers',
            },
        ),
        migrations.CreateModel(
            name='PostTagModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
            },
        ),
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='body')),
                ('main_image', models.ImageField(upload_to='main_images/', verbose_name='main image')),
                ('banner', models.ImageField(upload_to='post_banners/', verbose_name='banner')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('auther', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='posts', to='blogs.authermodel')),
                ('tag', models.ManyToManyField(related_name='posts', to='blogs.posttagmodel', verbose_name='tag')),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
            },
        ),
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('phone', models.CharField(max_length=13, verbose_name='phone')),
                ('comment', models.TextField(verbose_name='comment')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blogs.postmodel', verbose_name='post')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
            },
        ),
    ]
