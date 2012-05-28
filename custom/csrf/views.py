from django.shortcuts import render_to_response

def csrf_rejected(request, reason=""):
    ctx = {'reason':reason}
    return render_to_response("csrf/rejected.html", ctx)
