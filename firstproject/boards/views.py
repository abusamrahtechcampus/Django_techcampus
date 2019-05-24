from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import Board, Topic, Post
from django.contrib.auth.models import User
from .forms import NewTopicForm

# Create your views here.


def index(request):
	boards = Board.objects.all()
	return render(request, 'home.html', {'boards':boards})

def boards_topic(request, id):
	try:
		board = Board.objects.get(pk=id)
#		board = get_object_or_404(Board, pk=id)
	except Board.DoesNotExist:
		return render(request,'error.html',{'message':"There is no board"})
#		raise Http404

	return render(request,'topics.html',{'board':board})


def new_topic(request,id):

	board = Board.objects.get(pk=id)
	user = User.objects.first()
	if request.method == "POST":
		form = NewTopicForm(request.POST)
		if form.is_valid():
			topic = form.save(commit=False)
			topic.board = board
			topic.Created_by = user
			topic.save()


#		supject = request.POST['supject']
#		message = request.POST['message']
#		print(supject,message)
		
#		topic = Topic.objects.create(supject =supject, Created_by= user, board =board)
		post = Post.objects.create(message =form.cleaned_data.get('message'), topic =topic, Created_by =user)

		return redirect('boards_topic',id=board.pk)

	form = NewTopicForm()
	return render(request, 'new_topic.html',{'board':board,'form':form})
