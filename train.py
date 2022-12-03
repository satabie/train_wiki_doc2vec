from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import joblib


def main():
    f = open("dataset_en.pkl", "rb")
    dataset = joblib.load(f)
    trainings = [TaggedDocument(doc, [i]) for i, doc in enumerate(dataset)]
    model_en = Doc2Vec(documents=trainings)
    model_en.save('test_en.model')


if __name__ == "__main__":
    main()
