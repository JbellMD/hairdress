import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hairdresser',
            fields=[
                ('hairdresser_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('service_id', models.AutoField(primary_key=True, serialize=False)),
                ('service_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('duration', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('appointment_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_datetime', models.DateTimeField()),
                ('end_datetime', models.DateTimeField()),
                ('customer_contact', models.TextField()),
                ('hairdresser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointments.hairdresser')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointments.service')),
            ],
        ),
    ]

