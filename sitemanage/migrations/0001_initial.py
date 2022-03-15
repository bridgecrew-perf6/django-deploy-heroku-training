# Generated by Django 3.1 on 2022-03-15 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_title', models.CharField(max_length=100, verbose_name='meta_title')),
                ('meta_description', models.CharField(max_length=300, verbose_name='meta_description')),
                ('meta_keywords', models.CharField(max_length=300, verbose_name='SEO_keywords')),
                ('administrator', models.CharField(max_length=30, verbose_name='administrator')),
                ('top_title', models.CharField(max_length=100, verbose_name='top_title')),
                ('top_sub_title', models.CharField(max_length=200, verbose_name='top_sub_title')),
                ('site', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='sites.site', verbose_name='Site')),
            ],
        ),
    ]
