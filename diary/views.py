from django.shortcuts import renderfrom rest_framework.response import Responsefrom .models import Diaryfrom django.http import HttpResponse, Http404from rest_framework import statusfrom rest_framework.views import APIViewfrom rest_framework.response import Responsefrom .serializers import DiarySerializerfrom rest_framework import viewsets, permissionsfrom django_filters.rest_framework import DjangoFilterBackendfrom django.http import JsonResponse, HttpResponsefrom rest_framework import viewsets, permissions, statusfrom django_filters.rest_framework import DjangoFilterBackendfrom django.contrib.auth.models import Userimport random, stringfrom django.contrib.auth import login, authenticatefrom rest_framework.authtoken.models import Tokenfrom django.views.decorators.csrf import csrf_exemptimport datetimefrom rest_framework_jwt.authentication import JSONWebTokenAuthenticationfrom NLP.Diary2 import predictfrom rest_framework_jwt.utils import jwt_decode_handlerclass DiaryViewSet(viewsets.ModelViewSet):    permission_classes = (permissions.IsAuthenticated,)    queryset = Diary.objects.all()    serializer_class = DiarySerializer    def get_queryset(self):        user = self.request.user        if user.is_superuser:            return Diary.objects.all()        else:            return Diary.objects.filter(user=user)# , many=True)    def create(self, request, **kwargs):        content = request.data["content"]        user = request.user.id        #여기서 content를 통해 감정도를 넣으면 됌        feeling = 100        serializer = DiarySerializer(data={"content": content, "user": user, "happiness": feeling})        if serializer.is_valid():            serializer.save()            return JsonResponse(serializer.data)        else:            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    def partial_update(self, request, pk):        if pk == "987654321":            content = request.data["content"]            user = request.user.id            # 여기서 content를 통해 감정도를 넣으면 됌            emotions = predict(content)            print("@@@@@@@")            print(emotions)            print("@@@@@@@")            print("슬픔, 중립, 행복, 불안, 분노, 예외 리스트입니다.")            serializer = DiarySerializer(data={"content": content, "user": user, "sadness": emotions[0],                                               "neutrality": emotions[1], "happiness": emotions[2],                                               "worry": emotions[3], "anger": emotions[4]})            if serializer.is_valid():                serializer.save()                return JsonResponse(serializer.data)            else:                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        #model session error로 인한 임시 method        elif pk == "999999999":            content = request.data["content"]            user = request.user.id            serializer = DiarySerializer(data={"content": content, "user": user, "sadness": 0,                                               "neutrality": 0, "happiness": 1,                                               "worry": 0, "anger": 0})            if serializer.is_valid():                serializer.save()                return JsonResponse(serializer.data)            else:                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        else:            content = request.data["content"]            user = request.user.id            emotions = predict(content)            diary = Diary.objects.filter(id=pk)            diary.update(content=content, sadness=emotions[0], neutrality=emotions[1], happiness=emotions[2],                         worry=emotions[3], anger=emotions[4])            dt = datetime.datetime.now()            diary.update(updated_at = dt)            # return JsonResponse({"content": content})            return JsonResponse({"content": content, "user": user, "sadness": emotions[0],                                               "neutrality": emotions[1], "happiness": emotions[2],                                               "worry": emotions[3], "anger": emotions[4]})    filter_backends = (DjangoFilterBackend,)    filter_fields = ('user',)def deleteAccount(request):    try:        jwt = request.META['HTTP_AUTHORIZATION']        decoded_payload = jwt_decode_handler(jwt[4:])        user = User.objects.get(id=decoded_payload['user_id'])        user.delete()        return HttpResponse(status=200)    except Exception:        return HttpResponse(status=401)