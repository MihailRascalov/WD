#Napisz skrypt, gdzie w zmiennej string zapiszesz fragment tekstu piosenki z powtarzającymi
#się słowami np. "la la la". Następnie użyj odpowiedniej funkcji, która zliczy występowanie
#słowa "la". (trzeba użyć metody count)

fragment_of_the_song_lyrics = """
I'm covering my ears like a kid
When your words mean nothing, I go la la la
I'm turning up the volume when you speak
'Cause if my heart can't stop it, I'll find a way to block it, I go
Na na, la la la la la, na na na na na,
La la, na na, la la la la la, na na na na na,
I'll find a way to block it, I go
La la, na na, la la la la la, na na na na na,
La la, na na, la la la la la, na na na na na.
"""

word_to_count = "na na na"
count = fragment_of_the_song_lyrics.count(word_to_count)

print("Word \"" + word_to_count + "\" occurred " + str(count) + " times.")