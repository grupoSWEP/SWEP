# Generated by Django 4.1.2 on 2022-10-23 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swepApp', '0010_remove_recipe_ingredientes_recipe_ingredientes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='regiao',
            field=models.CharField(choices=[('Norte', 'Norte'), ('Nordeste', 'Nordeste'), ('Centro-Oeste', 'Centro-Oeste'), ('Sul', 'Sul'), ('Sudeste', 'Sudeste')], max_length=15, null=True),
        ),
    ]