import webbrowser
import time 
import random
from wonderwords import RandomWord
r=RandomWord()
print("\nStarting!!!")
nsearch=int(input("\nEnter number of search==>"))
i=0
print("\nHang On!!")
while(i<nsearch):
    word1=r.word()
    word2=r.word()
    word3=r.word()
    randomint=random.randint(3,8)
    time.sleep(randomint)
    webbrowser.open("https://www.bing.com/search?q="+word1+"+"+word2+"+"+word3+"&qs=n&form=QBRE&sp=-1&lq=0&pq=m&sc=11-1&sk=&cvid=BD43CEF94CB54B6CBC728896AF0A144A&ghsh=0&ghacc=0&ghpl=")
    i=i+1 
print("\n**ENDED**")
