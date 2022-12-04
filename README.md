# train wikipedia doc2vec
[wikipedia_Data_to_DB](https://github.com/satabie/wikipedia-Data_to_DB)で構築したデータベースを用いて、Doc2Vecの訓練を行う。


# Usage:
まずcloneして仮想環境に入る。私の環境はfishであることに注意する。bashおよびzshならばactivate.fishの部分をactivateに変更すればよい。
```bash
$ git clone https://github.com/satabie/train_wiki_doc2vec.git &&
cd train_wiki_doc2vec &&
python -m venv .venv &&
source .venv/bin/activate.fish &&
pip install -r requirements.txt
```
次にmake_corpus.pyでDBから取ってきたテキストデータを訓練用データに整形して保存する。
```bash
$ python make_corpus.py
```
あとはmodelsディレクトリを作成して、言語を指定してtrainingする。
対応言語は日本語：ja、英語:enのみ
```bash
$ mkdir models
```
```bash
$ python train.py en
```
