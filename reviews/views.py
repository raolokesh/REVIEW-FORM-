from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ReviewData
from django.views import View
# Create your views here.
from .form import ReviewForm

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


def thank_you(request):
    return render(request, "reviews/thank_you.html")
