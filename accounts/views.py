from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.
def register(res):
	if res.method == "POST":
		form = RegisterForm(res.POST)
		if form.is_valid():	
			form.save()

		redirect("/")
	form = RegisterForm()
	params = {
		"form": form
	}

	return render(res, "register/register.html", params)