from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from .models import Record
from django.contrib.auth.models import User
from social_django.models import UserSocialAuth
from django.db.models import Sum

from django.http import JsonResponse, HttpResponse
from .forms import PostForm
from django.conf import settings

import tweepy
import math
import datetime

def login_form(request):
    return render(request, 'app/login.html', {})

@login_required
def timer(request):
    if request.method=="POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
    form = PostForm() 
    return render(request, 'app/timer.html' , {'form': form, })

@login_required
def mypage(request):
    q = User.objects.filter(id=request.user.id).annotate(times=Sum('record__time'))
    time = q[0].times
    if not time:
        time = 0
    lv = level(time);
    progress = int(100 * (time - level_req(lv))/(level_req(lv+1)-level_req(lv)))
    require = level_req(lv+1) - time
    
    # 直近一週間の勉強時間集計
    startdate = datetime.date.today() - datetime.timedelta(6)
    enddate = datetime.date.today()
    q = Record.objects.filter(user__id=request.user.id, date__range=[startdate, enddate]).values('date').annotate(times=Sum('time')).order_by('date')
    weektime = [0 for i in range(7)]
    weekdate = [(startdate + datetime.timedelta(i)) for i in range(7)]
    i = 0
    for r in q:
        while r['date'] != startdate:
            i += 1
            startdate += datetime.timedelta(1)
        weektime[i] = "%.2f" % (r['times']/3600)

    auth = twitter_oauth(request.user.id)
    # tweepy初期化
    api = tweepy.API(auth)
    
    try:
        me = api.me()
        me.profile_image_url = me.profile_image_url_https.replace('_normal', '_bigger')
    except:
        me = None
    
    data = {
        'time': time_format(time),
        'weektime': weektime,
        'weekdate': weekdate,
        'level': lv,
        'progress': progress,
        'require': time_format(require),
        'me': me,
    }
    return render(request, 'app/info.html' , data)

@login_required
def tweet(request):
    if request.is_ajax() and request.method == 'POST':
        msg = request.POST.get('words')
        auth = twitter_oauth(request.user.id)
        try: 
            api = tweepy.API(auth)
            status = api.update_status(msg)
        except tweepy.error.TweepError as e: 
            return HttpResponse(status=500)
        msg = status.text
        icon = status.user.profile_image_url_https
        return JsonResponse({'msg': msg, 'icon': icon, })
    else:
        return HttpResponse(status=405)

@login_required
def ranking(request):
    auth = twitter_oauth(request.user.id)
    # tweepy初期化
    api = tweepy.API(auth)
    
    my_uid = UserSocialAuth.objects.get(user__id=request.user.id).uid
 
    friends_ids = [my_uid]
    # フォローした人のIDを全取得
 
    # Cursor使うとすべて取ってきてくれるが，配列ではなくなるので配列に入れる
    try:
        for friend_id in tweepy.Cursor(api.friends_ids, user_id=my_uid).items():
            friends_ids.append(friend_id)
 
        data = User.objects.filter(social_auth__uid__in=friends_ids).values('first_name','social_auth__uid').annotate(times=Sum('record__time')).order_by('-times')

        ranking_ids = []

        for i in range(len(data)):
            data[i]['times'] = time_format(data[i]['times'])
            ranking_ids.append(data[i]['social_auth__uid'])

        ranking_data = list(data)
        j=0

        for i in range(0, len(ranking_ids), 100):
            for user in api.lookup_users(user_ids=ranking_ids[i:i+100]):
                ranking_data[j]["prof_img"] = user.profile_image_url_https
                j+=1

        return render(request, 'app/ranking.html', {'ranking_data': ranking_data})
    except:
        msg = "フォロー情報の取得に失敗しました"
        return render(request, 'app/ranking.html', {'error': msg,}) 

def twitter_oauth(user_id):
    # 各種キーをセット
    consumer_key = settings.SOCIAL_AUTH_TWITTER_KEY
    consumer_secret = settings.SOCIAL_AUTH_TWITTER_SECRET
    access_token = UserSocialAuth.objects.get(user__id=user_id).access_token.get('oauth_token')
    access_token_secret = UserSocialAuth.objects.get(user__id=user_id).access_token.get('oauth_token_secret')
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return auth

def level(time):
    return int(math.sqrt(time/3600) + 1)

def level_req(level):
    return (level-1)**2 * 3600

def time_format(time):
    if not time:
        return "00:00:00"
    h = time//3600
    m = time//60%60
    s = time%60
    return "%02d:%02d:%02d" % (h, m, s)
