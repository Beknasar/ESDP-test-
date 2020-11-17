from django.contrib import admin

from instagram_app.models import Account, AccountPost, PostMedia

admin.site.register(Account)
admin.site.register(AccountPost)
admin.site.register(PostMedia)