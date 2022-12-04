from modules.DatasetManager import DatasetManager
from modules.dbManager import DBManager
import gc
import joblib

DB_HOST = "localhost"
DB_PORT = "5432"
DB_USER = "postgres"
DB_PASS = "postgres"
DB_NAME = "wikipedia_featured_articles"


def main():
    """
    DBからテキストの読み込みを行う
    """
    # english
    text_list_en = get_FAtext('en')
    data_maker_en = DatasetManager('en')
    dataset_en = list(map(data_maker_en.generate_dataset, text_list_en[0:4]))
    with open('dataset/dataset_en.pkl', 'wb') as f:
        joblib.dump(dataset_en, f)
    # メモリの解放
    del dataset_en
    del text_list_en
    gc.collect()

    # japanese
    text_list_ja = get_FAtext('ja')
    data_maker_ja = DatasetManager('ja')
    dataset_ja = list(map(data_maker_ja.generate_dataset, text_list_ja[0:4]))
    with open('dataset/dataset_ja.pkl', 'wb') as f:
        joblib.dump(dataset_ja, f)


def get_FAtext(lang):
    db_manager = DBManager(DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASS)
    table_names = db_manager.fetch_tablenames()
    text_list = []
    for table_taple in table_names:
        table_name = table_taple[0]

        if lang == 'en':
            query = f"SELECT en_text FROM {table_name} WHERE en_text != 'null'"  # 変更点
            text_taple = db_manager.select(query)
        elif lang == 'ja':
            query = f"SELECT ja_text FROM {table_name} WHERE ja_text != 'null'"  # 変更点
            text_taple = db_manager.select(query)

        for text in text_taple:
            text = text[0]
            text_list.append(text)
    return text_list


if __name__ == "__main__":
    main()
