# JAIROCloud_XML_DL
JAIRO Cloudで公開しているリポジトリのメタデータのXMLを取得するPythonプログラムです。

# 使い方
## [JCmetadataDL.py](https://github.com/hellboy84/JAIROCloud_XML_DL/blob/main/JCmetadataDL.py)
### 事前作業
- 'pip install sickle'  を行っておいて下さい。
### 使い方
- 以下の設定を施したあと，任意のディレクトリでこのpyを実行して下さい。
### 設定
- 「**base_url**」 に取得したいリポジトリのURLを入力して下さい。(例：https://toho.repo.nii.ac.jp)
- 「**metadata_format**」 に取得形式を設定して下さい。デフォルトは「jpcoar_1.0」です。
- 「**set_spec**」 に取得したいインデックスツリーのIDを入力して下さい(例：'1726806982884')。デフォルトは「None」になっており，リポジトリ上の全データを取得しようとします。
  - インデックスツリーのIDはリポジトリ上でもわかりますが，一覧取得用のpy([list_sets.py](https://github.com/hellboy84/JAIROCloud_XML_DL/blob/main/list_sets.py))も用意したので適宜ご利用下さい。
- テストで小件数を取得したい場合などは，50行目以下の「処理上限設定」を使って下さい。「if record_count >= 200: break」の部分のコメントアウトを解除してお好みの件数を設定して下さい。
### 動作内容補足
- pyと同じディレクトリにxmlファイルが作成されます。
  - ファイル名は「**records_yyyymmddhhmmss.xml**」です。
  - あるいはツリーを指定した場合は「**records_'インデックスツリーのID'_yyyymmddhhmmss.xml**」です。
- 多分100件の取得に30秒ほどかかります。1万件だと50分ほどかかる計算です。時間に余裕を見て実行して下さい。
  - 件数が多い場合はツリーごとに分割して取得するなどして下さい(set_specの利用)。

## [list_sets.py](https://github.com/hellboy84/JAIROCloud_XML_DL/blob/main/list_sets.py)


