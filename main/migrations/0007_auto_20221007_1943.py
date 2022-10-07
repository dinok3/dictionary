# Generated by Django 3.2.16 on 2022-10-07 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_lexicalentrie_audio_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inflection',
            name='lexical_entrie',
        ),
        migrations.RemoveField(
            model_name='lexicalentrie',
            name='result',
        ),
        migrations.RemoveField(
            model_name='notes',
            name='lexical_entrie',
        ),
        migrations.RemoveField(
            model_name='phrasalverbs',
            name='lexical_entrie',
        ),
        migrations.RemoveField(
            model_name='phrases',
            name='lexical_entrie',
        ),
        migrations.RemoveField(
            model_name='results',
            name='word',
        ),
        migrations.RemoveField(
            model_name='senses',
            name='lexical_entrie',
        ),
        migrations.RemoveField(
            model_name='subsenseexamples',
            name='subsense',
        ),
        migrations.RemoveField(
            model_name='subsenses',
            name='sense',
        ),
        migrations.RemoveField(
            model_name='subsensesynonyms',
            name='subsense',
        ),
        migrations.RemoveField(
            model_name='synonyms',
            name='sense',
        ),
        migrations.DeleteModel(
            name='Examples',
        ),
        migrations.DeleteModel(
            name='Inflection',
        ),
        migrations.DeleteModel(
            name='LexicalEntrie',
        ),
        migrations.DeleteModel(
            name='Notes',
        ),
        migrations.DeleteModel(
            name='PhrasalVerbs',
        ),
        migrations.DeleteModel(
            name='Phrases',
        ),
        migrations.DeleteModel(
            name='Results',
        ),
        migrations.DeleteModel(
            name='Senses',
        ),
        migrations.DeleteModel(
            name='SubsenseExamples',
        ),
        migrations.DeleteModel(
            name='Subsenses',
        ),
        migrations.DeleteModel(
            name='SubsenseSynonyms',
        ),
        migrations.DeleteModel(
            name='Synonyms',
        ),
        migrations.DeleteModel(
            name='Word',
        ),
    ]