# webget



## セットアップ

### chromedriverのインストール

https://pypi.org/project/chromedriver-binary/#history  
から、 自身のGoogleChromeのメジャーバージョンと同じ物を選択し、pipでインストールする

`pip install chromedriver-binary==chromedriverのバージョン`

### 事前インストール

`pip install selenium`
`pip install beautifulsoup4`

### 変数設定

DIST_URL:目的のURL  
IGNORE_TEXT = 退避ページに表示されるh1タグのテキスト(これ以外がh1タグにセットされるまで実行される)
