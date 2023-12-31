# Generated by Django 4.2.7 on 2023-11-29 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id_account', models.AutoField(primary_key=True, serialize=False)),
                ('email_account', models.CharField(max_length=45, unique=True)),
                ('password_account', models.CharField(max_length=255)),
                ('dateregister_account', models.DateTimeField(auto_now_add=True)),
                ('dateupdate_account', models.DateTimeField(auto_now=True)),
                ('isadmin_account', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'account',
                'managed': True,
            },
        ),
    ]
