# Generated by Django 2.0.3 on 2018-07-30 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_auto_20180724_0335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='employee_position',
            field=models.CharField(max_length=50),
        ),
    ]