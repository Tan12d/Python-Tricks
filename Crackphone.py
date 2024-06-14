import phonenumbers
from phonenumbers import geocoder

ph1 = phonenumbers.parse("+919680644586")

print(geocoder.description_for_number(ph1, "en"))  


