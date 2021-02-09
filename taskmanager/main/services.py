from .forms import TaskForm

def note(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        form.save()
        return redirect('main')

    form = TaskForm

    context = {'form' : form}
    return context
