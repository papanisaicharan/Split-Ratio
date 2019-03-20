# Spliting criteria

This package help to find spliting criteria in C4.5

## Information gain
ID3 uses information gain as its attribute selection measure. This measure is based on
pioneering work by Claude Shannon on information theory, which studied the value or
“information content” of messages. Let node N represent or hold the tuples of partition
D. The attribute with the highest information gain is chosen as the splitting attribute for
node N. This attribute minimizes the information needed to classify the tuples in the
resulting partitions and reflects the least randomness or “impurity” in these partitions.
Such an approach minimizes the expected number of tests needed to classify a given tuple
and guarantees that a simple (but not necessarily the simplest) tree is found.

The expected information needed to classify a tuple in D is given by:

![Info(D) = - \sum_{i=1}^{m} p_{i}\times log_{2}(p_{i})](https://latex.codecogs.com/gif.latex?Info(D)&space;=&space;-&space;\sum_{i=1}^{m}&space;p_{i}\times&space;log_{2}(p_{i}))

where pi is the probability that an arbitrary tuple inDbelongs to classCi and is estimated
by |Ci,D|/|D|. A log function to the base 2 is used, because the information is encoded in
bits. Info(D) is just the average amount of information needed to identify the class label
of a tuple in D. Note that, at this point, the information we have is based solely on the
proportions of tuples of each class. Info(D) is also known as the entropy of D.

Now, suppose we were to partition the tuples in D on some attribute A having v distinct
values, {a1, a2, . . . , av}, as observed from the training data. If A is discrete-valued,
these values correspond directly to the v outcomes of a test on A. Attribute A can be used
to splitDinto v partitions or subsets, {D1, D2, . . . , Dv},whereDj contains those tuples in
D that have outcome aj of A. These partitions would correspond to the branches grown
from node N. Ideally, we would like this partitioning to produce an exact classification of the tuples. That is, we would like for each partition to be pure. However, it is quite
likely that the partitions will be impure (e.g., where a partition may contain a collection
of tuples from different classes rather than from a single class). How much more
information would we still need (after the partitioning) in order to arrive at an exact
classification? This amount is measured by:

![Info_{A}(D)  = \sum_{i=1}^{v} \frac{\left |D_{j}  \right |}{\left |D  \right |}\times Info(D_{j})](https://latex.codecogs.com/gif.latex?Info_{A}(D)&space;=&space;\sum_{i=1}^{v}&space;\frac{\left&space;|D_{j}&space;\right&space;|}{\left&space;|D&space;\right&space;|}\times&space;Info(D_{j}))

The term
|Dj |
|D| acts as the weight of the jth partition. InfoA(D) is the expected information
required to classify a tuple from D based on the partitioning by A. The smaller the
expected information (still) required, the greater the purity of the partitions.
Information gain is defined as the difference between the original information requirement
(i.e., based on just the proportion of classes) and the newrequirement (i.e., obtained
after partitioning on A). That is,

![Gain(A) = Info(D) - Info_{A}(D)](https://latex.codecogs.com/gif.latex?Gain(A)&space;=&space;Info(D)&space;-&space;Info_{A}(D))

In other words, Gain(A) tells us how much would be gained by branching on A. It is the
expected reduction in the information requirement caused by knowing the value of A.
The attribute A with the highest information gain, (Gain(A)), is chosen as the splitting
attribute at node N. This is equivalent to saying that we want to partition on the attribute
A that would do the “best classification,” so that the amount of information still required
to finish classifying the tuples is minimal (i.e., minimum InfoA(D)).

## Gain ratio

C4.5, a successor of ID3, uses an extension to information gain known as gain ratio,
which attempts to overcome this bias. It applies a kind of normalization to information
gain using a “split information” value defined analogously with Info(D) as:

![SplitInfo_{A}(D)  = \sum_{i=1}^{v} \frac{\left |d_{j}  \right |}{\left |d  \right |}\times log_{2}(\frac{\left |d_{j}  \right |}{\left |d  \right |})](https://latex.codecogs.com/gif.latex?SplitInfo_{A}(D)&space;=&space;\sum_{i=1}^{v}&space;\frac{\left&space;|d_{j}&space;\right&space;|}{\left&space;|d&space;\right&space;|}\times&space;log_{2}(\frac{\left&space;|d_{j}&space;\right&space;|}{\left&space;|d&space;\right&space;|}))

This value represents the potential information generated by splitting the training
data set, D, into v partitions, corresponding to the v outcomes of a test on attribute A.
Note that, for each outcome, it considers the number of tuples having that outcome with
respect to the total number of tuples in D. It differs from information gain, which measures
the information with respect to classification that is acquired based on the same
partitioning. The gain ratio is defined as:

![GainRatio(A) = \frac{Gain(A)}{SplitInfo_{A}(D) }](https://latex.codecogs.com/gif.latex?GainRatio(A)&space;=&space;\frac{Gain(A)}{SplitInfo_{A}(D)&space;})

The attribute with the maximum gain ratio is selected as the splitting attribute. Note,
however, that as the split information approaches 0, the ratio becomes unstable. A constraint
is added to avoid this, whereby the information gain of the test selected must be
large—at least as great as the average gain over all tests examined.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install split_ratio
```

## Usage

```python
import split_ratio

p = {"age":["youth","youth","middle_agged","senior","senior","senior","middle_agged","youth","youth","senior","youth","middle_agged","middle_agged","senior"],
                     "student":["no","no","no","no","yes","yes","yes","no","yes","yes","yes","no","yes","no"],
                     "credit_rating":["fair","excellent","fair","fair","fair","excellent","excellent","fair","fair","fair","excellent","excellent","fair","excellent"],
                     "buys_computer":["no","no","yes","yes","yes","no","yes","no","yes","yes","yes","yes","yes","no"],
                     "income":["high","high","high","medium","low","low","low","medium","low","medium","medium","medium","high","medium"]}

complete_db = []
complete_attr = []
for i in p:
    complete_db.append(p[i])
    complete_attr.append(i)
features_values = complete_db[:len(complete_db)-1] 
features_attributes = complete_attr[:len(complete_attr)-1]
target_values = complete_db[len(complete_db)-1]
target_attribute = complete_attr[len(complete_attr)-1]
# print(features_values,features_attributes,target_values,target_attribute)

#now we will take a as age so
a = features_values[0]
D = target_values

# print(a,D)

# info(D) returns the expected information needed to classify a tuple in D
print( split_ratio.info(D) ) # D is the target attribute.

print( split_ratio.infoA(a,D) ) # returns the expected information required to
# classify a tuple from D based on the partitioning by A

print( split_ratio.info_gain(D,A) )#tells us how much would be gained by branching on A.

print( split_ratio.split_infoA(a) )#returns the potential information generated by
# splitting the training data set, D, into v partitions, 
# corresponding to the v outcomes of a test on attribute A.

print( split_ratio.gain_ratio(A,D) )
# The attribute with the maximum gain ratio is selected as the splitting attribute. 
 
```



## License
[MIT](https://choosealicense.com/licenses/mit/)