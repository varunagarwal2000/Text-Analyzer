# I have created this file - Varun 
from django.http import HttpResponse
from django.shortcuts import render,redirect


def index(request):
	return render(request,'index.html')


def analyze(request):
	# get the text
	djtext = request.POST.get('text','defualt')
	removepunc = request.POST.get('removepunc','off')
	fullcaps = request.POST.get('fullcaps','off')
	newlineremover = request.POST.get('newlineremover','off')
	extraspaceremover = request.POST.get('extraspaceremover','off')
	charcounter = request.POST.get('charcounter','off')
	# print(djtext)
	# analyzed = djtext
	punctuations = '''!()-[]{};:'",<>./?@#$%^&*_~'''
	analyzed=""

	if removepunc == 'on':
		for char in djtext:
			if char not in punctuations:
				analyzed = analyzed + char
		params = {'purpose': 'Remove punctuations','analyzed_text': analyzed}
		#we are updating the value of djtext to use it further in the code
		djtext = analyzed
		# return render(request,'analyze.html',params)

	if(fullcaps=='on'):
		analyzed = ""
		for char in djtext:
			analyzed = analyzed + char.upper()
		params = {'purpose': 'Upper Case', 'analyzed_text' : analyzed}
		djtext = analyzed
		# return render(request,'analyze.html',params)

	if(newlineremover=='on'):
		analyzed = ""
		for char in djtext:
			if char != '\n' and char!='\r':
				analyzed = analyzed +char
		params = {'purpose': 'new line remove', 'analyzed_text' : analyzed}
		djtext = analyzed
		# return render(request,'analyze.html',params)

	if(extraspaceremover=='on'):
		analyzed = ""
		for index, char in enumerate(djtext):
			if not(djtext[index]==' ' and djtext[index+1]==' '):
				analyzed = analyzed +char
		params = {'purpose': 'extra space remover', 'analyzed_text' : analyzed}
		djtext = analyzed
		# return render(request,'analyze.html',params)

	if(charcounter=='on'):
		counter = 0
		for char in djtext:
			counter = counter + 1
		params = {'purpose': 'counting the characters','analyzed_text':'There are '+ str(counter) +' characters'}
		djtext = analyzed
		# return render(request,'analyze.html',params)
	if(removepunc!='on' and fullcaps!='on' and newlineremover!='on' and extraspaceremover!='on' and charcounter!='on'):
		return HttpResponse("Please select a valid operation!!")	

	return render(request,'analyze.html',params)

def aboutpage(request):
	return render(request,'about.html')

def contactuspage(request):
	return render(request,'contact.html')