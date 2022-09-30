from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from .models import Note


def notes(request):
    return render(request, "nodos/nodos.html")


def get_notes(request):
    notes = Note.objects.all()
    # notes = Note.objects.filter(done=False)
    # notes_done = Note.objects.filter(done=True)

    context = {"notes": notes}
    template = "nodos/htmx/list_notes.html"

    return render(request, template, context)


# def get_single_note(request, id):
#     note = Note.objects.filter(pk=id)
#     context = {"note": note}
#     template = "nodos/htmx/list_notes.html"

#     return render(request, template, context)


def add_note(request):
    data = Note.objects.all()
    title = request.POST.get("title")
    description = request.POST.get("description")
    context = {"notes": data}
    template = "nodos/htmx/list_notes.html"

    if title:
        note = Note(title=title, description=description)
        note.save()
        return render(request, template, context)
    return render(request, template, context)


def delete_note(request, id):
    note = Note.objects.filter(pk=id)
    note.delete()
    return HttpResponse("")


def done_note(request, id):
    data = Note.objects.all()
    done = request.POST.get(f"done")
    note = Note.objects.filter(pk=id)
    note_done = list(note.values())[0]["done"]
    # print(list(note.values())[0]["done"])

    context = {"notes": note}
    template = "nodos/htmx/list_notes.html"

    if note_done == True:
        note.update(done=0)
        return render(request, template, context)
    elif note_done == False:
        note.update(done=1)
        return render(request, template, context)
