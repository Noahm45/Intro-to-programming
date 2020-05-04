so for this project i decided to try and make a fundamental stock valuation software program.
I reasserted as much as i could and watched and read many tutorials and how too. by the end of it i was aware of my limitations knowledge wise and understood why a data science degree is a good idea for these types of projects.
my first hurdle was weather i wanted to use an api or not. i looked at many apis, as well as ways to have your computer look at data thats from a web brouser and and pulls its numbers from there. I tried the web pulling methood first, and despite multiple videos and articals i couldn't get it to work. then i tried using simfin, but couldn't figure out how to use it. then i found alpaca and finviz, and i used them both. Alpaca is the host for the actually buying and selling of equity. and finviz is where were pulling the data from.

#ALPACA
alpaca was a little difficult to figure out how to download and import and then use to buy and sell equity. for the download i used there github and followed directions. as for the usage and importation, i watched the top video found on alpaca's website found here (https://alpaca.markets/docs/get-started-with-alpaca/tutorial-videos/)

#Imports
I imported pandas as pd, this allowed me to write neater code with few lines.
I imported beautiful soup to do some analysis and some graphing.
i imported requests so i can request my comp to go to certain websites.
i imported Alpaca. for buying and selling equity
and i imported json, for a standard for data display

then i uploaded my equations and made them in a code format, it has certain perimeters that it looks at and calculates the values, then theres a filter at the end that has a range of numbers that normally good companies will have in each area, and will filter out companies that don't meet these standards i have set.

at the end i put where you can buy the companies that make it through the filter, you have complete control on the volume and order type as well.

#kinks
BS4 is not working thus making the calculator portion of the program not workable. i have tried updating bs4, i have uninstalled it and reinstalled it. and nothing seems to work. how ever it will still run through the companies it just wont calculate any of them.

#what i learned.
i learned what and how pip is used. i learned about api usage, and how much more i need to know about them to make this process more fluid. there's always more than one way to do something. api's aren't necessary but help a lot. git hub is used for literally everything. most resources on this subject are ether not for beginners, or very outdated. and how tricky it is to write code for numbers that are pulled.  

#code used
alpaca api code can be found on the first video, all code from that video is used. I used it to get the Alpaca api to work. found at https://alpaca.markets/docs/get-started-with-alpaca/tutorial-videos/

calculation code can be found at https://blog.quantinsti.com/quantitative-value-investing-strategy-python/
this code was the foundation, but it did have some odd numbers in the calculations that i fixed, as well as some errors that idle reported as syntax errors, so its cleaned up and has improvement in the calibration of the numbers.
