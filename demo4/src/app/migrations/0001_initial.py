# Generated by Django 2.0.7 on 2018-07-31 16:38

import app.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=100, verbose_name='班级')),
            ],
            options={
                'verbose_name': '班级',
                'verbose_name_plural': '班级',
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='学生姓名')),
                ('sex', models.CharField(choices=[('男', '男'), ('女', '女')], max_length=50, verbose_name='性别')),
                ('studentname', models.CharField(blank=True, max_length=250, verbose_name='学号')),
                ('enter_date', models.DateField(verbose_name='违纪时间')),
                ('reason', models.TextField(blank=True, verbose_name='违纪原因')),
                ('level', models.CharField(choices=[('警告', '警告'), ('严重警告', '严重警告'), ('记过', '记过'), ('留校察看', '留校察看')], max_length=30, verbose_name='处分类型')),
                ('photo', models.ImageField(blank=True, null=True, upload_to=app.models.Students.get_photo, verbose_name='相关照片')),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Class', verbose_name='所在班级')),
            ],
            options={
                'verbose_name': '学生信息',
                'verbose_name_plural': '学生信息',
            },
        ),
    ]
