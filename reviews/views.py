from typing import Any, Dict
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ReviewData
from django.views import View
from django.views import View
# Create your views here.
from .form import ReviewForm
from django.views.generic import DetailView


from django.views.generic.base import TemplateView
class ReviewView(View):
    def get(self,request):
        form = ReviewForm()
        return render(request, "reviews/review.html", {
        "form": form
    })

    def post(self, request): 
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")
        return render(request, "reviews/review.html", {
        "form": form
    }) 
# def review(request):
#     if request.method == "POST":
#         # entered_username = request.POST["username"]
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # review = ReviewData(user_name=form.cleaned_data["user_name"],
#             #                     review_field=form.cleaned_data["review_text"],
#             #                     rating_field=form.cleaned_data["rating"])
#             # review.save()
#             return HttpResponseRedirect("/thank-you")
#     #     if e ntered_username == "":
#     #         return render(request, "reviews/review.html",{
#     #             "has_error": True
#     #         })
#             # print(entered_username)
#     #     return HttpResponseRedirect("/thank-you")
#     else:
#         form = ReviewForm()
#     return render(request, "reviews/review.html", {
#         "form": form
#     })

#     def get(self,request):
# class ThankyouView(View):
#         return render(request, "reviews/thank_you.html")
class ThankyouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "this works!" 
        return context
    
    # def get(self,request):
    #     return render(request, "reviews/thank_you.html")




# def thank_you(request):
    # return render(request, "reviews/thank_you.html")
class AllReviewView(TemplateView):
    template_name = "reviews/review_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] = ReviewData.objects.all()
        return context
    

# class SingleReviewView(TemplateView):
#     template_name = "reviews/single_review.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         review_id = kwargs["id"]
#         reviews = ReviewData.objects.get(pk = review_id)
#         context["review"] = reviews
#         return context
    

class SingleReviewView(DetailView):
    model = ReviewData
    template_name = "reviews/single_review.html"
    
    def get_context_data(self, **kwargs) :
        context =  super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session.get("favorite_review")
        context["is_favorite"] = favorite_id == str(loaded_review.id)
        return context

class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST["id"]
        print(review_id)
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect("/review/"+ review_id)
    
     