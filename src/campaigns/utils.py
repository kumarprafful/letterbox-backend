from campaigns.models import CampaignContent, ContentStyle


def manage_content_after_creation(content):
    if content.content_type == CampaignContent.TITLE:
        pass
    if content.content_type == CampaignContent.PARAGRAPH:
        pass
    if content.content_type == CampaignContent.SINGLE_IMAGE:
        pass
    if content.content_type == CampaignContent.MULTIPLE_IMAGE:
        pass
    if content.content_type == CampaignContent.CONTENT_WITH_IMAGE:
        pass
    if content.content_type == CampaignContent.NAVIGATION:
        pass
    if content.content_type == CampaignContent.SPACE:
        ContentStyle.objects.create(
            content=content, style_type=ContentStyle.HEIGHT, style_value='50px')
        return
    if content.content_type == CampaignContent.DIVIDER:
        ContentStyle.objects.create(
            content=content, style_type=ContentStyle.BORDER_WIDTH, style_value='1px')
        ContentStyle.objects.create(
            content=content, style_type=ContentStyle.BORDER_STYLE, style_value='solid')
        ContentStyle.objects.create(
            content=content, style_type=ContentStyle.BORDER_COLOR, style_value='#bfbfbf')
        return
    if content.content_type == CampaignContent.SOCIAL_LINKS:
        pass
    if content.content_type == CampaignContent.BUTTON:
        ContentStyle.objects.create(
            content=content, style_type=ContentStyle.BACKGROUND, style_value='#000')
        ContentStyle.objects.create(
            content=content, style_type=ContentStyle.COLOR, style_value='#fff')
        ContentStyle.objects.create(
            content=content, style_type=ContentStyle.FONT_SIZE, style_value='16px')
        ContentStyle.objects.create(
            content=content, style_type=ContentStyle.PADDING, style_value='10px 20px')
        return
    return
