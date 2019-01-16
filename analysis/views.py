from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Matches, Deliveries
from django.db.models import Count, Sum, FloatField
from django.db.models.functions import Cast
import json
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)
# Create your views here.

@cache_page(CACHE_TTL)
def home(request):
    return render(request, 'analysis/home.html', {'title':'About'})

@cache_page(CACHE_TTL)
def matches_played_per_year(request):
    query = list(Matches.objects.values('season').annotate(count=Count('season')))
    return JsonResponse(query, safe=False)

@cache_page(CACHE_TTL)
def matches_played_graph(request):
    query = list(Matches.objects.values('season').annotate(count=Count('season')))
    query = json.dumps(query)
    context = {
        'query': query
    }
    return render(request, 'analysis/first_graph.html', context)

@cache_page(CACHE_TTL)
def matches_won_by_teams(request):
    query = list(Matches.objects.values('season', 'winner').annotate(count=Count('winner')))
    return JsonResponse(query, safe=False)

@cache_page(CACHE_TTL)
def matches_won_by_teams_graph(request):
    query = list(Matches.objects.values('season', 'winner').annotate(count=Count('winner')))
    query = json.dumps(query)
    context = {
        'query': query
    }
    return render(request, 'analysis/second_graph.html', context)

@cache_page(CACHE_TTL)
def extra_runs(request):
    query = list(Deliveries.objects.values('bowling_team').filter(match_id_id__season=2016).annotate(extra_run=Sum('extra_runs')).order_by('extra_run'))
    return JsonResponse(query, safe=False)

@cache_page(CACHE_TTL)
def extra_runs_graph(request):
    query = list(Deliveries.objects.values('bowling_team').filter(match_id_id__season=2016).annotate(extra_run=Sum('extra_runs')).order_by('extra_run'))
    query = json.dumps(query)
    context = {
        'query': query
    }
    return render(request, 'analysis/third_graph.html', context)

@cache_page(CACHE_TTL)
def economic_bowler(request):
    query = list(Matches.objects.values('deliveries__bowler').filter(season=2015).annotate(economy=Cast(Sum('deliveries__total_runs')/(Count('deliveries__ball')/6.0), FloatField())).order_by('economy')[:10])
    return JsonResponse(query, safe=False)

@cache_page(CACHE_TTL)
def economic_bowler_graph(request):
    query = list(Matches.objects.values('deliveries__bowler').filter(season=2015).annotate(economy=Cast(Sum('deliveries__total_runs')/(Count('deliveries__ball')/6.0), FloatField())).order_by('economy')[:10])
    query = json.dumps(query)
    context = {
        'query': query
    }
    return render(request, 'analysis/fourth_graph.html', context)

@cache_page(CACHE_TTL)
def top_batsmen(request):
    query = list(Deliveries.objects.values('batsman').annotate(top_run=Sum('batsman_runs')).order_by('-top_run')[:10])
    return JsonResponse(query, safe=False)

@cache_page(CACHE_TTL)
def top_batsmen_graph(request):
    query = list(Deliveries.objects.values('batsman').annotate(top_run=Sum('batsman_runs')).order_by('-top_run')[:10])
    query = json.dumps(query)
    context = {
        'query': query
    }
    return render(request, 'analysis/fifth_graph.html', context)