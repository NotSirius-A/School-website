from django.db import models
from django.core.exceptions import ValidationError
from bs4 import BeautifulSoup

class Article(models.Model):
    title = models.CharField(max_length=110, default="Title here")
    slug = models.SlugField(max_length=60, unique=True, default="slug-here", 
        help_text="Slug will appear in a URL, it be short and resemble the title")

    text = models.TextField(max_length=15000, default="Text here", help_text="HTML tags are allowed")

    show_on_lists = models.BooleanField(default=False, 
        help_text="Choose whether this article should be visible on lists or only accesible trough direct urls. \
        Leave disabled for hardcoded articles like:'rules' or 'contact'")

    date = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

    def short_snippet(self):
        """return a snippet of the article, without images
        """
        length = 250

        content = self.text[:length]
        soup = BeautifulSoup(content, features="html.parser")

        #remove the images, so they dont disrupt the page
        try:
            soup.img.decompose()
        except:
            pass

        #just to make sure it doesnt crash when text is empty
        try:
            snippet = soup.prettify()
        except Exception:
            return "Snippet not available"

        if len(self.text) > length:
            return snippet + '...'
        else:
            return snippet


    def clean(self):
        #html tags are allowed in the article text, therefore is has to be sanitized

        soup = BeautifulSoup(self.text, features="html.parser")

        if len(soup.find_all("script")) > 0:
            raise ValidationError({'text':'No scripts are allowed'})

        if soup.get_text().find(".js") != -1:
            raise ValidationError({'text':'".js" is not allowed'})

        if soup.get_text().find(".%00js") != -1:
            raise ValidationError({'text':'".js" is not allowed'})

        if soup.get_text().find("alert") != -1:
            raise ValidationError({'text':'No scripts are allowed'})

        allowed_tags = ['a', 'img', 'p', 'li', 'ul', 'h1', 'span']

        for tag in soup():
            if tag.name not in allowed_tags:
                raise ValidationError({'text': f"Only {', '.join(allowed_tags)} tags are allowed"})
