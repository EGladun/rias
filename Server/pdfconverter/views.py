import os

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework import permissions
from pdfconverter.serializers import UserSerializer, GroupSerializer, FileuploadSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

from .models import Fileupload, File
from .serializers import FileSerializer
import glob
import PyPDF2
from natsort import natsorted


class CreateUserView(CreateModelMixin, GenericViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class FileView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()

            i = (len([name for name in os.listdir('/Users/monst/OneDrive/Рабочий стол/проект/проект/project/media/resulit/.') if os.path.isfile(name)]))
            output_file_path = 'media/resulit/exaple'+str(i)+'.pdf'
            merge_pdf = PyPDF2.PdfFileMerger()
            pdfs = glob.glob("media/*.pdf")
            for pdf in natsorted(pdfs):
                merge_pdf.append(open(pdf, "rb"))

            merge_pdf.write(open(output_file_path, 'wb'))
            uploads = Fileupload()
            uploads.file = output_file_path
            uploads.save()


            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileUpload(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Fileupload.objects.all()
    serializer_class = FileuploadSerializer
