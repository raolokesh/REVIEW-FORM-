from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic import CreateView,ListView
# Create your views here.

from .form  import ProfileForm
from .models import UserProfile

class CreateProfileView(CreateView):
    model = UserProfile
    template_name = "profiles/profile.html"
    fields = "__all__"
    success_url = "/profle"

class ProfileView(ListView):
     template_name = "profiles/user_profile.html"
     model = UserProfile
     context_object_name = "profiles"

# def store_file(file):
#     with open("temp/image.jpg","wb+") as dest:
#          for chunk in file.chunks():
#             dest.write(chunk)

# class ProfileView(View):
#     def get(self,request):
#         form = ProfileForm()
#         return render(request, "profiles/profile.html",{
#             "form":form,
#         })
    
#     def post(self, request):
#         submitted_form = ProfileForm(request.POST , request.FILES)
#         if submitted_form.is_valid():
#             profile = UserProfile(image = request.FILES["user_image"])
#             profile.save()
#             # store_file(request.FILES["image"])
#             # print(request.FILES["image"])
#             return HttpResponseRedirect("profile")

#         return render(request,"profiles/profile.html",{
#             "form": submitted_form
#         })    