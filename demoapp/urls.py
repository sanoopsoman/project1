from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.demo,name='demo'),
    path('staff/',views.staff,name='staff'),
    path('accounts/',views.accounts,name='accounts'),
    path('person/',views.person,name='person'),
    path('add_staff/',views.add_staff,name='add_staff'),
    path('add_accounts/',views.add_accounts,name='add_accounts'),
    path('add_person/',views.add_person,name='add_person'),
    path('view_staff/',views.view_staff,name='view_staff'),
    path('view_accounts/',views.view_accounts,name='view_accounts'),
    path('view_person/',views.view_person,name='view_person'),
    path('update_staff/<int:id>',views.update_staff,name='update_staff'),
    path('update_staff2/<int:id>',views.update_staff2,name='update_staff2'),
    path('update_accounts/<int:id>',views.update_accounts,name='update_accounts'),
    path('update_accounts1/<int:id>',views.update_accounts1,name='update_accounts1'),
    path('update_person/<int:id>',views.update_person,name='update_person'),
    path('update_person2/<int:id>',views.update_person2,name='update_person2'),
    path('delete_accounts/<int:id>',views.delete_accounts,name='delete_accounts'),
    path('delete_person/<int:id>',views.delete_person,name='delete_person'),
    path('delete_person/<int:id>',views.delete_staff,name='delete_staff'),
    path('view_salary/',views.view_salary,name='view_salary'),
    path('flower/',views.flower,name='flower'),
    path('add_flower/',views.add_flower,name='add_flower'),
    ]