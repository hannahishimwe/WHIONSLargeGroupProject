"""
URL configuration for task_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from tasks import views
from ckeditor_uploader import views as ckeditor_views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('log_in/', views.LogInView.as_view(), name='log_in'),
    path('log_out/', views.log_out, name='log_out'),
    path('password/', views.PasswordView.as_view(), name='password'),
    path('profile/', views.ProfileUpdateView.as_view(), name='profile'),
    path('sign_up/', views.SignUpView.as_view(), name='sign_up'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('journal_log/',views.journal_log,name ='journal_log'),
    path('journal/entry/<int:entry_id>/pdf/', views.export_journal_entry_to_pdf, name='export_journal_entry_to_pdf'),
    path('journal/entry/<int:entry_id>/rtf/', views.export_journal_entry_to_rtf, name='export_journal_entry_to_rtf'),
    path('export_entries/', views.export_entries, name='export_entries'),
    path('favourites/',views.favourites,name ='favourites'),
    path('mood_breakdown/',views.mood_breakdown,name ='mood_breakdown'),
    path('templates/',views.templates,name ='templates'),
    path('trash/',views.trash,name ='trash'),
    path('create_entry/', views.CreateJournalEntryView.as_view(), name="create_entry"),
    path('delete_entry/<int:entry_id>', views.delete_journal_entry, name="delete_entry"),
    path('favourite_entry/<int:entry_id>', views.favourite_journal_entry, name="favourite_entry"),
    path('unfavourite_entry/<int:entry_id>', views.unfavourite_journal_entry, name="unfavourite_entry"),
    path('delete_entry_permanent/<int:entry_id>',views.delete_journal_entry_permanent,name = "delete_entry_permanent"),
    path('recover_entry/<int:entry_id>',views.recover_journal_entry,name = "recover_entry"),
    path('set_preferences/',views.SetPreferences.as_view(),name = "set_preferences"),
    path('edit_preferences/',views.EditPreferences.as_view(),name = "edit_preferences"),
    path('ckeditor/', include('ckeditor_uploader.urls')), 
    path('r^ckeditor/upload/', login_required(ckeditor_views.upload), name='ckeditor_upload'),
    path('search/', views.search_journal, name='search_journal'),
    path('journal/<int:entry_id>/', views.journal_detail, name='journal_detail'),
    path('search-suggestions/', views.search_suggestions, name='search-suggestions'),
    path('search-trash/', views.search_trash, name='search_trash'),
    path('search-suggestions1/', views.search_suggestions1, name='search-suggestions1'),
    path('search/favourite/', views.search_favourite, name='search_favourite'),
    path('search/favouritesuggestion/', views.search_favouriteSuggestion, name='search_favouriteSuggestion'),

    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

