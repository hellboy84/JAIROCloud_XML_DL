# JAIROCloud_XML_DL
JAIRO Cloudで公開しているリポジトリのメタデータを一括取得するPythonツール(JCmetadataDL.py)です。OAI-PMHプロトコルを使用してJPCOAR形式のXMLメタデータを収集できます。

# [JCmetadataDL.py](https://github.com/hellboy84/JAIROCloud_XML_DL/blob/main/JCmetadataDL.py) (メインプログラム)
## 事前作業
- 'pip install sickle'  を行っておいて下さい。
## 使い方
- 以下の設定を施したあと，任意のディレクトリでこのpyを実行して下さい。
## 設定
- 「**base_url**」 に取得したいリポジトリのURLを入力して下さい。(例：https://toho.repo.nii.ac.jp)
- 「**metadata_format**」 に取得形式を設定して下さい。デフォルトは「jpcoar_1.0」です。
- 「**set_spec**」 に取得したいインデックスツリーのIDを入力して下さい(例：'1726806982884')。デフォルトは「None」になっており，リポジトリ上の全データを取得しようとします。
  - インデックスツリーのIDはリポジトリ上でもわかりますが，一覧取得用のpy([list_sets.py](https://github.com/hellboy84/JAIROCloud_XML_DL/blob/main/list_sets.py))も用意したので適宜ご利用下さい。
- テストで小件数を取得したい場合などは，50行目以下の「処理上限設定」を使って下さい。「if record_count >= 200: break」の部分のコメントアウトを解除してお好みの件数を設定して下さい。
## 動作内容補足
- pyと同じディレクトリにxmlファイルが作成されます。
  - ファイル名は「**records_yyyymmddhhmmss.xml**」です。
  - あるいはツリーを指定した場合は「**records_'インデックスツリーのID'_yyyymmddhhmmss.xml**」です。
- 100件取得ごとにファイルを更新します。途中で止めた場合もその時点までに取得したレコードでファイルができています。
- 多分100件の取得に30秒ほどかかります。1万件だと50分ほどかかる計算です。時間に余裕を見て実行して下さい。
  - 件数が多い場合はツリーごとに分割して取得するなどして下さい(set_specの利用)。

# [list_sets.py](https://github.com/hellboy84/JAIROCloud_XML_DL/blob/main/list_sets.py) (おまけ)
- 対象のリポジトリのインデックスツリーの情報を取得します
## 事前作業
- 'pip install sickle'  を行っておいて下さい。
## 使い方
- 以下の設定を施したあと，任意のディレクトリでこのpyを実行して下さい。
## 設定
- 「**base_url**」 に取得したいリポジトリのURLを入力して下さい。(例：https://toho.repo.nii.ac.jp)
- 「**target_level**」に取得したい階層レベルを入力して下さい。初期は「0」になっており，最上位のみを取得します。（0=最上位、1=第1階層、None=全階層）
## 動作内容補足
- pyと同じディレクトリにtxtファイルが作成されます。
  - ファイル名は「**sets_list_yyyymmddhhmmss.txt**」です。

# 参考リンク
- [NIMSのページのsickle利用例紹介](https://dice.nims.go.jp/services/MDR/manual/html/api.html#bulk-metadata-download)
  - このページの使用例に簡易な機能を付与したものがこのリポジトリのプログラムです。

# 注記
- xmlファイルは，VS Codeなどで「Shift + ALt + F」で構造が展開できます。(要拡張機能「XML Tools」など)
- これらのコードの作成は生成AIのサポートを受けています。 

