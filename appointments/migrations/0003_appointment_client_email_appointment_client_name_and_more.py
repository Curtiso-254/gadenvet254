# Generated by Django 4.2.11 on 2024-07-18 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_appointment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='client_email',
            field=models.EmailField(default='default@example.com', max_length=254),
        ),
        migrations.AddField(
            model_name='appointment',
            name='client_name',
            field=models.CharField(default='default@gmail.com', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='veterinarian',
            field=models.CharField(default=12, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='price',
            field=models.DecimalField(decimal_places=2, default=100, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('canceled', 'Canceled')], default='pending', max_length=10),
        ),
        migrations.AlterField(
            model_name='service',
            name='duration',
            field=models.DurationField(),
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]