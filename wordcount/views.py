from django.shortcuts import render
import operator
def home(request):
    return render(request,"home.html")

def count(request):
    data=request.GET["fulltextarea"]
    word_list=data.split()
    word_length=len(word_list)
    worddictionary={}
    for word in word_list:
        if word in worddictionary:
            worddictionary[word]+=1
        else:
            worddictionary[word]=1
        sort_list=sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,"count.html",{"fulltext":data,"length":word_length,"worddictionary":sort_list})
