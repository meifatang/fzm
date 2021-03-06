# Generated by Django 3.1 on 2020-08-28 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('good_name', models.CharField(max_length=200)),
                ('quantity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
                ('type_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='StockOperate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('the_time', models.DateTimeField(verbose_name='Stock Operate time')),
                ('quantity', models.IntegerField(default=1)),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fzm.good')),
            ],
        ),
        migrations.AddField(
            model_name='good',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fzm.type'),
        ),
    ]
