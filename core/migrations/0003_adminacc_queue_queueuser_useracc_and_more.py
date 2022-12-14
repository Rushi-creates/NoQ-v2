# Generated by Django 4.0.3 on 2022-07-27 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_gymtrack_g_uid_delete_attendance_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminAcc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='no value', max_length=256)),
                ('number', models.IntegerField(default=1)),
                ('password', models.CharField(default='no value', max_length=20)),
                ('companyName', models.CharField(default='no value', max_length=100)),
                ('proofOfBiz_link', models.CharField(default='no value', max_length=500)),
                ('category', models.CharField(default='no value', max_length=40)),
                ('loc_firstLine', models.CharField(default='no value', max_length=200)),
                ('loc_secondLine', models.CharField(default='no value', max_length=200)),
                ('loc_pincode', models.IntegerField(default=1)),
                ('isAgreementAccpeted', models.BooleanField(default=False)),
                ('isAdminVerified', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('description', models.CharField(max_length=80)),
                ('setMaxPeople', models.IntegerField(default=1000)),
                ('isOpen', models.BooleanField(default=True)),
                ('adminAcc_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='adminAccFk_in_queue', to='core.adminacc')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='QueueUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('queue_name', models.CharField(default='no value', max_length=80)),
                ('userAcc_name', models.CharField(default='no value', max_length=80)),
                ('shopAdmin_name', models.CharField(default='no value', max_length=80)),
                ('joinedTime', models.CharField(max_length=20)),
                ('queue_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='queueFk_in_queueUser', to='core.queue')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='UserAcc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='no value', max_length=256)),
                ('number', models.IntegerField(default=1)),
                ('password', models.CharField(default='no value', max_length=50)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.RemoveField(
            model_name='memberprofile',
            name='m_uid',
        ),
        migrations.DeleteModel(
            name='AuthUser',
        ),
        migrations.DeleteModel(
            name='MemberProfile',
        ),
        migrations.AddField(
            model_name='queueuser',
            name='userAcc_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userAccFk_in_queueUser', to='core.useracc'),
        ),
    ]
