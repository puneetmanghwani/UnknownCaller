from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from caller.models import SpamDetail,ContactDetail
from users.models import CustomUser
from users.serializers import UserSerializer
from caller.serializers import SearchSerializer,DetailSerializer
import json
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


class SearchView(ListAPIView):
    model = CustomUser
    serializer_class = SearchSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):

        # If name is given in search.
        if self.request.query_params.get('name',None):

            name=self.request.query_params.get('name',None)

            # Filtering users based on name start with search query.
            queryset = CustomUser.objects.filter(full_name__istartswith=name)
        
            # Filtering users whoom name contains search query.
            queryset |=CustomUser.objects.filter(full_name__icontains=name)

            users=[]

            # Taking each search result and adding its spam count in the object.
            for obj in queryset:
                try:
                    spam_count=SpamDetail.objects.get(phone_no=obj.phone_no).spam_count
                    setattr(obj, 'spam_count', spam_count)
                    users.append(obj)
                except ObjectDoesNotExist:
                    setattr(obj, 'spam_count', 0)
                    users.append(obj)
            # returning the list of users.
            return users
        
        # If phone number is given in search.
        elif self.request.query_params.get('phone_no',None):
            users=[]
            phone_no=self.request.query_params.get('phone_no',None)

            # Finding the phone number in registered users database.
            queryset=CustomUser.objects.filter(phone_no=phone_no)

            # If no such user exist find in Contact table of all registered user.
            if not queryset.exists():
                 queryset=ContactDetail.objects.filter(phone_no=phone_no)
            
            # Add spam count for each search result.
            for obj in queryset:
                try:
                    spam_count=SpamDetail.objects.get(phone_no=obj.phone_no).spam_count
                    setattr(obj, 'spam_count', spam_count)
                    users.append(obj)
                except ObjectDoesNotExist:
                    setattr(obj, 'spam_count', 0)
                    users.append(obj)
            return users
        
class DetailView(APIView):
    serializer_class = DetailSerializer
    permission_classes = [IsAuthenticated]

    # Receiving User data in POST request.
    def post(self, request, format=None):

        # Getting Details
        # currentUserId is the user who is searching
        currentUserId=request.data.get("user_id",None)
        contact_id=request.data.get("contact_id",None)
        full_name=request.data.get("full_name",None)
        phone_no=request.data.get("phone_no",None)
        spam_count=request.data.get("spam_count",None)
        
        # Dictionary without email
        user={
            'full_name':full_name,
            'phone_no':phone_no,
            'spam_count':spam_count
        }

        # Checking the user is registered and the user who is searching is in the person’s contact list then append the email in dictionary.
        try:
            registeredUser=CustomUser.objects.get(phone_no=phone_no)

            registeredUserId=registeredUser.id

            currentUserNumber=CustomUser.objects.get(pk=currentUserId).phone_no

            registeredUserContacts=ContactDetail.objects.filter(user_id=registeredUserId)

            registeredUserContactsNumbers=[ UserContact.phone_no for UserContact in registeredUserContacts ]

            # If user's number who is searching exist in contacts
            if currentUserNumber in registeredUserContactsNumbers:
                user['email']=registeredUser.email

        except ObjectDoesNotExist:
            pass

        # Returning the dictionary in json.                                                                                                                                                                                                                                                                                                                                    #   
        return JsonResponse(user)  
        
        
