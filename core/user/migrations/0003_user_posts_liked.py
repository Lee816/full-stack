# Generated by Django 4.2.5 on 2023-09-13 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_post', '0002_alter_post_table'),
        ('core_user', '0002_user_avatar_user_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='posts_liked',
            field=models.ManyToManyField(related_name='liked_by', to='core_post.post'),
        ),
    ]
