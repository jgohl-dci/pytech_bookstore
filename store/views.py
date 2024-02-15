#  from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.views import View


def index(request):
    # text = "A basic function-based view"
    # if text is not None:
    #     text = "We changed it!"
    # content = f"<h1>{text}</h1>"

    # if request.method == "GET":
    #     text = "This is a GET request"
    # elif request.method == "POST":
    #     text = "This is a POST request"

    # cookie_info = request.COOKIES.get("sessionid")
    logged_in = request.user.is_authenticated
    if logged_in:
        text = f"Welcome {request.user}"

    return HttpResponse(text)


def test_view(request):
    response = HttpResponse()
    if request.user.is_authenticated:
        response.write(f"Welcome, {request.user}.")
    else:
        response.write("Please log in.")
    return response


@require_http_methods(["PUT", "GET"])
def browse(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/test")
    else:
        return HttpResponse(f"Hello. {request.user}")


class SimpleClassBasedView(View):
    http_method_names = ["DELETE", "GET"]

    def get(self, request):
        text = "This is a GET request"
        if request.user.is_authenticated:
            text = f"Hi {request.user}. This is a GET request"
        return HttpResponse(text)

    def post(self, request):
        text = "This is a POST request"
        return HttpResponse(text)
