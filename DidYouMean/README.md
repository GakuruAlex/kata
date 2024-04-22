# DESCRIPTION #

I'm sure, you know Google's "Did you mean ...?", when you entered a search term and mistyped a word. In this kata we want to implement something similar.

You'll get an entered term (lowercase string) and an array of known words (also lowercase strings). Your task is to find out, which word from the dictionary is most similar to the entered one. The similarity is described by the minimum number of letters you have to add, remove or replace in order to get from the entered word to one of the dictionary. The lower the number of required changes, the higher the similarity between each two words.

Same words are obviously the most similar ones. A word that needs one letter to be changed is more similar to another word that needs 2 (or more) letters to be changed. E.g. the mistyped term berr is more similar to beer (1 letter to be replaced) than to barrel (3 letters to be changed in total).

Extend the dictionary in a way, that it is able to return you the most similar word from the list of known words.

## Code Examples ##

fruits = Dictionary(['cherry', 'pineapple', 'melon', 'strawberry', 'raspberry'])
fruits.find_most_similar('strawbery') # must return "strawberry"
fruits.find_most_similar('berry') # must return "cherry"

things = Dictionary(['stars', 'mars', 'wars', 'codec', 'codewars'])
things.find_most_similar('coddwars') # must return "codewars"

languages = Dictionary(['javascript', 'java', 'ruby', 'php', 'python', 'coffeescript'])
languages.find_most_similar('heaven') # must return "java"
languages.find_most_similar('javascript') # must return "javascript" (identical words are obviously the most similar)