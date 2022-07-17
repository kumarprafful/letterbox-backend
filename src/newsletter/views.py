
from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from letterbox.pagination import CursorPagination
from newsletter.models import Genre, Newsletter
from newsletter.serializers import GenreSerializer, NewsletterSerializer


class GenreViewSet(viewsets.ModelViewSet):
    lookup_field = "identifier"
    permission_classes = [IsAuthenticated]
    serializer_class = GenreSerializer

    def get_queryset(self):
        return Genre.objects.all()


class NewsletterViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    pagination_class = CursorPagination
    lookup_field = "name"
    model = Newsletter
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
