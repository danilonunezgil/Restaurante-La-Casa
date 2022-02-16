# Generated by Django 3.1.1 on 2022-02-07 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('hide_menu_root', models.BooleanField(default=True, help_text='Defines if the root menu item should be hidden (a menu always have exactly one root menu item).')),
                ('expansion_depth', models.PositiveSmallIntegerField(default=0, help_text='Defines the default expansion level of the menu. Use e.g. 2 to show the first two levels in the menu. A value of 0 shows the entire menu. This field can be overridden by the template.')),
                ('max_depth', models.PositiveSmallIntegerField(default=0, help_text='Defines the maximum number of levels allowed in the menu. A value of 0 means no limits. This field can be overridden by the template.')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('link', models.CharField(blank=True, help_text="Use lower-case letters only. Local links should start with forward slash, and normally ends with slash - eg /science/. Remote links should be full URLs - eg http://www.cnn.com/. The field can be left empty, in which case the menu item won't be linked.", max_length=255)),
                ('published', models.BooleanField(default=True)),
                ('on_click', models.PositiveIntegerField(choices=[(0, 'Same window'), (1, 'New window')], default=0)),
                ('is_primary', models.BooleanField(default=True, help_text='In case a menu contains several items with the same link, set this field to true and the others menu items field to false, to control which item is used for item highlighting and breadcrumb generation.')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('menu', models.ForeignKey(blank=True, help_text='This field only have effect for the root menu item', null=True, on_delete=django.db.models.deletion.CASCADE, to='Menus.menu')),
                ('parent', models.ForeignKey(blank=True, help_text='Moving a node to a new parent, will place it as the last node. When moving a menu item, all of it sub-items will be moved as well.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='Menus.menuitem')),
            ],
            options={
                'ordering': ['tree_id', 'lft'],
            },
        ),
    ]
