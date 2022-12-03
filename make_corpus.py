from modules.manage_dataset import manage_dataset
import gc
import joblib


def main():
    """
    DBからテキストの読み込みを行う
    """

    text_list_en = [
        "The quick brown fox jumped over the lazy dog. The fox was very agile and managed to avoid the dog's attempts to catch it. The fox eventually reached the other side of the field and disappeared into the forest.",
        'I am a large language model trained by OpenAI. I am not capable of browsing the internet, so my knowledge is limited to what I was trained on. I can assist with many topics, but I am not perfect and may not always provide the correct answers.',
        'I am not capable of browsing the internet, so my knowledge is limited to what I was trained on. My training data includes a wide range of written text, so I can assist with many topics. Please let me know if you have any questions.'
    ]
    # english
    data_maker_en = manage_dataset('en')
    dataset_en = list(map(data_maker_en.generate_dataset, text_list_en))
    with open('dataset_en.pkl', 'wb') as f:
        joblib.dump(dataset_en, f)
    # メモリの解放
    del dataset_en
    del text_list_en
    gc.collect()

    # japanese
    text_list_ja = [
        'Yahoo Japanなどを\r運営するヤフーの親会社Zホールディングス（以下ZHD）とLINEは11月18日、経営統合することで基本合意したことを正式に発表した。\n11月13日に日本経済新聞などが両社の合併を報じていた。',
        '「パン工場」に住むパン作りの名人・ジャムおじさん。彼は“心を持ったあんパン”を作りたいと思っていたが上手くいかずに困っていた。ある夜、夜空の流れ星がパン工場のパン焼き窯に降り注ぐ。この「いのちの星」があんパンに宿り、アンパンマンが誕生したのだった。アンパンマンは、困っている人がいればどこへでも飛んで行き、お腹を空かせて泣いている人には自分の顔を食べさせてくれる正義のヒーロー。そんなアンパンマンをやっつけるために誕生したのが、「バイキン星」からやって来たばいきんまんであった。',
        'のび太がお正月をのんびりと過ごしていると、突然、どこからともなくのび太の未来を告げる声が聞こえ、机の引出しの中からドラえもんと、のび太の孫の孫のセワシが現れた。セワシ曰く、のび太は社会に出た後も沢山の不運に見舞われ、会社の倒産が原因で残った莫大な借金によって子孫を困らせているという。そんな悲惨な未来を変えるために、ドラえもんを子守用ロボットとしてのび太のもとへと連れてきたのだった。'
    ]

    data_maker_ja = manage_dataset('ja')
    dataset_ja = list(map(data_maker_ja.generate_dataset, text_list_ja))
    with open('dataset_ja.pkl', 'wb') as f:
        joblib.dump(dataset_ja, f)


if __name__ == "__main__":
    main()
