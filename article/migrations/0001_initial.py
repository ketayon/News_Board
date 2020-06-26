# Generated by Django 3.0.7 on 2020-06-25 11:53

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
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('link', models.URLField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('amount_of_upvotes', models.IntegerField(default=0)),
                ('author_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_msgs', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-creation_date',),
            },
        ),
    ]