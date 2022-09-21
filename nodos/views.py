from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from .models import Note


def notes(request):
    return render(request, 'nodos/nodos.html')


def get_notes(request):
    data = Note.objects.all()
    return render(request, 'nodos/htmx/list_notes.html', {'notes': data})


def add_note(request):
    data = Note.objects.all()
    title = request.POST.get('title')
    description = request.POST.get('description')
    #done = request.POST.get('note-done')

    if title:
        note = Note(title=title, description=description)
        note.save()
        #return HttpResponse('success')
        return render(request, "nodos/htmx/list_notes.html", {'notes': data})
    return render(request, "nodos/htmx/list_notes.html", {'notes': data})


def delete_note(request, id):
    data = Note.objects.all()
    note = Note.objects.filter(pk=id)
    note.delete()
    return render(request, "nodos/htmx/list_notes.html", {'notes': data})

def done_note(request, id):
    data = Note.objects.all()
    done = request.POST.get(f'done')
    note = Note.objects.filter(pk=id)
    note_done = list(note.values())[0]["done"]
    #print(list(note.values())[0]["done"])
    
    if note_done == True:
        note.update(done=0)
        return render(request, "nodos/htmx/list_notes.html", {'notes': data})
    elif note_done == False:
        note.update(done=1)
        return render(request, "nodos/htmx/list_notes.html", {'notes': data})
    
    