from deep_translator import GoogleTranslator

t = GoogleTranslator(
    source="auto",
    target="en"
) 

r = t.translate("Kaise ho")

print(r)