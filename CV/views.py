from django.shortcuts import get_object_or_404, render

from .models import Information, Education, Research, Internship, Honor, Addition


def index(request):
    inf = get_object_or_404(Information)
    edu_list = Education.objects.all()
    res_list = Research.objects.all()
    int_list = Internship.objects.all()
    hon_list = Honor.objects.all()
    add_list = Addition.objects.all()
    context = {"inf": inf, "edu_list": edu_list, "res_list": res_list, "int_list": int_list, "hon_list": hon_list, "add_list": add_list}
    return render(request, "CV/index.html", context)
