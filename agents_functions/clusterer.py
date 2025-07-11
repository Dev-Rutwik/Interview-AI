import re
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

def preprocess_text(text):
    text = re.sub(r'[^a-zA-Z0-9\\s.,;!?]', '', text.lower())
    tokens = nltk.word_tokenize(text)
    stop_words = set(nltk.corpus.stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    stemmer = nltk.stem.PorterStemmer()
    lemmatizer = nltk.stem.WordNetLemmatizer()
    return ' '.join([lemmatizer.lemmatize(stemmer.stem(word)) for word in tokens])

def cluster_resume_sentences(resume_text):
    sentences = [s.strip() for s in re.split(r'[.!?]', resume_text) if s.strip()]
    processed = [preprocess_text(s) for s in sentences]

    X = TfidfVectorizer().fit_transform(processed)
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    
    clusters = {}
    for i, label in enumerate(kmeans.fit_predict(X)):
        clusters.setdefault(label, []).append(sentences[i])
    return clusters
