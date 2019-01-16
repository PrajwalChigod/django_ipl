from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'home'),
    
    path('first/', views.matches_played_per_year, name='first_solution'),
    path('second/', views.matches_won_by_teams, name='second_solution'),
    path('third/', views.extra_runs, name='third_solution'),
    path('fourth/', views.economic_bowler, name='fourth_solution'),
    path('fifth/', views.top_batsmen, name='fifth_solution'),

    path('first_graph/', views.matches_played_graph, name='first_graph'),
    path('second_graph/', views.matches_won_by_teams_graph, name='second_graph'),
    path('third_graph/', views.extra_runs_graph, name='third_graph'),
    path('fourth_graph/', views.economic_bowler_graph, name='fourth_graph'),
    path('fifth_graph/', views.top_batsmen_graph, name='fifth_graph')
]