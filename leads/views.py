from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models.functions import TruncDate
from django.db.models import Count
import requests

# Create your views here.
from .models import Lead
from .serializers import LeadSerializer

class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.order_by("-created_at")
    serializer_class = LeadSerializer

    @action(detail=False, methods=["post"])
    def import_from_jsonplaceholder(self, request):
        """Example third-party API integration:
           Pull users from JSONPlaceholder and upsert as leads.
        """
        try:
            r = requests.get("https://jsonplaceholder.typicode.com/users", timeout=20)
            r.raise_for_status()
            added = 0
            for u in r.json():
                name = u.get("name")
                email = u.get("email")
                if not email:
                    continue
                obj, created = Lead.objects.get_or_create(email=email, defaults={"name": name, "source": "api"})
                if created:
                    added += 1
            return Response({ "status": "ok", "added": added })
        except Exception as e:
            return Response({ "status": "error", "detail": str(e) }, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["get"])
    def metrics_by_day(self, request):
        """Reporting endpoint: returns counts grouped by day & source for the dashboard."""
        qs = (
            Lead.objects
            .annotate(day=TruncDate("created_at"))
            .values("day", "source")
            .annotate(count=Count("id"))
            .order_by("day", "source")
        )
        return Response(list(qs))
