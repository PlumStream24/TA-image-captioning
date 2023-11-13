import string
from nltk.translate.bleu_score import corpus_bleu, SmoothingFunction

token_path = "Flickr8K_Text/Flickr8k.token.txt"
trans_path = 'backtrans_output.txt'

table = str.maketrans('', '', string.punctuation)
bleu_w = {
        "bleu-1": [1.0],
        "bleu-2": [0.5, 0.5],
        "bleu-3": [0.333, 0.333, 0.333],
        "bleu-4": [0.25, 0.25, 0.25, 0.25]
    }

def avg(lst): 
    return sum(lst) / len(lst) 

with open(token_path, "r") as f:
    data = []
    for line in f.readlines() :
        tokens = line.split()
        img_name, caption_words = tokens[0].split("#")[0], tokens[1:]
        caption_words = [token.strip().lower().translate(table) for token in caption_words]
        data.append(caption_words)

with open(trans_path, "r") as f:
    trans_data = []
    for line in f.readlines() :
        tokens = line.split()
        img_name, caption_words = tokens[0].split("#")[0], tokens[1:]
        caption_words = [token.strip().lower().translate(table) for token in caption_words]
        trans_data.append(caption_words)

chencherry = SmoothingFunction()
bleu = {"b1": [],
        "b2": [],
        "b3": [],
        "b4": []
        }

for i in range(len(data)):
    bleu_1 = corpus_bleu([[data[i]]], [trans_data[i]], weights=bleu_w["bleu-1"], smoothing_function=chencherry.method3) * 100
    bleu_2 = corpus_bleu([[data[i]]], [trans_data[i]], weights=bleu_w["bleu-2"], smoothing_function=chencherry.method3) * 100
    bleu_3 = corpus_bleu([[data[i]]], [trans_data[i]], weights=bleu_w["bleu-3"], smoothing_function=chencherry.method3) * 100
    bleu_4 = corpus_bleu([[data[i]]], [trans_data[i]], weights=bleu_w["bleu-4"], smoothing_function=chencherry.method3) * 100
    bleu["b1"].append(bleu_1)
    bleu["b2"].append(bleu_2)
    bleu["b3"].append(bleu_3)
    bleu["b4"].append(bleu_4)

print(avg(bleu["b1"]), avg(bleu["b2"]), avg(bleu["b3"]), avg(bleu["b4"]))
