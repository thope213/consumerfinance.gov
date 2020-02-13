# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-02-12 19:26
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import v1.atomic_elements.organisms
import v1.blocks
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0200_expandable_group_help_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnforcementActionPage',
            fields=[
                ('abstractfilterpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='v1.AbstractFilterPage')),
                ('sidebar_header', models.CharField(default='Action details', max_length=100)),
                ('court', models.CharField(blank=True, default='', max_length=150)),
                ('institution_type', models.CharField(choices=[('Nonbank', 'Nonbank'), ('Bank', 'Bank')], max_length=50, null=True)),
                ('status', models.CharField(choices=[('Post Order/Post Judgment', 'Post Order/Post Judgment'), ('Expired/Terminated/Dismissed', 'Expired/Terminated/Dismissed'), ('Pending Litigation', 'Pending Litigation')], max_length=50, null=True)),
                ('docket_number', models.CharField(max_length=50, null=True)),
                ('content', wagtail.wagtailcore.fields.StreamField((('full_width_text', wagtail.wagtailcore.blocks.StreamBlock((('content', wagtail.wagtailcore.blocks.RichTextBlock(icon='edit')), ('content_with_anchor', wagtail.wagtailcore.blocks.StructBlock((('content_block', wagtail.wagtailcore.blocks.RichTextBlock()), ('anchor_link', wagtail.wagtailcore.blocks.StructBlock((('link_id', wagtail.wagtailcore.blocks.CharBlock(help_text='\n            ID will be auto-generated on save.\n            However, you may enter some human-friendly text that\n            will be incorporated to make it easier to read.\n        ', label='ID for this content block', required=False)),)))))), ('heading', wagtail.wagtailcore.blocks.StructBlock((('text', v1.blocks.HeadingTextBlock(required=False)), ('level', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')])), ('icon', v1.blocks.HeadingIconBlock(help_text='Input the name of an icon to appear to the left of the heading. E.g., approved, help-round, etc. <a href="https://cfpb.github.io/capital-framework/components/cf-icons/#the-icons">See full list of icons</a>', required=False))), required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailcore.blocks.StructBlock((('upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('alt', wagtail.wagtailcore.blocks.CharBlock(help_text="If the image is decorative (i.e., if a screenreader wouldn't have anything useful to say about it), leave the Alt field blank.", required=False))))), ('image_width', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('full', 'full'), (470, '470px'), (270, '270px'), (170, '170px')])), ('image_position', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('right', 'right'), ('left', 'left')], help_text='Does not apply if the image is full-width')), ('text', wagtail.wagtailcore.blocks.RichTextBlock(label='Caption', required=False)), ('is_bottom_rule', wagtail.wagtailcore.blocks.BooleanBlock(default=True, help_text='Check to add a horizontal rule line to bottom of inset.', label='Has bottom rule line', required=False))))), ('table_block', v1.atomic_elements.organisms.AtomicTableBlock(table_options={'renderer': 'html'})), ('quote', wagtail.wagtailcore.blocks.StructBlock((('body', wagtail.wagtailcore.blocks.TextBlock()), ('citation', wagtail.wagtailcore.blocks.TextBlock(required=False)), ('is_large', wagtail.wagtailcore.blocks.BooleanBlock(required=False))))), ('cta', wagtail.wagtailcore.blocks.StructBlock((('slug_text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('paragraph_text', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('button', wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('url', wagtail.wagtailcore.blocks.CharBlock(default='/', required=False)), ('size', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('regular', 'Regular'), ('large', 'Large Primary')])))))))), ('related_links', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('url', wagtail.wagtailcore.blocks.CharBlock(default='/', required=False))))))))), ('reusable_text', v1.blocks.ReusableTextChooserBlock('v1.ReusableText')), ('email_signup', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(default='Stay informed', required=False)), ('default_heading', wagtail.wagtailcore.blocks.BooleanBlock(default=True, help_text='If selected, heading will be styled as an H5 with green top rule. Deselect to style header as H3.', label='Default heading style', required=False)), ('text', wagtail.wagtailcore.blocks.CharBlock(help_text='Write a sentence or two about what kinds of emails the user is signing up for, how frequently they will be sent, etc.', required=False)), ('gd_code', wagtail.wagtailcore.blocks.CharBlock(help_text='Code for the topic (i.e., mailing list) you want people who submit this form to subscribe to. Format: USCFPB_###', label='GovDelivery code', required=False)), ('disclaimer_page', wagtail.wagtailcore.blocks.PageChooserBlock(help_text='Choose the page that the "See Privacy Act statement" link should go to. If in doubt, use "Generic Email Sign-Up Privacy Act Statement".', label='Privacy Act statement', required=False))))), ('well', wagtail.wagtailcore.blocks.StructBlock((('content', wagtail.wagtailcore.blocks.RichTextBlock(label='Well', required=False)),))), ('well_with_ask_search', wagtail.wagtailcore.blocks.StructBlock((('content', wagtail.wagtailcore.blocks.RichTextBlock(label='Well', required=False)), ('ask_search', wagtail.wagtailcore.blocks.StructBlock((('show_label', wagtail.wagtailcore.blocks.BooleanBlock(default=True, help_text='Whether to show form label.', required=False)), ('placeholder', wagtail.wagtailcore.blocks.TextBlock(help_text='Text to show for the input placeholder text.', required=False))))))))))), ('expandable', wagtail.wagtailcore.blocks.StructBlock((('label', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('is_bordered', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), ('is_midtone', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), ('is_expanded', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), ('content', wagtail.wagtailcore.blocks.StreamBlock((('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('well', wagtail.wagtailcore.blocks.StructBlock((('content', wagtail.wagtailcore.blocks.RichTextBlock(label='Well', required=False)),))), ('links', wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('url', wagtail.wagtailcore.blocks.CharBlock(default='/', required=False))))), ('email', wagtail.wagtailcore.blocks.StructBlock((('emails', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('url', wagtail.wagtailcore.blocks.EmailBlock(label='Email address')), ('text', wagtail.wagtailcore.blocks.CharBlock(label='Link text (optional)', required=False)))))),))), ('phone', wagtail.wagtailcore.blocks.StructBlock((('fax', wagtail.wagtailcore.blocks.BooleanBlock(default=False, label='Is this number a fax?', required=False)), ('phones', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('number', wagtail.wagtailcore.blocks.CharBlock(help_text='Do not include spaces or dashes. Ex. 8554112372', max_length=15, validators=[django.core.validators.RegexValidator(message='Enter a numeric phone number, without punctuation.', regex='^\\d*$')])), ('extension', wagtail.wagtailcore.blocks.CharBlock(max_length=4, required=False)), ('vanity', wagtail.wagtailcore.blocks.CharBlock(help_text='A phoneword version of the above number. Include any formatting. Ex. (555) 222-CFPB', max_length=15, required=False)), ('tty', wagtail.wagtailcore.blocks.CharBlock(help_text='Do not include spaces or dashes. Ex. 8554112372', label='TTY', max_length=15, required=False, validators=[django.core.validators.RegexValidator(message='Enter a numeric phone number, without punctuation.', regex='^\\d*$')])), ('tty_ext', wagtail.wagtailcore.blocks.CharBlock(label='TTY Extension', max_length=4, required=False))))))))), ('address', wagtail.wagtailcore.blocks.StructBlock((('label', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('title', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('street', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('city', wagtail.wagtailcore.blocks.CharBlock(max_length=50, required=False)), ('state', wagtail.wagtailcore.blocks.CharBlock(max_length=25, required=False)), ('zip_code', wagtail.wagtailcore.blocks.CharBlock(max_length=15, required=False)))))), blank=True))))), ('expandable_group', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(help_text='Added as an <code>&lt;h3&gt;</code> at the top of this block. Also adds a wrapping <code>&lt;div&gt;</code> whose <code>id</code> attribute comes from a slugified version of this heading, creating an anchor that can be used when linking to this part of the page.', required=False)), ('body', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('is_accordion', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), ('has_top_rule_line', wagtail.wagtailcore.blocks.BooleanBlock(default=False, help_text='Check this to add a horizontal rule line to top of expandable group.', required=False)), ('expandables', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('label', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('is_bordered', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), ('is_midtone', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), ('is_expanded', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), ('content', wagtail.wagtailcore.blocks.StreamBlock((('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('well', wagtail.wagtailcore.blocks.StructBlock((('content', wagtail.wagtailcore.blocks.RichTextBlock(label='Well', required=False)),))), ('links', wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('url', wagtail.wagtailcore.blocks.CharBlock(default='/', required=False))))), ('email', wagtail.wagtailcore.blocks.StructBlock((('emails', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('url', wagtail.wagtailcore.blocks.EmailBlock(label='Email address')), ('text', wagtail.wagtailcore.blocks.CharBlock(label='Link text (optional)', required=False)))))),))), ('phone', wagtail.wagtailcore.blocks.StructBlock((('fax', wagtail.wagtailcore.blocks.BooleanBlock(default=False, label='Is this number a fax?', required=False)), ('phones', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('number', wagtail.wagtailcore.blocks.CharBlock(help_text='Do not include spaces or dashes. Ex. 8554112372', max_length=15, validators=[django.core.validators.RegexValidator(message='Enter a numeric phone number, without punctuation.', regex='^\\d*$')])), ('extension', wagtail.wagtailcore.blocks.CharBlock(max_length=4, required=False)), ('vanity', wagtail.wagtailcore.blocks.CharBlock(help_text='A phoneword version of the above number. Include any formatting. Ex. (555) 222-CFPB', max_length=15, required=False)), ('tty', wagtail.wagtailcore.blocks.CharBlock(help_text='Do not include spaces or dashes. Ex. 8554112372', label='TTY', max_length=15, required=False, validators=[django.core.validators.RegexValidator(message='Enter a numeric phone number, without punctuation.', regex='^\\d*$')])), ('tty_ext', wagtail.wagtailcore.blocks.CharBlock(label='TTY Extension', max_length=4, required=False))))))))), ('address', wagtail.wagtailcore.blocks.StructBlock((('label', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('title', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('street', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('city', wagtail.wagtailcore.blocks.CharBlock(max_length=50, required=False)), ('state', wagtail.wagtailcore.blocks.CharBlock(max_length=25, required=False)), ('zip_code', wagtail.wagtailcore.blocks.CharBlock(max_length=15, required=False)))))), blank=True))))))))), ('notification', wagtail.wagtailcore.blocks.StructBlock((('message', wagtail.wagtailcore.blocks.CharBlock(help_text='The main notification message to display.', required=True)), ('explanation', wagtail.wagtailcore.blocks.TextBlock(help_text='Explanation text appears below the message in smaller type.', required=False)), ('links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('url', wagtail.wagtailcore.blocks.CharBlock(default='/', required=False)))), help_text='Links appear on their own lines below the explanation.', required=False))))), ('table_block', v1.atomic_elements.organisms.AtomicTableBlock(table_options={'renderer': 'html'})), ('feedback', wagtail.wagtailcore.blocks.StructBlock((('was_it_helpful_text', wagtail.wagtailcore.blocks.CharBlock(default='Was this page helpful to you?', help_text='Use this field only for feedback forms that use "Was this helpful?" radio buttons.', required=False)), ('intro_text', wagtail.wagtailcore.blocks.CharBlock(help_text='Optional feedback intro', required=False)), ('question_text', wagtail.wagtailcore.blocks.CharBlock(help_text='Optional expansion on intro', required=False)), ('radio_intro', wagtail.wagtailcore.blocks.CharBlock(help_text='Leave blank unless you are building a feedback form with extra radio-button prompts, as in /owning-a-home/help-us-improve/.', required=False)), ('radio_text', wagtail.wagtailcore.blocks.CharBlock(default='This information helps us understand your question better.', required=False)), ('radio_question_1', wagtail.wagtailcore.blocks.CharBlock(default='How soon do you expect to buy a home?', required=False)), ('radio_question_2', wagtail.wagtailcore.blocks.CharBlock(default='Do you currently own a home?', required=False)), ('button_text', wagtail.wagtailcore.blocks.CharBlock(default='Submit')), ('contact_advisory', wagtail.wagtailcore.blocks.RichTextBlock(help_text='Use only for feedback forms that ask for a contact email', required=False)))))), blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('v1.abstractfilterpage',),
        ),
    ]
