# Generated by Django 2.0.2 on 2018-09-11 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180824_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cotegories',
            field=models.ManyToManyField(related_name='get_posts', to='blog.category', verbose_name='categorias'),
        ),
    ]