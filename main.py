import os
import urllib
# from concurrent.futures._base import as_completed
from concurrent.futures.thread import ThreadPoolExecutor

import eng_to_ipa as ipa
from google_trans_new import google_translator
import translators
import requests
from bs4 import BeautifulSoup as BS
import time
import pandas as pd
from tqdm import tqdm

# TARGET LANGUAGE SETTINGS
TARGET_LANGUAGE = 'ru'


def getRow(word):
    global TARGET_LANGUAGE
    try:
        transcrypt = ipa.convert(word)
        try:
            translator = google_translator()
            translation = translator.translate(word, lang_tgt=TARGET_LANGUAGE)
        except:
            try:
                translation = translators.deepl(word, from_language='en', to_language=TARGET_LANGUAGE)
            except:
                try:
                    translation = translators.bing(word, from_language='en', to_language=TARGET_LANGUAGE)
                except:
                    try:
                        translation = translators.baidu(word, from_language='en', to_language=TARGET_LANGUAGE)
                    except:
                        translation = 'not available'
        try:
            r = requests.post("https://www.wordhippo.com/what-is/process-form.html",
                              data={'word': word,
                                    'action': 'Sentences'
                                    })
            soup = BS(r.text, features="html.parser")
            sentence = soup.findAll('tr', {'id': 'gexv2row1'})[0].findAll('td')[0].text
        except:
            try:
                r = urllib.request.urlopen('https://sentence.yourdictionary.com/' + word).read().decode("utf8")
                soup = BS(r, features="html.parser")
                sentence = soup.findAll('div', {'class': 'sentence-item'})[0].text
            except:
                sentence = 'not available'
        # i += 1
        # printProgressBar(i, number_of_words, prefix='Progress:', suffix='Complete', length=50)
        return {
            'word': word,
            'transcrypt': transcrypt,
            'translation': translation,
            'sentence': sentence
        }
    except:
        pass


print('type in words for glossary')
print('enter when finish')
words = list()
inp = input()
while inp != '':
    words.append(inp)
    inp = input()

print('processing, please wait...')

start = time.time()

data = {
    'word': [],
    'transcrypt': [],
    'translation': [],
    'sentence': []
}
df = pd.DataFrame(data)

with ThreadPoolExecutor(max_workers=20) as executor:
    results = list(tqdm(executor.map(getRow, words), total=len(words)))

print('processed. saving, please wait...')

for result in results:
    df = df.append(result, ignore_index=True)

print('done in', time.time() - start, 'sec')

output_file_name = "glossary.xlsx"

if os.path.isfile(output_file_name):
    old_df = pd.read_excel(output_file_name)
    df = pd.concat([old_df, df], ignore_index=True)
    df.to_excel(output_file_name, index=False)
    print('updated glossary.xlsx glossary with requested words')
else:
    df.to_excel(output_file_name, index=False)
    print('created glossary.xlsx glossary with requested words')
inp = input()
