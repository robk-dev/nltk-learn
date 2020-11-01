import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train = state_union.raw('2005-GWBush.txt')
sample = state_union.raw('2006-GWBush.txt')
custom_sent_tokenizer = PunktSentenceTokenizer(train)

tokenized = custom_sent_tokenizer.tokenize(sample)

words = nltk.word_tokenize(tokenized[0])
tagged = nltk.pos_tag(words)
print(tagged)


# # chunking
# def process_content():
#     try:
#         for i in tokenized:
#             words = nltk.word_tokenize(i)
#             tagged = nltk.pos_tag(words)
#             chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?} """
            
#             chunkParser = nltk.RegexpParser(chunkGram)
#             chunked = chunkParser.parse(tagged)
            
#             print(chunked)
            

#     except Exception as e:
#         print(str(e))
        
# process_content()

# # chinking
# def process_content():
#     try:
#         for i in tokenized[5:50]:
#             words = nltk.word_tokenize(i)
#             tagged = nltk.pos_tag(words)
#             chunkGram = r"""Chunk: {<.*>+}
#                                     }<VB.?|IN|DT|TO>+{"""
            
#             chunkParser = nltk.RegexpParser(chunkGram)
#             chunked = chunkParser.parse(tagged)
            
#             chunked.draw()
            

#     except Exception as e:
#         print(str(e))
        
# process_content()


def process_content():
    try:
        for i in tokenized[5:50]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            
            named_entity = nltk.ne_chunk(tagged)
            
            named_entity.draw()
            

    except Exception as e:
        print(str(e))
        
process_content()