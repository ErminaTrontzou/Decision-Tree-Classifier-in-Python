## _Decision-Tree-Classifier-in-Python_


[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

A program that reads and compares specific numeric values of a provided 2D array, creates the questions with the best uncertainty about the **max** value of each attribute , assigns the leaf noads and builds the correct decision tree which provides the percentage of how accurate the result was. It uses : 
- [Python] Obviously 
- [CART]  algorithm


## Purpose
The purpose for me making this project was to gain a bonus for my Machine Learning course in Univercity but my professor could't understand it _(mainly because he still mostly codes in c/c++ )_ so I uploaded it here. I did allot of reasearch for this one to just not share it.

## In a Nutshell
In my particular program I provide an array with musical intruments and some numeric **attributes** about them such as their number of strings, their size and their number of octaves. The last column is a label for the row (the name of the  musical intrument).
Then I split the array into rows so my program can read each one as a data to **generate a question from**.
After that the **root node** receives the whole array as input and after some calculations and true/false questions about the attributes _(each is explained right below)_ , it splits the data to **child nodes**. If there is only one data in a splitted side, then it becomes a **LEAF**.
The process ends when all ends of every question ends with a Leaf.

## How to use

##### OfCourse you can change the whole thing, especially if you know how to code but if you want to use it as is but with your own data then here are the minor changes for you to make :

###### Both the attributes of the array and the condition of the question can be appointed by you by changing my code : 

| Line | Code to Change |
| ------ | ------ |
| 3-9 | The whole array and its values(you can even adjust the size without changing something else) |
| 46 | the '>=' symbol as my program calculates according to the max value |
| 49 | If you changed the above line then here you can simply put your symbol again|
| 196-202 | Again write your new array as given in lines 3-9|


Install the dependencies and devDependencies and start the server.

```sh
cd dillinger
npm i
node app
```

For production environments...

```sh
npm install --production
NODE_ENV=production node app
```
# Not in a Nutshell

#### `def side_handler`



## License

MIT

**Free Software, Hell Yeah!**


   [python]: <https://www.python.org/>
   [CART]: <https://www.geeksforgeeks.org/cart-classification-and-regression-tree-in-machine-learning/>
  
