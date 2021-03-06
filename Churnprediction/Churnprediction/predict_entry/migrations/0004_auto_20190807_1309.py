# Generated by Django 2.1.5 on 2019-08-07 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict_entry', '0003_auto_20190806_1413'),
    ]

    operations = [
        migrations.CreateModel(
            name='Churn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Nonchurn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('non_name', models.CharField(max_length=50)),
                ('non_address', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='predict',
            name='address',
            field=models.CharField(default=1, max_length=50),
        ),
        migrations.AddField(
            model_name='predict',
            name='full_name',
            field=models.CharField(default=1, max_length=50),
        ),
        migrations.AddField(
            model_name='predict',
            name='phone_no',
            field=models.IntegerField(default=1),
        ),
    ]
