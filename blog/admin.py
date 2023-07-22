from django.contrib import admin

from blog.models import (
    CategoryModel, PostModel, CommentModel, ContactModel
)

admin.site.register(CategoryModel)

#33 admin register islemleri
@admin.register(PostModel)
class PostAdmin(admin.ModelAdmin):
    search_fields = ('title', 'content')
    list_display = (
        'title', 'create_date', 'update_date'
    )
#admin.site.register(PostModel,PostAdmin)

@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('writer', 'post', 'comment')
    search_fields = ('writer__username', )
#admin.site.register(CommentModel,CommentAdmin)

@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'create_date')
    search_fields = ('email',)
