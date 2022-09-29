# Generated by Django 4.1.1 on 2022-09-29 18:12

from django.db import migrations, models
import paste_image.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', paste_image.fields.PasteImageField(blank=True, upload_to='pasted_images/')),
            ],
        ),
    ]
