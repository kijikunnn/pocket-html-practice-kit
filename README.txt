Cloudflare BeaconのHTML確認 — 無料オフライン練習キット

目的
保存したHTMLに、チェッカーの条件に一致するscript要素が何件あるかを読みます。
data-cf-beacon属性の有無とscript要素の有無を分けて考える練習です。
全HTMLは人工例で、実在サイトの応答・障害・利用者数ではありません。
トークンの代わりに EXAMPLE_NOT_REAL を使っています。

準備と実行
Python 3.9以降が必要です。追加パッケージ・アカウント・通信・AIは不要です。
ZIPを手元のフォルダに展開し、ターミナルでそのフォルダへ移動してください。
最初に同梱のPythonソースとHTMLをテキストエディタで確認してください。
HTMLはブラウザーで開いたり実行したりせず、Pythonで文字として読みます。
HTML内には実在するスクリプト配信先のURLがありますが、チェッカーは取得しません。

1件を確認する例:
  python3 check-analytics-html.py fixtures/06-query-token.html

全10例を期待結果と比較する:
  python3 verify_examples.py

Windowsでpython3がない場合は、利用中のPython環境に応じて py -3 に置き換えます。
検証スクリプトは同梱チェッカーのSHA-256を確認し、各例を最大2秒で実行します。
一致すると status: expected_outputs_match、fixture_count: 10 を表示します。
これは「期待した件数が出た」という意味で、サイトの合格判定ではありません。

結果の読み方（script要素 / 値のあるdata-cf-beacon属性）
01-no-script.html                  0 / 0  scriptなし
02-attribute-only.html             0 / 0  divに属性があっても対象scriptではない
03-script-no-attribute.html        1 / 0  scriptあり・属性なし
04-empty-attribute.html            1 / 0  scriptあり・属性は空文字
05-example-attribute.html          1 / 1  架空の属性値あり。正常設定の証明ではない
06-query-token.html               1 / 0  URLのqueryに架空token。属性なしでもscriptはある
07-two-scripts.html                2 / 2  2要素ある。二重集計が起きたという証明ではない
08-wrong-host.html                 0 / 0  似た名前の別ホストは数えない
09-comment-only.html               0 / 0  HTMLコメント内だけの例は数えない
10-template-and-script.html        1 / 1  template内を除き、外の1要素を数える

06の表記は、属性0だけで未設置と判断しないための例です。架空tokenなので、
有効な設定・送信成功の例として使わないでください。Cloudflare公式FAQには、
GTM向けにtokenをscript URLのqueryで指定する別形式が掲載されています。
https://developers.cloudflare.com/web-analytics/faq/

確認できないこと
・このPython版はHTMLParserによる文字解析です。ブラウザー版と同一の解析器ではありません。
・属性値の空白だけ、無効なJSON、架空tokenも「値あり」と数えます。
  JSONの正しさ・tokenの有効性・正しい設定であることは検証しません。
・scriptのtype、SVG等の名前空間、重複属性、不正HTMLの補正をブラウザー準拠で判定しません。
  URLもHTTP/HTTPSだけに限定していません。これらを実行可能なタグの判定に使わないでください。
・JavaScriptで後から追加するタグ、スクリプト実行、CSP、実際の通信、管理画面への集計、
  広告や検索の承認、売上は確認しません。件数だけでタグの追加・削除を決めないでください。
・同梱チェッカー単体には入力サイズ上限がありません。練習には同梱の小さいHTMLを使ってください。
  検証スクリプトは1例8 KiB以内に制限しています。秘密情報や本番HTMLは同梱していません。

自分の公開ページを後で確認する場合も、HTMLの存在、Networkの通信、管理画面の集計を
別々に記録します。このキットの実行で本番サイトのアクセスや売上は発生しません。

同梱物と出所
check-analytics-html.py はポケットAIラボの既存公開ソースを無改変でコピーしています。
公開元: https://pocket-ai-lab.com/downloads/check-analytics-html.py
SHA-256: 9927076590dcf237cca3d4c59f8a11d85c4a534d693868d53c253f4831818c67
expected-results.json は人工例の期待件数、manifest.json は各同梱物のSHA-256です。
検証結果の一致は教材の動作確認です。利用需要・購入・収益の証拠ではありません。

任意の参考資料
DNS切り替え当日の記録が必要な方向けに、980円（税込）の公開前チェックリストがあります。
この無料キットの利用に購入は不要です。計測の修理・設定代行を販売するものではありません。
https://pocket-ai-lab.com/product/xserver-cloudflare-checklist/?utm_source=github&utm_medium=release&utm_campaign=html_practice_20261107
