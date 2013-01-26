from django.shortcuts import render
from dotastats.json import steamapi
from django.views.decorators.cache import cache_page

def home(request):
    return render(request, 'home.html')
    
#@cache_page(60 * 15) # 15min
def matches_overview(request):
    result_dict = steamapi.GetMatchHistory()
    return render(request, 'match_history.html', result_dict)

#@cache_page(60 * 60) # 60min
def matches_id(request, match_id):
    result_match = steamapi.GetMatchDetails(match_id)
    radiant_players = result_match.matchdetailsplayerentry_set.filter(player_slot__lt=100)
    dire_players = result_match.matchdetailsplayerentry_set.filter(player_slot__gte=100)
    
    
    return render(request, 'match_id.html', {'match': result_match, 'teams': (radiant_players, dire_players)})