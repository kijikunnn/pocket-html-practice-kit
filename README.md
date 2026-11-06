# Cloudflare BeaconのHTML確認・練習キット

保存したHTMLで、`data-cf-beacon`属性が0でもscript要素が存在するケースを、人工例10件で練習できます。Python 3.9以降の標準ライブラリだけを使います。無料で完結し、アカウント・追加パッケージ・外部送信は不要です。

## 始め方

[Releases](https://github.com/kijikunnn/pocket-html-practice-kit/releases)から専用ZIPを展開し、そのフォルダで次を実行します。

```sh
python3 verify_examples.py
python3 check-analytics-html.py fixtures/06-query-token.html
```

全例が一致すると`expected_outputs_match`、`fixture_count: 10`を表示します。Windowsで`python3`がない場合は、利用中のPython環境に合わせて`py -3`に置き換えてください。[詳しい手順と10例の表](README.txt)も同梱しています。

HTMLはブラウザーで開かず、文字として読みます。例のtokenはすべて`EXAMPLE_NOT_REAL`です。この確認ではJavaScriptの実行、通信、Cloudflare管理画面への集計、設定の正否を判定できません。出力一致は「正常に計測できた」という意味ではありません。

## 試した結果を伝える

[Issues](https://github.com/kijikunnn/pocket-html-practice-kit/issues)に、試した例のファイル名と、何が分かった・どこで困ったかを記載できます。本番HTML、トークン、メールアドレス、個人情報は投稿しないでください。報告は任意です。

既存の無料[ブラウザー版HTML確認ツール](https://pocket-ai-lab.com/tools/html-check/)もあります。Python版とは解析器が異なります。
