import re
sample = ["hello ,  how are you?",
        "i dont know",
        "contact me at lab@yahoo.com",
        "",
        "i can't log in."
        ]

for text in sample:
    ws = text.split()
    words = re.findall(r"\b\w+\b", text, flags=re.UNICODE)
    print(repr(text), "whitespace:", ws, len(ws))
    print("word_like:", words, len(words))
    
assert re.findall(r"\b\w+\b", "") == []
  
# optinal modle comparison; first use download the model

from sentence_transformers import sentencetransformer


model = sentencetransformer(
    "sentence-transformers/all-miniLM=l6-v2",
    device = "cpu"
    
)

for text in sample[:2]:
    print(text, model.tokenizer.tokenize(text))