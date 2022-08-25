import keras_ocr

detector = keras_ocr.detection.Detector(weights='clovaai_general')
recognizer = keras_ocr.recognition.Recognizer(
    weights='kurapan'
)

pipeline = keras_ocr.pipeline.Pipeline(detector=detector, recognizer=recognizer)
# # Get a set of three example images
# images = [
#     # "11_year_old_boy_first_week_at_oak_hill.jpg"
#     keras_ocr.tools.read(url) for url in [
#     "https://fileuploadapp.blob.core.windows.net/tutorial-container/sdfadfas.png"
#     ]
# ]
from spellchecker import SpellChecker
 
# spell = SpellChecker()
# prediction_groups = pipeline.recognize(images)

# score = 0

# for a in prediction_groups[0]:
#     word = a[0]
#     corr_word = spell.correction(word)
    
#     if(word==corr_word):
#         score+=1

#     print(a[0],corr_word)
# print(score, len(prediction_groups[0]))

def make_pred(url):
    images = [keras_ocr.tools.read(url)]
    spell = SpellChecker()
    prediction_groups = pipeline.recognize(images)
    score = 0

    for a in prediction_groups[0]:
        word = a[0]
        corr_word = spell.correction(word)
        
        if(word==corr_word):
            score+=1

        # print(a[0],corr_word)
    return(score, len(prediction_groups[0]))

# make_pred("https://fileuploadapp.blob.core.windows.net/tutorial-container/sdfadfas.png")