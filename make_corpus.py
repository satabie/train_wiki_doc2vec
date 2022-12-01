from modules.manage_dataset import manage_dataset
from gensim.models.doc2vec import Doc2Vec, TaggedDocument


def main():
    text_list = []
    text_list.append(
        'Yahoo Japanなどを\r運営するヤフーの親会社Zホールディングス（以下ZHD）とLINEは11月18日、経営統合することで基本合意したことを正式に発表した。\n11月13日に日本経済新聞などが両社の合併を報じていた。')
    text_list.append('「パン工場」に住むパン作りの名人・ジャムおじさん。彼は“心を持ったあんパン”を作りたいと思っていたが上手くいかずに困っていた。ある夜、夜空の流れ星がパン工場のパン焼き窯に降り注ぐ。この「いのちの星」があんパンに宿り、アンパンマンが誕生したのだった。アンパンマンは、困っている人がいればどこへでも飛んで行き、お腹を空かせて泣いている人には自分の顔を食べさせてくれる正義のヒーロー。そんなアンパンマンをやっつけるために誕生したのが、「バイキン星」からやって来たばいきんまんであった。')
    text_list.append('のび太がお正月をのんびりと過ごしていると、突然、どこからともなくのび太の未来を告げる声が聞こえ、机の引出しの中からドラえもんと、のび太の孫の孫のセワシが現れた。セワシ曰く、のび太は社会に出た後も沢山の不運に見舞われ、会社の倒産が原因で残った莫大な借金によって子孫を困らせているという。そんな悲惨な未来を変えるために、ドラえもんを子守用ロボットとしてのび太のもとへと連れてきたのだった。')
    data_maker = manage_dataset('ja')
    dataset = list(map(data_maker.generate_dataset, text_list))
    trainings = [TaggedDocument(doc, [i]) for i, doc in enumerate(dataset)]
    model = Doc2Vec(documents=trainings)
    model.save('test.model')


if __name__ == "__main__":
    main()
