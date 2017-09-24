# Study Rival


## インストール方法

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

6. データベースのマイグレーション
``
(myvenv) $ python3 manage.py migrate
``

## テストサーバの起動
1. サーバの起動
``
(myvenv) $ python3 manage.py runserver
``

2. ブラウザで以下にアクセス  
``
http://127.0.0.1:8000/
``

## テストサーバの終了
サーバを起動したコンソールでCtrl+Cを入力
