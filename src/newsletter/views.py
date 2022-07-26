
from campaigns.serializers import CampaignCreateSerializer
from letterbox.pagination import CursorPagination
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from newsletter.models import Genre, Newsletter, NewsletterCampaign
from newsletter.serializers import (GenreSerializer,
                                    NewsletterCampaignSerializer,
                                    NewsletterCampaignWriteSerializer,
                                    NewsletterSerializer)


class GenreViewSet(viewsets.ModelViewSet):
    lookup_field = "identifier"
    permission_classes = [IsAuthenticated]
    serializer_class = GenreSerializer

    def get_queryset(self):
        return Genre.objects.all()


class NewsletterViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    pagination_class = CursorPagination
    lookup_field = "identifier"
    serializer_classes = {
        # "list": serializers.ListaGruppi,
        # "retrieve": serializers.DettaglioGruppi,
        "create": NewsletterSerializer
    }
    default_serializer_class = NewsletterSerializer

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_queryset(self):
        company = self.request.user.company
        return Newsletter.objects.filter(company=company)

    def create(self, request, *args, **kwargs):
        data = request.data
        company = request.user.company
        if company.has_newsletter:
            return Response({"status": "newsletter_exists"}, status=400)
        data["company"] = company.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=201)


class NewsletterCampaignViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    pagination_class = CursorPagination
    lookup_field = 'id'

    serializer_classes = {
        # "list": serializers.ListaGruppi,
        # "retrieve": serializers.DettaglioGruppi,
        'create': NewsletterCampaignWriteSerializer
    }
    default_serializer_class = NewsletterCampaignSerializer

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_queryset(self):
        company = self.request.user.company
        newsletter_id = self.request.query_params.get('newsletter_id')

        qs = NewsletterCampaign.objects.filter(newsletter__company=company)

        if newsletter_id:
            try:
                newsletter = Newsletter.objects.get(
                    company=company, identifier=newsletter_id)
            except Newsletter.DoesNotExist:
                return qs.none()
            return qs.filter(newsletter=newsletter)
        return qs

    def create(self, request, *args, **Kwargs):
        company = request.user.company
        data = request.data
        print(data)

        newsletter_id = data.pop('newsletter_id')
        letter_data = data.pop('letter')
        letter_data['company'] = company.id
        if newsletter_id is None:
            return Response({'message': 'newsletter_id is required'}, status=400)
        try:
            newsletter = Newsletter.objects.get(
                identifier=newsletter_id, company=company)
        except Newsletter.DoesNotExist:
            return Response({'message': 'newsletter not found'}, status=400)

        campaign = CampaignCreateSerializer(data=letter_data)
        campaign.is_valid(raise_exception=True)
        campaign = campaign.save()
        newsletter.letters.add(campaign)
        return Response({'identifier': campaign.identifier}, status=201)
