# Study Rival

## Study Rivalとは
StudyRivalはあなたのモチベーション維持を助けるアプリケーションです。  
ランキング機能により、Twitterでフォローしている友達と勉強時間の競争ができます！  
さらに！勉強すればするほどあなたのプレイヤーレベルもUP！！

このアプリケーションは、第三期 [CodePBL](http://codepbl.com/)で開発されました。

アプリケーションのURL(Heroku)  
https://studyrival.herokuapp.com/

## 必要な環境
- python3
- pip3

## 使用したライブラリ・フレームワーク
- Django
- Bootstrap
- Tweepy
- JQuery
- Python Social Auth
- Chart.js
- easy_regist

## ローカルでの起動方法
### 起動の準備
1. レポジトリをクローンまたはダウンロードする

2. ターミナルでレポジトリに移動する。

3. 仮想環境を作成  
``
$ python3 -m venv myvenv
``
4. 仮想環境を起動  
``
$ source myvenv/bin/activate
``  
実行後，以下ようになればOK  
``
(myvenv) 〜〜〜 $
``

5. 必要なライブラリをインストール  
``
(myvenv) $ pip3 install -r requirements.txt
``

6. ローカル用の設定ファイルを作成
`studyrival/local_settings.py`を作成し，以下のように記述して保存する。  

```
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SOCIAL_AUTH_TWITTER_KEY = 'ツイッターのAPI Key'
SOCIAL_AUTH_TWITTER_SECRET = 'ツイッターのAPI Secret'
DEBUG = True
```

7. データベースのマイグレーション  
``
(myvenv) $ python3 manage.py migrate
``

### テストサーバの起動
1. サーバの起動  
``
(myvenv) $ python3 manage.py runserver
``

2. ブラウザで以下にアクセス  
``
http://127.0.0.1:8000/
``

### テストサーバの終了
サーバを起動したコンソールでCtrl+Cを入力
