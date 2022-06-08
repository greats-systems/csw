# Generated by Django 4.0.4 on 2022-06-03 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csw', '0002_alter_csw_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='csw',
            name='description',
        ),
        migrations.AddField(
            model_name='csw',
            name='Gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=20, null=True, verbose_name='Gender'),
        ),
        migrations.AddField(
            model_name='csw',
            name='city',
            field=models.CharField(max_length=70, null=True, verbose_name='Town/City Of Birth'),
        ),
        migrations.AddField(
            model_name='csw',
            name='country_of_birth',
            field=models.CharField(max_length=80, null=True, verbose_name='Country Of Birth'),
        ),
        migrations.AddField(
            model_name='csw',
            name='date_of_birth',
            field=models.DateField(null=True, verbose_name='Date of Birth'),
        ),
        migrations.AddField(
            model_name='csw',
            name='first_name',
            field=models.CharField(max_length=50, null=True, verbose_name='First Name'),
        ),
        migrations.AddField(
            model_name='csw',
            name='national_id_number',
            field=models.CharField(max_length=40, null=True, verbose_name='National ID Number'),
        ),
        migrations.AddField(
            model_name='csw',
            name='nationality',
            field=models.CharField(max_length=50, null=True, verbose_name='Nationality'),
        ),
        migrations.AddField(
            model_name='csw',
            name='surname',
            field=models.CharField(max_length=70, null=True, verbose_name='Surname'),
        ),
        migrations.AlterField(
            model_name='csw',
            name='title',
            field=models.CharField(choices=[(1, 'Mr'), (2, 'Mrs'), (3, 'Miss'), (4, 'Other')], max_length=20, null=True, verbose_name='Title'),
        ),
    ]