# Fizz Buzz!

**What I tried first.**
 - First i tried using your examples as source code but i couldn't get it to work. i tried really just renaming and messing with the syntax hoping it would work. And it would almost work. but it would always print numbers 1 - 100 then print at the very end FizzBuzz.
- I stoped once i got to this point.

*for (let number = 0; number <= 100; number = number + 1) console.log (number)

  let num = Number

  if (num / 3)
    console.log ("Fizz")
   else if (num / 5 )
    console.log ("Buzz")
   else if (num / 3 && 5 )
    console.log ("Fizz Buzz");
   else (num)
     console.log (num);*
**Second attempt with fresh eyes.**
-so i then took a break and decided to not use your source code. after reviewing my notes i realized that the pyramid project could help. mainly the counting system. it's more mathematical and to me makes more sense than

*for (let number = 0; number <= 100; number = number + 1) console.log (number)*

-at least to me.


**New Formula**
- *for (var i = 1; i < 100; i++) console.log(i);*

- How ever with the new formula for counting it would only go up to 99 so i had to make it go up by one more so i added an equal sign so it reads *for (var i = 1; i <= 100; i++) console.log(i);*

- I couldn't figure out how to divide in if/else statements so i looked up how and found something that got me thinking about modulos (%)

-  After reading a little more on geeksforgeeks on how modulos work in js i realized i can use it to divide in the if/else statements and if they divide to 0 then they can be fizz buzz or fizzbuzz.

- After manipulating the first attempt at this i got a little bit better at writing if statements. and some of my tests running my code on chrome i noticed the brackets in your if/else statement would give me weird errors until i got rid of them. So when i got to my making of the if/else statement i used your code as a reference but i fully typed out my line of code.

- When i got to the fizz buzz part it stumped me for a bit. until i looked at your little hint of to do some basic math and realized if it was divisible by both 3 and 5 then i had to be divisible by a multiple of 15.

- Once i got the if/else statement i thought my code would be done. but no. it's not even showing up. so i try some new stuff and nothing still works. then google starts acting weird. then chrome crashes like it normally does. once its back up again. my code is now printing but isn't printing correctly. I'm getting the same results as before *print numbers 1 - 100 then print at the very end FizzBuzz.*. This time i go back into my code and notice a few errors. nothing on the if/else statements has a ";" and the console print is still in the counting line before the if/else statement.

- I started to get weird errors on things not being defined. then i realized that because i'm not the best speller i spent console all differently and none of them were right. after fixing my bad spelling my code was printing all the fizz and buzz but no fizzbuzz. it is here i realized the nature of computers and how they cant abstract things. the fizz buzz has to be the if statement if it's not then the others will always be considered first.

- I test it out and it works!


##Code Used

- *let num = Number(prompt("Pick a number between 1 and 12"));

if (num < 3) {
  console.log ("Costard");
} else if (num < 6) {
  console.log ("Dogberry");
} else if (num < 8) {
  console.log ("Falstaff");
} else if (num < 10) {
  console.log ("Feste");
} else {
    console.log ("Puck")
}*


**Found on github under**
- *rdwrome/LMSC261-SP20/Lesson-05Memory/jsexamples/chainoffools.js*

## Inspired code Used

- *int main(){
  for (int i = 0; i < 10 ; i++)*

**Found on github under**

- *rdwrome/LMSC261-SP20/Lesson-04Data/thinkoutside.c*
