from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Tip
from .serializers import TipSerializer

class TipListView(APIView):
    def get(self, request):
        tips = Tip.objects.all()[:3]  # Get any 3 objects
        serializer = TipSerializer(tips, many=True)
        return Response(serializer.data)
