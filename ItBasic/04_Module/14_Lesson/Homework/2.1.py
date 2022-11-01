
text = '\"Don’t compare yourself with anyone in this world… if you do so, you are insulting yourself.\"' "\"Bill " \
       "Gates\" "

def textFormat(text):
    text = text.split('."')
    print("Цитата: {}".format(text[0]))
    print("Автор: {}".format(text[1]))

textFormat(text)



