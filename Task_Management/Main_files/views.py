from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm

# Function for Home page rendering
def Home(request):
    tasks = Task.objects.all()  # Get all tasks from the database
    return render(request, 'Home.html', {'tasks': tasks})

# Function for Task Page Rendering
def Tasks(request):
    tasks = Task.objects.all()
    return render(request, 'Task.html', {'tasks': tasks})

# Function for Task details page rendering
def Task_details(request):
    return render(request, 'Thankyou.html')

# Function for Add Task page rendering
def add_task(request):
    if request.method == 'POST':
        # Get data from the form fields
        name = request.POST['name']
        status = request.POST['status']
        priority = request.POST['priority']
        due_date = request.POST['due_date']
        description = request.POST['description']

        # Create a new Task object and save it to the database
        new_task = Task(
            name=name,
            status=status,
            priority=priority,
            due_date=due_date,
            description=description
        )
        new_task.save()

        # Redirect to the tasks page after saving
        return redirect('task')  # Or any other URL you want to redirect to after task creation

    return render(request, 'Add_task.html')

# Function to edit task
def edit_task(request, id):
    task = get_object_or_404(Task, id=id)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task')  # Redirect to task page after saving
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'Edit_task.html', {'form': form})

# Function to delete task
def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('task')  # Redirect to task page after deletion
