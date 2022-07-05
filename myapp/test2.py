import MeCab
mecab = MeCab.Tagger()
out = mecab.parse("오늘은 맑은 날씨이다.")
print(out)