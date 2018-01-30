import glob
import json
import chardet
import collections
import operator


for filename in glob.glob('json/*.json'):
    news_content = ''
    with open(filename, 'rb') as file:
        file_data = file.read()
        charset_detector = chardet.detect(file_data)
        file_data_decoded = file_data.decode(charset_detector['encoding'])

        news = json.loads(file_data_decoded)
        for new in news['rss']['channel']['items']:
            news_content += new['description'] + ' '

        counted_words = collections.Counter(news_content.split(' '))
        more_6_letters = {k: v for k, v in counted_words.items() if len(k) > 6}
        top_10_words = dict(sorted(more_6_letters.items(), key = operator.itemgetter(1), reverse = True)[:10])

        print('Топ 10 слов для файла {}: {}, {}, {}, {}, {}, {}, {}, {}, {}, {}.'.format(filename, *top_10_words))
