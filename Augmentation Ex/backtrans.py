'''
import time
from googletrans import Translator

translator = Translator(raise_exception=True)
token_path = "dataset_captioning/Flickr8K_Text/Flickr8k.token.txt"

#from google.cloud import translate_v2 as translate
#translator= translate.Client()

with open(token_path, "r") as f:
    data = []
    for line in f.readlines() :
        tokens = line.split()
        img_name, caption_words = tokens[0].split("#")[0], tokens[1:]
        pair = (img_name, ' '.join(caption_words))
        data.append(pair)

backtrans_cap = []
for cap in data:
    #result = translator.translate(cap[1], source_language='id', target_language='en')
    #back_result = translator.translate(result["translatedText"], source_language='en', target_language='id')
    result = translator.translate(cap[1], src='id', dest='en')
    back_result = translator.translate(result.text, src='en', dest='id')
    backtrans_cap.append(cap[0] + back_result.text)

    time.sleep(0.5)

with open('output.txt', 'w') as f:
    for cap in backtrans_cap:
        f.write("%s\n" % cap)
'''
data = []
with open('output.txt', 'r') as f:
    i = 6
    for line in f.readlines() :
        tokens = line.split('.jpg')
        tokens[0] = tokens[0] + '.jpg#' + str(i)
        new_line = ' '.join(tokens)

        if (i == 10) :
            i = 6
        else :
            i += 1
        
        data.append(new_line)
with open('new_output.txt', 'w') as f:
    for cap in data:
        f.write("%s" % cap)
