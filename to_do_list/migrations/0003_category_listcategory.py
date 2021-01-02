# Generated by Django 3.1.4 on 2021-01-02 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0002_auto_20210102_1254'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ListCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='to_do_list.category')),
                ('item_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='to_do_list.items')),
            ],
        ),
    ]
