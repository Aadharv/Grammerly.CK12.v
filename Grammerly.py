from textblob import TextBlob
v=TextBlob( "Helo I am frim Inida adn i lkie my countery")
p=v.correct()
print(p)

h=TextBlob("Hllo my nmae iz janiter becoz i luv wokring at scool adn cleening flors")
j=h.correct()
print(j)