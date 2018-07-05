# Generated by Django 2.0.5 on 2018-06-08 20:17

from django.db import migrations, models
import django.db.models.deletion
import economy.models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0084_auto_20180604_1723'),
    ]

    operations = [
        migrations.CreateModel(
            name='TokenApproval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('coinbase', models.CharField(max_length=50)),
                ('token_name', models.CharField(max_length=50)),
                ('token_address', models.CharField(max_length=50)),
                ('approved_address', models.CharField(max_length=50)),
                ('approved_name', models.CharField(max_length=50)),
                ('tx', models.CharField(default='', max_length=255)),
                ('network', models.CharField(default='', max_length=255)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='token_approvals', to='dashboard.Profile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]