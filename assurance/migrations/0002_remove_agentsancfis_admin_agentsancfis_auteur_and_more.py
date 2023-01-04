# Generated by Django 4.1.3 on 2023-01-04 17:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('assurance', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agentsancfis',
            name='admin',
        ),
        migrations.AddField(
            model_name='agentsancfis',
            name='auteur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='auteur', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='agentassurance',
            name='assurance',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='agentcs',
            name='cs',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='agentlaboratoire',
            name='laboratoire',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='agentpharmacie',
            name='pharmacie',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='assurance',
            name='agent_sancfis',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='assure',
            name='agent_assurance',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='centredesoins',
            name='agent_sancfis',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='laboratoire',
            name='agent_sancfis',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='pharmacie',
            name='agent_sancfis',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='policeassurance',
            name='agent_assurance',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='souscripteur',
            name='agent_assurance',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
