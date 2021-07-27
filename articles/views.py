from django.http import HttpResponseRedirect
from django.shortcuts import render
from articles.models import Article, Comment



def articles_list(request):
    if request.method == "POST": 
        article = Article() 
        article.name = request.POST['title'] 
        article.category = request.POST['category']
        article.text = request.POST['text']
        article.photo = request.FILES.get("photo")
        article.save()

        for tag in (request.POST['tags']).split(","):
            article.tags.add(tag)
        article.save()
        return HttpResponseRedirect("/")

    articles = Article.objects.all()
    context = {"articles":articles}
    return render(request,"articles_list.html",  context=context)

def view_article(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == "POST":
        comment = Comment()
        comment.article = article
        comment.author = request.POST["author"]
        comment.text = request.POST["comment_text"]
        comment.save()
        return HttpResponseRedirect(article_id)   

    comments = Comment.objects.filter(article=article)
    context = {"article":article, "comments":comments}
    return render(request,"article.html", context=context)




