from django.urls import path, include
from dbproject.views.index import index
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='API文档')
urlpatterns = [
    path("", index, name="index"),
    path("settings/", include("dbproject.urls.settings.index")),
    path("sysuser/", include("dbproject.urls.sysuser.index")),
    path("coach/", include("dbproject.urls.coach.index")),
    path("course/", include("dbproject.urls.course.index")),
    path("courseorder/", include("dbproject.urls.courseorder.index")),
    path("data/", include("dbproject.urls.datadisplay.index")),

    path(r'docs/', schema_view),

]