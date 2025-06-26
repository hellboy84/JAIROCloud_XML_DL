from sickle import Sickle
import time
from datetime import datetime
import os

# 設定
base_url = 'https://toho.repo.nii.ac.jp' # リポジトリのベースURL
repository_url = f'{base_url}/oai'
metadata_format = 'jpcoar_1.0'
set_spec = None # セット指定 Noneの場合は全レコードを取得

print(f"処理開始: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("OAIリポジトリに接続中...")

sickle = Sickle(repository_url)
print("メタデータレコードの取得を開始します...")

# セット指定(set_spec)がない場合(= None)とある場合(≠ None)で分岐
if set_spec:
    print(f"セット指定: {set_spec}")
    records = sickle.ListRecords(metadataPrefix=metadata_format, set=set_spec)
else:
    print("全レコードを取得します")
    records = sickle.ListRecords(metadataPrefix=metadata_format)

print("レコードの書き込みを開始します...")
record_count = 0

# ファイル名に現在の日時を追加
timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
# 出力ファイルのパスを設定
output_dir = os.path.dirname(os.path.abspath(__file__)) 
if set_spec:
    # セット指定がある場合、ファイル名にセット名を含める
    set_name = set_spec.replace(':', '_')  # コロンをアンダースコアに変換
    filename = os.path.join(output_dir, f'records_{set_name}_{timestamp}.xml')
else:
    filename = os.path.join(output_dir, f'records_{timestamp}.xml')

with open(filename, 'w', encoding='utf-8') as f:
    for record in records:
        f.write(str(record) + '\n')
        record_count += 1
        
        # 100件ごとに進捗を表示と保存
        if record_count % 100 == 0:
            print(f"処理済み: {record_count} 件 - {datetime.now().strftime('%H:%M:%S')}")
            f.flush()
        
        # 処理上限設定
        # if record_count >= 200:
        #     break

print(f"処理完了: {record_count} 件のレコードを取得しました")
print(f"出力ファイル: {filename}")
print(f"終了時刻: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("\n" + "="*10)
print("処理が完了しました。Enterキーを押して終了してください...")
input()
