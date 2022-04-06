from django.contrib import admin
from Library_app.models import BookModel
# Register your models here.

#register book model to admin site
class BookAdmin(admin.ModelAdmin):
    list_display = ['book_name','book_price','book_pages','book_author','book_publisher']
admin.site.register(BookModel,BookAdmin)