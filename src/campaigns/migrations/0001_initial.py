# Generated by Django 3.1 on 2021-12-13 19:33

import campaigns.models
from django.db import migrations, models
import django.db.models.deletion
import letterbox.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', letterbox.fields.IdentifierField(default=campaigns.models.generate_name_campaign, help_text='internal name', max_length=255, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='')),
                ('subject', models.CharField(max_length=150, null=True)),
                ('preview_line', models.CharField(max_length=150, null=True)),
                ('campaign_type', models.CharField(choices=[('classic', 'Classic'), ('code', 'HTML code'), ('text', 'Rich Text')], default='text', max_length=20)),
                ('is_template', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CampaignContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('index', models.IntegerField()),
                ('content_type', models.CharField(choices=[('title', 'Title'), ('paragraph', 'Paragraph'), ('single_img', 'Single Image'), ('multiple_img', 'Multiple Image'), ('content_img', 'Content with Image'), ('navigation', 'Navigation'), ('space', 'Space'), ('divider', 'Divider'), ('social_links', 'Social Links'), ('button', 'Button')], max_length=20)),
                ('text', models.TextField(blank=True, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campaigns.campaign')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContentStyle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('style_type', models.CharField(choices=[('background', 'Background'), ('border-width', 'Border Width'), ('border-style', 'Border Style'), ('border-color', 'Border Color'), ('border-radius', 'Border Radius'), ('color', 'Color'), ('height', 'Height'), ('width', 'Width'), ('padding', 'Padding'), ('margin', 'Margin'), ('font-size', 'Font Size')], max_length=100)),
                ('style_value', models.CharField(max_length=255)),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campaigns.campaigncontent')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContentSocialLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('social_type', models.CharField(choices=[('facebook', 'Facebook'), ('twitter', 'Twitter'), ('instagram', 'Instagram'), ('linkedin', 'LinkedIN'), ('whatsapp', 'WhatsApp'), ('website', 'Website'), ('email', 'Email')], max_length=30)),
                ('url', models.URLField()),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campaigns.campaigncontent')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContentImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='')),
                ('alt_text', models.CharField(blank=True, max_length=100, null=True)),
                ('url', models.URLField(blank=True)),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campaigns.campaigncontent')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
