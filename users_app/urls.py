from django.urls import include, path
import users_app.views as v


app_name = "users_app"


urlpatterns = [
    path("register_user/", v.RegisterView.as_view(), name="register_user"),

]