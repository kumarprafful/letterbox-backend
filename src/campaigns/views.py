from letterbox.pagination import CursorPagination
from rest_framework import viewsets
from rest_framework.decorators import (api_view, parser_classes,
                                       permission_classes)
from rest_framework.exceptions import ValidationError
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from campaigns.models import Campaign, CampaignContent
from campaigns.serializers import (CampaignContentCreateSerializer, CampaignContentEditSerializer,
                                   CampaignContentSerializer,
                                   CampaignCreateSerializer,
                                   CampaignSerializer)


class CampaignViewSet(viewsets.ModelViewSet):
    # serializer_class = CampaignSerializer
    permission_classes = [IsAuthenticated, ]
    pagination_class = CursorPagination
    lookup_field = 'identifier'
    model = Campaign
    serializer_classes = {
        # 'list': serializers.ListaGruppi,
        # 'retrieve': serializers.DettaglioGruppi,
        'create': CampaignCreateSerializer
    }
    default_serializer_class = CampaignSerializer

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_queryset(self):
        company = self.request.user.company
        campaigns = Campaign.objects.filter(company=company)
        return campaigns

    def create(self, request, *args, **kwargs):
        data = request.data
        data['company'] = request.user.company.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {'identifier': serializer.data['identifier']}
        return Response(response, status=201)


class ContentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    # pagination_class = CursorPagination
    # lookup_field = 'identifier'
    model = CampaignContent
    serializer_classes = {
        'update': CampaignContentEditSerializer,
        'create': CampaignContentCreateSerializer
    }
    default_serializer_class = CampaignContentSerializer

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_queryset(self):
        # figure out better way
        company = self.request.user.company
        try:
            campaign_id = self.request.query_params['campaign_id']
        except KeyError:
            raise ValidationError('campaign_id is required')
        try:
            campaign = Campaign.objects.get(
                identifier=campaign_id, company=company)
        except Campaign.DoesNotExist:
            raise ValidationError('Campaign not found')
        return campaign.contents

    def create(self, request, *args, **kwargs):
        data = request.data
        campaign = Campaign.objects.get(
            identifier=data['campaign'], company=request.user.company)
        data['campaign'] = campaign.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        content = serializer.save()
        data = CampaignContentSerializer(content).data
        return Response(data, status=201)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([JSONParser])
def set_sequence_of_contents(request):
    # move this to ContentViewSet
    data = request.data
    indexes = data['indexes']
    campaign_name = data['campaign_name']
    campaign = Campaign.objects.get(
        identifier=campaign_name, company=request.user.company)
    contents = campaign.contents

    for index, campaign_id in enumerate(indexes):
        contents.filter(id=campaign_id).update(index=index)
    return Response(status=200)
