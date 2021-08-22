機能
- 参照可能なファイル一覧
- タグ付けしたファイル一覧
- ファイルにタグ付け、タグ外し
- タグ検索と同じ感じで拡張子検索も一緒に出来る
  - suffix:mp3 AND tag:SUKI

```
$ phyaa ls . --json

# 拡張子が.mp3のファイル一覧
# NOTE: filetypeではなくあくまで拡張子
$ phyaa ls . --json --tags "ext_mp3"

```
