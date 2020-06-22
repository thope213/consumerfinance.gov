import re

from django import forms
from django.core.exceptions import ValidationError

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


def number_validator(value, search=re.compile(r'[^0-9]').search):
    if value:
        return bool(search(value))
    else:
        return False


def is_required(field_name):
    return [str(field_name) + ' is required.']


class NumberBlock(blocks.StructBlock):
    text = blocks.CharBlock(max_length=100, required=False)

    def __init__(self, required=True):
        self.is_required = required
        super(NumberBlock, self).__init__()

    @property
    def required(self):
        return self.is_required

    def clean(self, data):
        error_dict = {}

        try:
            data = super(NumberBlock, self).clean(data)
        except ValidationError as e:
            error_dict.update(e.params)

        if self.required:
            if not data['text']:
                error_dict.update({'text': is_required('Text')})

        if number_validator(data['text']):
            error_dict.update({'text': ['Must be a numerical value']})

        if error_dict:
            raise ValidationError("NumberBlock validation errors",
                                  params=error_dict)
        else:
            return data

    class Meta:
        icon = 'order'
        template = '_includes/atoms/number.html'


class IntegerBlock(blocks.FieldBlock):
    def __init__(self, required=True, help_text=None, min_value=None,
                 max_value=None, **kwargs):
        self.field = forms.IntegerField(
            required=required,
            help_text=help_text,
            min_value=min_value,
            max_value=max_value
        )
        super(IntegerBlock, self).__init__(**kwargs)

    class Meta:
        icon = 'plus-inverse'


class Hyperlink(blocks.StructBlock):
    text = blocks.CharBlock(required=False)
    url = blocks.CharBlock(default='/', required=False)

    def __init__(self, required=True):
        self.is_required = required
        super(Hyperlink, self).__init__()

    @property
    def required(self):
        return self.is_required

    def clean(self, data):
        error_dict = {}

        try:
            data = super(Hyperlink, self).clean(data)
        except ValidationError as e:
            error_dict.update(e.params)

        if self.required:
            if not data['text']:
                error_dict.update({'text': is_required('Text')})

        if error_dict:
            raise ValidationError("Hyperlink validation errors",
                                  params=error_dict)
        else:
            return data

    class Meta:
        icon = 'link'
        template = '_includes/atoms/hyperlink.html'


class Button(Hyperlink):
    size = blocks.ChoiceBlock(choices=[
        ('regular', 'Regular'),
        ('large', 'Large Primary'),
    ], default='regular')


class ImageBasicStructValue(blocks.StructValue):
    @property
    def url(self):
        upload = self.get('upload')

        if upload:
            return upload.get_rendition('original').url

    @property
    def alt_text(self):
        # TODO: This duplicates the logic in v1.jinja2tags.image_alt_value,
        # which cannot be called here because of a circular import. It would
        # be better to deprecate the image_alt_value tag in favor of using
        # this logic wherever we use ImageBasic atoms.
        alt = self.get('alt')
        if alt:
            return alt

        upload = self.get('upload')
        if upload and upload.alt:
            return upload.alt

        # Deliberately return the empty string. It's better to have an empty
        # alt attribute than to have none at all.
        return ''


class ImageBasic(blocks.StructBlock):
    upload = ImageChooserBlock(required=False)
    alt = blocks.CharBlock(
        required=False,
        help_text='If the image is decorative (i.e., if a screenreader '
                  'wouldn\'t have anything useful to say about it), leave the '
                  'Alt field blank.'
    )

    def __init__(self, required=True):
        self.is_required = required
        super(ImageBasic, self).__init__()

    @property
    def required(self):
        return self.is_required

    def clean(self, data):
        error_dict = {}

        try:
            data = super(ImageBasic, self).clean(data)
        except ValidationError as e:
            error_dict.update(e.params)

        if not self.required and not data['upload']:
            return data

        if not data['upload']:
            error_dict.update({'upload': is_required("Upload")})

        if error_dict:
            raise ValidationError("ImageBasic validation errors",
                                  params=error_dict)
        else:
            return data

    class Meta:
        icon = 'image'
        value_class = ImageBasicStructValue


class ImageBasicUrl(ImageBasic):
    url = blocks.CharBlock(required=False)

    def clean(self, data):
        error_dict = {}

        try:
            data = super(ImageBasicUrl, self).clean(data)
        except ValidationError as e:
            error_dict.update(e.params)

        if not self.required and not data['upload'] and not data['url']:
            return data

        if not data['upload'] and not data['url']:
            img_err = ['Please upload or enter an image path']
            error_dict.update({
                'upload': img_err,
                'url': img_err,
                'alt': is_required('Image alt')
            })

        if data['upload'] and data['url']:
            img_err = ['Please select one method of image rendering']
            error_dict.update({
                'upload': img_err,
                'url': img_err})

        if error_dict:
            raise ValidationError("ImageBasicUrlAlt validation errors",
                                  params=error_dict)
        else:
            return data
