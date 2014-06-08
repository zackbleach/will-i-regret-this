#!/bin/bash

curl http://www.brainyquote.com/quotes/keywords/regret.html | grep boxyPaddingBig -A 3 > static/quotes.html

for i in {2..17}
do
    echo -- >> static/quotes.html
    curl http://www.brainyquote.com/quotes/keywords/regret_$i.html | grep boxyPaddingBig -A 3 >> static/quotes.html
done

w3m -dump -cols 10000 static/quotes.html | tac > static/quotes.txt
rm static/quotes.html

