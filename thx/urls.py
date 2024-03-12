from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("base.urls")),
]

# Change admin text
admin.site.site_header = "THX. Admin"
admin.site.site_title = "THX."
admin.site.index_title = "Admin Dashboard"
