# Generated by Django 2.0.3 on 2018-03-21 16:39

import django.contrib.postgres.fields
from django.db import migrations, models
import economy.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExternalBounty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('action_url', models.URLField(db_index=True, help_text='Where to send interested parties')),
                ('active', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, default='', help_text='Plainext only please!')),
                ('source_project', models.CharField(help_text='The upstream project being linked it..', max_length=255)),
                ('amount', models.IntegerField(default=1)),
                ('amount_denomination', models.CharField(help_text='ex: ETH, LTC, BTC', max_length=255)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_sync_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, default=[], help_text='comma delimited', size=None)),
                ('github_handle', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]