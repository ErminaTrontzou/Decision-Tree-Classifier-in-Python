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

###### OfCourse you can change the whole thing, especially if you know how to code but if you want to use it as is but with your own data then here are the minor changes for you to make :

##### Both the attributes of the array and the condition of the question can be appointed by you by changing my code : 

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
#### `def n_of_strings_counter(rows)`
##### This function receives as input all the `rows` of the data array and counts how many times the specific label *(the last attribute of each row of my data array)* exists in the array. It **returns** the label and the  number it counted for every element in an array called count with a form `"Label : count number"`.
If a label doesnt already exist in the array `count` then it's value will be `1` else it's value will be it's current + 1.

**Input**
[![input.png](https://i.postimg.cc/d34c5vXG/input.png)](https://postimg.cc/GT8f20bp)
**Return**
[![output.png](https://i.postimg.cc/qqkdcgmk/output.png)](https://postimg.cc/ZBDg4Ytg)

#### `class Question`
##### This class has 3 functions that all work together to generate the best possible questions for every value of every column of the data array. `def match` compares the value of the current element of the column with a threshold *(in my case with a >= condition)*. `__repr__` has a very simple purpose. It is a function that converts the above procedure to a readable printed output : [![output-Question.png](https://i.postimg.cc/tRz5NBJp/output-Question.png)](https://postimg.cc/RqNKMQwD)


# Coming soon
#### `def side_handler(rows, question)`
#### `def gini(rows)`
#### `def info_gain(left, right, current_uncertainty)`
#### `def find_best_split(rows)`
#### `class Leaf`
#### `class Decision_Node`
#### `def build_tree(rows)`
#### `def print_tree(node, spacing="")`
#### `def classify(row, node)`
#### `def print_leaf(counts)`



## License

MIT

**Free Software, Hell Yeah!**


   [python]: <https://www.python.org/>
   [CART]: <https://www.geeksforgeeks.org/cart-classification-and-regression-tree-in-machine-learning/>
  
