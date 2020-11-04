from django.shortcuts import render

from .models import Project

# Get Projects and display them
def index(request):
    project_list = Project.objects.order_by('-tvl')[:10]
    context = {'project_list' : project_list}
    return render(request, 'defi/index.html', context)

# Show specific project
def detail(request, project_id):
    try:
        project = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        raise Http404('Project does not exist')
    return render(request, 'defi/show.html', { 'project': project })