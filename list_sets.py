from sickle import Sickle
from datetime import datetime
import os

# 設定
base_url = 'https://toho.repo.nii.ac.jp'
repository_url = f'{base_url}/oai'
target_level = 0  # 取得したい階層レベル（0=最上位、1=第1階層、None=全階層）

print(f"セット一覧取得開始: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("OAIリポジトリに接続中...")
if target_level is not None:
    print(f"階層レベル {target_level} のセットのみを取得します")
else:
    print("全階層のセットを取得します")

# ファイル名に現在の日時を追加
timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
# 出力ファイルのパスを設定
output_dir = os.path.dirname(os.path.abspath(__file__))  
filename = os.path.join(output_dir, f'sets_list_{timestamp}.txt')
print(f"出力ファイル: {filename}")

sickle = Sickle(repository_url)
print("利用可能なセット一覧を取得しています...")

sets = sickle.ListSets()

print(f"セット一覧を '{filename}' に書き出し中...")

with open(filename, 'w', encoding='utf-8') as f:
    f.write(f"セット一覧取得開始: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    f.write(f"リポジトリURL: {repository_url}\n")
    if target_level is not None:
        f.write(f"対象階層レベル: {target_level}\n")
    else:
        f.write("対象階層レベル: 全階層\n")
    f.write("\n=== 利用可能なセット一覧 ===\n")
    
    set_count = 0
    filtered_count = 0  # フィルタリング後のカウント
    set_hierarchy = {}  # 階層構造を把握するための辞書
    
    for s in sets:
        set_count += 1
        spec = s.setSpec
        name = s.setName
        
        # 階層レベルを判定（:の数で判断）
        level = spec.count(':')
        
        # 階層レベルでフィルタリング
        if target_level is not None and level != target_level:
            continue  # 指定した階層レベルでない場合はスキップ
        
        filtered_count += 1
        indent = "  " * level  # インデントで階層を表現
        
        f.write(f"{filtered_count}. {indent}セット識別子: {spec}\n")
        f.write(f"   {indent}セット名: {name}\n")
        f.write(f"   {indent}階層レベル: {level}\n")
        
        if hasattr(s, 'setDescription') and s.setDescription:
            f.write(f"   {indent}説明: {s.setDescription}\n")
        
        # 階層関係を記録
        if level > 0:
            parent = ':'.join(spec.split(':')[:-1])
            f.write(f"   {indent}上位セット: {parent}\n")
        
        f.write("-" * 50 + "\n")
        
        # 50件ごとに進捗表示とファイル保存
        if set_count % 50 == 0:
            print(f"[進捗] 全{set_count}件中 {filtered_count}件を抽出済み...")
            f.flush()  # 途中経過を保存
    
    f.write(f"\n=== 取得完了 ===\n")
    f.write(f"総セット数: {set_count} 件\n")
    f.write(f"抽出されたセット数: {filtered_count} 件\n")
    f.write(f"終了時刻: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

print(f"セット一覧の書き出しが完了しました: {filename}")
print(f"総セット数: {set_count} 件")
print(f"抽出されたセット数: {filtered_count} 件")
print(f"終了時刻: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("\n" + "="*10)
print("処理が完了しました。Enterキーを押して終了してください...")
input()

