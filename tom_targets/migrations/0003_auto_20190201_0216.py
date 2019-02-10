# Generated by Django 2.1.5 on 2019-02-01 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tom_targets', '0002_auto_20190115_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='target',
            name='name2',
            field=models.CharField(blank=True, default='', help_text='An alternative name for this target', max_length=100, verbose_name='Name 2'),
        ),
        migrations.AlterField(
            model_name='target',
            name='name3',
            field=models.CharField(blank=True, default='', help_text='An alternative name for this target', max_length=100, verbose_name='Name 3'),
        ),
    ]