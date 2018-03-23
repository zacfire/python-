from bs4 import UnicodeDammit

markup = b"<p>I just \x93love\x94 Microsoft Word\x92s smart quotes</p>"
dammit = UnicodeDammit("Sacr\xc3\xa9 bleu!")
print(dammit,unicode_markup)