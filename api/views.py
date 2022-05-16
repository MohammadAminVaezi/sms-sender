from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .tasks import send_text as send_text_task


@csrf_exempt
def send_text(request):

    if request.method != "POST":
        return HttpResponse(
            "Not Implemented",
            status=501
        )

    email = request.POST.get('email')
    phone_number = request.POST.get('phone_number')
    text = request.POST.get('text')


    send_text_task.delay(phone_number=phone_number, email=email, text=text)

    return HttpResponse(
        "We will send your text as soon as possible",
        status=200,
    )
