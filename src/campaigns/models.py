from letterbox.models import BaseModel
from django.db import models
from letterbox.fields import IdentifierField
from letterbox.utils.random import generate_random_id


def generate_name_campaign():
    return generate_random_id('CP')


class Campaign(BaseModel):
    CLASSIC = 'classic'
    HTML_CODE = 'code'
    TEXT = 'text'
    CAMPAIGN_TYPE_CHOICES = (
        (CLASSIC, 'Classic'),
        (HTML_CODE, 'HTML code'),
        (TEXT, 'Rich Text'),
    )

    company = models.ForeignKey(
        'users.Company', on_delete=models.SET_NULL, null=True)
    identifier = IdentifierField(default=generate_name_campaign)
    title = models.CharField(max_length=255)
    thumbnail = models.ImageField(blank=True, null=True)
    subject = models.CharField(max_length=150, null=True)
    preview_line = models.CharField(max_length=150, null=True)
    campaign_type = models.CharField(
        max_length=20, choices=CAMPAIGN_TYPE_CHOICES, default=TEXT)
    is_template = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title

    @property
    def contents(self):
        return CampaignContent.objects.filter(campaign=self).order_by('index')


class CampaignContent(BaseModel):
    TITLE = 'title'
    PARAGRAPH = 'paragraph'
    SINGLE_IMAGE = 'single_img'
    MULTIPLE_IMAGE = 'multiple_img'
    CONTENT_WITH_IMAGE = 'content_img'
    NAVIGATION = 'navigation'
    SPACE = 'space'
    DIVIDER = 'divider'
    SOCIAL_LINKS = 'social_links'
    BUTTON = 'button'

    CONTENT_TYPE_CHOICES = (
        (TITLE, 'Title'),
        (PARAGRAPH, 'Paragraph'),
        (SINGLE_IMAGE, 'Single Image'),
        (MULTIPLE_IMAGE, 'Multiple Image'),
        (CONTENT_WITH_IMAGE, 'Content with Image'),
        (NAVIGATION, 'Navigation'),
        (SPACE, 'Space'),
        (DIVIDER, 'Divider'),
        (SOCIAL_LINKS, 'Social Links'),
        (BUTTON, 'Button'),
    )

    index = models.IntegerField()
    campaign = models.ForeignKey(
        'campaigns.Campaign', on_delete=models.CASCADE)
    content_type = models.CharField(
        max_length=20, choices=CONTENT_TYPE_CHOICES)
    text = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    def __str__(self) -> str:
        return f'{str(self.campaign)} - {self.content_type}'

    @property
    def image_type(self):
        if self.content_type == self.SINGLE_IMAGE \
                or self.content_type == self.MULTIPLE_IMAGE \
                or self.content_type == self.CONTENT_WITH_IMAGE:
            return True
        return False

    @property
    def images(self):
        return ContentImage.objects.filter(content=self)

    @property
    def styles(self):
        return ContentStyle.objects.filter(content=self)

    @property
    def social_links(self):
        return ContentSocialLink.objects.filter(content=self)


class ContentImage(BaseModel):
    content = models.ForeignKey(
        'campaigns.CampaignContent', on_delete=models.CASCADE)
    image = models.ImageField()
    alt_text = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField(blank=True)


class ContentStyle(BaseModel):
    BACKGROUND = 'background'
    BORDER_WIDTH = 'border-width'
    BORDER_STYLE = 'border-style'
    BORDER_COLOR = 'border-color'
    BORDER_RADIUS = 'border-radius'
    COLOR = 'color'
    HEIGHT = 'height'
    WIDTH = 'width'
    PADDING = 'padding'
    MARGIN = 'margin'
    FONT_SIZE = 'font-size'

    STYLE_TYPE_CHOICES = (
        (BACKGROUND, 'Background'),
        (BORDER_WIDTH, 'Border Width'),
        (BORDER_STYLE, 'Border Style'),
        (BORDER_COLOR, 'Border Color'),
        (BORDER_RADIUS, 'Border Radius'),
        (COLOR, 'Color'),
        (HEIGHT, 'Height'),
        (WIDTH, 'Width'),
        (PADDING, 'Padding'),
        (MARGIN, 'Margin'),
        (FONT_SIZE, 'Font Size'),
    )

    content = models.ForeignKey(
        'campaigns.CampaignContent', on_delete=models.CASCADE)
    style_type = models.CharField(max_length=100, choices=STYLE_TYPE_CHOICES)
    style_value = models.CharField(max_length=255)


class ContentSocialLink(BaseModel):
    FACEBOOK = 'facebook'
    TWITTER = 'twitter'
    INSTAGRAM = 'instagram'
    LINKEDIN = 'linkedin'
    WHATSAPP = 'whatsapp'
    WEBSITE = 'website'
    EMAIL = 'email'

    SOCIAL_TYPE_CHOICES = (
        (FACEBOOK, 'Facebook'),
        (TWITTER, 'Twitter'),
        (INSTAGRAM, 'Instagram'),
        (LINKEDIN, 'LinkedIN'),
        (WHATSAPP, 'WhatsApp'),
        (WEBSITE, 'Website'),
        (EMAIL, 'Email'),
    )

    content = models.ForeignKey(
        'campaigns.CampaignContent', on_delete=models.CASCADE)
    social_type = models.CharField(max_length=30, choices=SOCIAL_TYPE_CHOICES)
    url = models.URLField()
