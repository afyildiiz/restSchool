from rest_framework import status
from rest_framework.response import Response #redirect, render
from rest_framework.decorators import api_view

from ogrenci.models import Ogrenci
from  ogrenci.api.serializers import OgrenciSerializer

from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView

# 'API VIEW' CLASS BASED

class OgrenciApiView(APIView):
    def get(self,request):
        # VERIYI CEK, SERIALIZE ET VE DÖNDÜR

        ogrenciler = Ogrenci.objects.filter(still_student=True)
        seriliazer= OgrenciSerializer(ogrenciler,many=True)
        return Response(seriliazer.data)
    
    def post(self,request):
        # GIRILEN VERIYI SERIALIZE ET, GECERLIYSE KAYDET VE MESAJ DONDUR

        serializer = OgrenciSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class OgrenciDetailView(APIView):
    def get_object(self,pk):
        ogrenci_instance = get_object_or_404(Ogrenci,pk=pk)
        return ogrenci_instance
    
    def get(self,request,pk):
        ogrenci = self.get_object(pk=pk)
        serializer=OgrenciSerializer(ogrenci)
        return Response(serializer.data)

    def put(self,request,pk):
        # POST'UN AYNISI sadece gonderecegimiz veriyi (request.data) kullanarak serializer olustururuz 
        ogrenci = self.get_object(pk=pk)
        serializer = OgrenciSerializer(ogrenci,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        ogrenci= self.get_object(pk=pk)
        ogrenci.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# FUNCTION BASED VIEWS

    
# @api_view(['GET','PUT','DELETE'])
# def api_detail(request,pk):
#     try:
#         ogrenciInstance = Ogrenci.objects.get(pk=pk)
#     except Ogrenci.DoesNotExist:
#         return Response(
#             {
#                 'errors':{
#                     'code':404,
#                     'message': f'not found object with this id ({pk})'
#                 }
#             },
#             status=status.HTTP_404_NOT_FOUND
#         )
        
        
#     if request.method=='GET':
#         serializer = OgrenciSerializer(ogrenciInstance)
#         return Response(serializer.data)
    
    
    # elif request.method=='PUT':
    #     seriliazer=OgrenciSerializer(ogrenciInstance,data=request.data) # OGRENCI OBJEMIZ VE GELEN DATAYI KOYDUK.
    #     if seriliazer.is_valid():
    #         seriliazer.save()
    #         return Response(seriliazer.data,status=status.HTTP_201_CREATED)
    #     return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
    # elif request.method=='DELETE':
    #     ogrenciInstance.delete()
    #     return Response(
    #                     {
    #             'errors':{
    #                 'code':204,
    #                 'message': f'deleted object id ({pk})'
    #             }
    #         },
    #         status=status.HTTP_204_NO_CONTENT
    #     )
    
    
    
    # @api_view(['GET','POST'])
# def api_list(request):
    
#     if request.method=='GET':
#         ogrenciler = Ogrenci.objects.filter(still_student=True)
#         seriliazer= OgrenciSerializer(ogrenciler,many=True)
#         return Response(seriliazer.data)
#     elif request.method=='POST':
#         seriliazer=OgrenciSerializer(data=request.data)
#         if seriliazer.is_valid():
#             seriliazer.save()
#             return Response(seriliazer.data,status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
    