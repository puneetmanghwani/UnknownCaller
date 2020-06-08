from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated
from caller.models import SpamDetail


class MarkSpamView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request,pk, format=None):

        # Check if Number Already exist then increase the spam count otherwise create that number with spam count initialized by 1.s
        try:
            PhoneNumber=SpamDetail.objects.get(phone_no=pk)
            PhoneNumber.spam_count+=1
            PhoneNumber.save()
            return Response(status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            PhoneNumber=SpamDetail(phone_no=pk,spam_count=1)
            PhoneNumber.save()
            return Response(status=status.HTTP_200_OK)

        
        