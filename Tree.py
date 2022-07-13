                            #Array assignment
#----------------------------------------------------------------------------- 
instruments= [
        [0.9, 4, 6  ,"Guitar"],
        [0.3, 2, 8  ,"Violin"],
        [0.5, 2, 4  ,"Ukulele"],
        [0.8, 3, 4  ,"Bass"],
        [1.8,6.5,47 ,"Harp"],
        [1.5, 4, 4  ,"Cello"]]

labels = ["Size", "Octaves", "Num_of_Strings", "Name"]
#-----------------------------------------------------------------------------


       #Counts the number of each type of tester in a dataset
#----------------------------------------------------------------------------- 
def n_of_strings_counter(rows):
    counts = {}
    for row in rows:
        label = row[-1]
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    return counts
#print(n_of_strings_counter(instruments))
#----------------------------------------------------------------------------- 


                      #Test if a value is numeric
#-------------------------------------------------------------------- 
def is_numeric(value):
    return isinstance(value, int) or isinstance(value, float)
#-------------------------------------------------------------------- 


 #Assignment of values, Comparison of values with tester, Print of Questions
#-----------------------------------------------------------------------------
class Question:
    def __init__(self, column, value):  
        #This will help the threshold to send the match to the right side
        self.column = column
        self.value = value

    def match(self, tester):
        val = tester[self.column]
        return val >= self.value
      
    def __repr__(self):
        condition = ">="
        return "Is %s %s %s ?" % (
            labels[self.column], condition, str(self.value))
 #-----------------------------------------------------------------------------      

         #It defines whether the match will go to true_row or false_row
#-----------------------------------------------------------------------------
def side_handler(rows, question):
    true_rows, false_rows = [], []
    for row in rows:
        if question.match(row):
            true_rows.append(row)
        else:
            false_rows.append(row)
    return true_rows, false_rows 
#-----------------------------------------------------------------------------


        #It quantifies the uncertainty of the whole intruments array
#-----------------------------------------------------------------------------
def gini(rows):
    counts = n_of_strings_counter(rows)
    uncertainty = 1
    
    for lbl in counts:
        prob_of_lbl = counts[lbl] / float(len(rows))
        #1-(1/6)
        uncertainty -= prob_of_lbl**2 
    return uncertainty
#print(gini(instruments)) = 0.833333 ~ 0.8
#-----------------------------------------------------------------------------


            #Quantifies the uncertainty of every question
#-----------------------------------------------------------------------------
def info_gain(left, right, current_uncertainty):
    p = float(len(left)) / (len(left) + len(right))
    return current_uncertainty - p * gini(left) - (1 - p) * gini(right) #entropy
#-----------------------------------------------------------------------------


            #Finds the question with the best uncertainty reducer
#-----------------------------------------------------------------------------
def find_best_split(rows):
    best_gain = 0  # keep track of the best information gain
    best_question = None  # keep train of the feature that produced it
    current_uncertainty = gini(rows)
    n_features = len(rows[0]) - 1  # number of columns
    for col in range(n_features):  # for each feature
        values = set([row[col] for row in rows])  # unique values in the column
        for val in values:  # for each value
            question = Question(col, val)
            true_rows,false_rows  = side_handler(rows, question)
            if len(true_rows) == 0 or len(false_rows) == 0: # Skip this split if it doesn't divide 
                continue
            gain = info_gain(true_rows, false_rows, current_uncertainty) # Calculate the information gain from this split
            if gain >= best_gain:
                best_gain, best_question = gain, question
    return best_gain, best_question
#-----------------------------------------------------------------------------


                         #Assigns the Leaf Node
#-----------------------------------------------------------------------------
class Leaf:
    def __init__(self, rows):
        self.predictions =n_of_strings_counter(rows)
#-----------------------------------------------------------------------------

                    #Assign values to the rhombus
#-----------------------------------------------------------------------------
class Decision_Node:
    def __init__(self,question,true_branch,false_branch):
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch
#-----------------------------------------------------------------------------


                            #Tree Builder
#-----------------------------------------------------------------------------
def build_tree(rows):
    gain, question = find_best_split(rows)

    if gain == 0:
        return Leaf(rows)
    true_rows,false_rows  = side_handler(rows, question)

    true_branch = build_tree(true_rows)
    false_branch = build_tree(false_rows)
    return Decision_Node(question, true_branch, false_branch)
#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------
def print_tree(node, spacing=""):

    #Leaf
    if isinstance(node, Leaf):
        print (spacing + "Predict", node.predictions)
        return

    #Question
    print (spacing + str(node.question))

    #True_row
    print(spacing + "True:")
    print_tree(node.true_branch, spacing + "  ")

    #False_row
    print(spacing +"False:")
    
    print_tree(node.false_branch, spacing + "  ")
#-----------------------------------------------------------------------------



#-----------------------------------------------------------------------------
def classify(row, node):
    # Base case: we've reached a leaf
    if isinstance(node, Leaf):
        return node.predictions

    if node.question.match(row):
        return classify(row, node.true_branch)
    else:
        return classify(row, node.false_branch)
#-----------------------------------------------------------------------------

                            #Prediction Counter
#-----------------------------------------------------------------------------
def print_leaf(counts):
    total = sum(counts.values()) * 1.0
    probs = {}
    for lbl in counts.keys():
        probs[lbl] = str(int(counts[lbl] / total * 100)) + "%"
    return probs
#-----------------------------------------------------------------------------

                            #Evaluation of the tree
#-----------------------------------------------------------------------------
if __name__ == '__main__':

    my_tree = build_tree(instruments)

    print_tree(my_tree)

    instruments= [
        [0.9, 4, 6  ,"Guitar"],
        [0.3, 2, 8  ,"Violin"],
        [0.5, 2, 4  ,"Ukulele"],
        [0.8, 3, 4  ,"Bass"],
        [1.8,6.5,47 ,"Harp"],
        [1.5, 4, 4  ,"Cello"]]

    for row in instruments:
        print ("Actual: %s. Predicted: %s" % (row[-1], print_leaf(classify(row, my_tree))))
#-----------------------------------------------------------------------------