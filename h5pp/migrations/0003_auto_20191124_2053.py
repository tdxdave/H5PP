# Generated by Django 2.2.7 on 2019-11-24 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('h5pp', '0002_auto_20170608_0830'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='h5p_contents',
            options={'ordering': ['title', 'author', 'content_id'], 'verbose_name': 'Content', 'verbose_name_plural': 'Contents'},
        ),
        migrations.AlterModelOptions(
            name='h5p_events',
            options={'ordering': ['created_at', 'type', 'sub_type'], 'verbose_name': 'Event', 'verbose_name_plural': 'Events'},
        ),
        migrations.AlterModelOptions(
            name='h5p_libraries',
            options={'ordering': ['machine_name', 'major_version', 'minor_version'], 'verbose_name': 'Library', 'verbose_name_plural': 'Libraries'},
        ),
        migrations.AlterModelOptions(
            name='h5p_libraries_languages',
            options={'ordering': ['language_code', 'library_id'], 'verbose_name': 'Library-language', 'verbose_name_plural': 'Libraries-languages'},
        ),
        migrations.AlterModelOptions(
            name='h5p_points',
            options={'ordering': ['content_id', 'uid'], 'verbose_name': 'Score', 'verbose_name_plural': 'Scores'},
        ),
        migrations.AlterField(
            model_name='h5p_contents',
            name='content_id',
            field=models.AutoField(help_text='Identifier of the content', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='h5p_contents',
            name='content_type',
            field=models.CharField(help_text='Content type as defined in h5p.json', max_length=127, null=True),
        ),
        migrations.AlterField(
            model_name='h5p_contents',
            name='filtered',
            field=models.TextField(help_text='Filtered version of json_contents'),
        ),
        migrations.AlterField(
            model_name='h5p_contents',
            name='json_contents',
            field=models.TextField(help_text='The content in JSON format'),
        ),
        migrations.AlterField(
            model_name='h5p_contents',
            name='license',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='h5p_contents',
            name='main_library_id',
            field=models.PositiveIntegerField(help_text='The library we first instanciate for this content'),
        ),
        migrations.AlterField(
            model_name='h5p_contents',
            name='meta_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='h5p_contents',
            name='meta_keywords',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='h5p_contents',
            name='slug',
            field=models.CharField(help_text='Human readable content identifier that is unique', max_length=127),
        ),
        migrations.AlterField(
            model_name='h5p_events',
            name='content_id',
            field=models.PositiveIntegerField(help_text='If not 0, identifier of the content affected by this event'),
        ),
        migrations.AlterField(
            model_name='h5p_events',
            name='content_title',
            field=models.CharField(help_text='If not blank, title of the content affected by this event', max_length=255),
        ),
        migrations.AlterField(
            model_name='h5p_events',
            name='library_name',
            field=models.CharField(help_text='If not blank, name of the library affected by this event', max_length=127),
        ),
        migrations.AlterField(
            model_name='h5p_events',
            name='library_version',
            field=models.CharField(help_text='If not blank, version of the library affected by this event', max_length=31),
        ),
        migrations.AlterField(
            model_name='h5p_events',
            name='sub_type',
            field=models.CharField(help_text='Action of the event. Example : Create, Delete, Edit...', max_length=63),
        ),
        migrations.AlterField(
            model_name='h5p_events',
            name='type',
            field=models.CharField(help_text='Type of the event. If it concerns a library, a content or a user', max_length=63),
        ),
        migrations.AlterField(
            model_name='h5p_events',
            name='user_id',
            field=models.PositiveIntegerField(help_text='Identifier of the user who caused this event'),
        ),
        migrations.AlterField(
            model_name='h5p_libraries',
            name='drop_library_css',
            field=models.TextField(blank=True, help_text='List of Libraries that should not have CSS included if this library is used', null=True),
        ),
        migrations.AlterField(
            model_name='h5p_libraries',
            name='embed_types',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='h5p_libraries',
            name='fullscreen',
            field=models.PositiveSmallIntegerField(default=0, help_text='Display fullscreen button'),
        ),
        migrations.AlterField(
            model_name='h5p_libraries',
            name='library_id',
            field=models.AutoField(help_text='Identifier of the library', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='h5p_libraries',
            name='machine_name',
            field=models.CharField(default='', help_text='Full name of the library', max_length=127),
        ),
        migrations.AlterField(
            model_name='h5p_libraries',
            name='preloaded_css',
            field=models.TextField(help_text='List of Stylesheet files needed by the library', null=True),
        ),
        migrations.AlterField(
            model_name='h5p_libraries',
            name='preloaded_js',
            field=models.TextField(help_text='List of JavaScript files needed by the library', null=True),
        ),
        migrations.AlterField(
            model_name='h5p_libraries',
            name='restricted',
            field=models.PositiveSmallIntegerField(default=0, help_text='If this library can be used to create new content'),
        ),
        migrations.AlterField(
            model_name='h5p_libraries',
            name='runnable',
            field=models.PositiveSmallIntegerField(default=1, help_text='If the library can be started alone (not a dependency) ?'),
        ),
        migrations.AlterField(
            model_name='h5p_libraries',
            name='semantics',
            field=models.TextField(blank=True, help_text='The semantics definition in JSON format'),
        ),
        migrations.AlterField(
            model_name='h5p_libraries',
            name='title',
            field=models.CharField(default='', help_text='Short name of the library', max_length=255),
        ),
        migrations.AlterField(
            model_name='h5p_libraries',
            name='tutorial_url',
            field=models.CharField(blank=True, help_text='URL to a tutorial for this library', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='h5p_libraries_languages',
            name='language_json',
            field=models.TextField(help_text='The translations defined in json format'),
        ),
        migrations.AlterField(
            model_name='h5p_points',
            name='content_id',
            field=models.PositiveIntegerField(help_text='Identifier of the content having a score'),
        ),
        migrations.AlterField(
            model_name='h5p_points',
            name='finished',
            field=models.PositiveIntegerField(default=0, help_text='Timestamp. Indicates when the user finished watching the video'),
        ),
        migrations.AlterField(
            model_name='h5p_points',
            name='max_points',
            field=models.PositiveIntegerField(blank=True, help_text='Maximum point that the user can have', null=True),
        ),
        migrations.AlterField(
            model_name='h5p_points',
            name='points',
            field=models.PositiveIntegerField(blank=True, help_text='Current point of the user', null=True),
        ),
        migrations.AlterField(
            model_name='h5p_points',
            name='started',
            field=models.PositiveIntegerField(help_text='Timestamp. Indicates when the user started watching the video'),
        ),
        migrations.AlterField(
            model_name='h5p_points',
            name='uid',
            field=models.PositiveIntegerField(help_text='Identifier of the user with this score'),
        ),
    ]
