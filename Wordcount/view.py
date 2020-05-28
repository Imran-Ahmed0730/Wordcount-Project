from django.http import HttpResponse # To write anything
from django.shortcuts import render  #To write HTML code
import operator
def homepage(request):
   return render(request, "Homepage.html")
def AboutPage(request):
   return render(request,"About.html")
def count(request):
   fullText = request.GET["fun"]
   WordList = fullText.split()
   WordDictionary = {}


   for Word in WordList:
      if Word in WordDictionary:
         WordDictionary[Word] +=1
      else:
         WordDictionary[Word] = 1

   SortedWords = sorted(WordDictionary.items(), key=operator.itemgetter(1), reverse=False)

   return render(request, "counting.html", {"Text": fullText, "WordCount": len(WordList), "Dictionary": SortedWords })
def eggs(request):
   return HttpResponse("Jasons loves eggs")

