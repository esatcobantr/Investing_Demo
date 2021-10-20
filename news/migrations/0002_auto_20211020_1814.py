# Generated by Django 3.2.7 on 2021-10-20 18:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorymodel',
            name='user',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categoryuser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='newsmodel',
            name='image',
            field=models.ImageField(null=True, upload_to='news'),
        ),
        migrations.AlterField(
            model_name='commentmodel',
            name='user',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='commentuser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='user',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='newsuser', to=settings.AUTH_USER_MODEL),
        ),
    ]