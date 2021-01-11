# Generated by Django 3.1.5 on 2021-01-07 17:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Total', models.IntegerField(default=0)),
                ('Created_At', models.DateField(auto_now_add=True, null=True)),
                ('Updated_At', models.DateField(auto_now=True, null=True)),
                ('Status', models.PositiveSmallIntegerField(choices=[('new', 'New'), ('paid', 'Paid')], default=1)),
                ('Mode_of_payment', models.PositiveSmallIntegerField(choices=[('cash', 'Cash_OnDelivery'), ('paytm', 'Paytm_bank'), ('card', 'creditcard/debitcard')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=30)),
                ('Description', models.CharField(max_length=150)),
                ('ImageLink', models.ImageField(upload_to='')),
                ('Price', models.FloatField()),
                ('Created_At', models.DateField(auto_now_add=True, null=True)),
                ('Updated_At', models.DateField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField(default=1)),
                ('Price', models.FloatField(default=0)),
                ('OrderId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cartapp.order')),
                ('ProductId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cartapp.product')),
                ('UserId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='ProductId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cartapp.product'),
        ),
        migrations.AddField(
            model_name='order',
            name='UserId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]