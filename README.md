# Trash Classifier ♻
Predict to which container should you throw a particular item. 
**European trash sorting rules (check out the table below).**

![Example of usage](https://github.com/weronikazak/Handy-Trash-Classifier/blob/master/test/metal.gif)

Using:
- OpenCV
- Tensorflow
- Numpy
- Keras
- Scikit
- Android Studio


**TRASH SORTING RULES:**

| Bin's Color | Waste Type  |
| ----------- | ----------- |
| Blue        | Paper       |
| Green       | Glass       |
| Yellow      | Metal       |
| Black       | Mixed       |
| Brown       | Bio         |


### MODEL PERFORMANCE:
![Example of usage](https://github.com/weronikazak/Handy-Trash-Classifier/blob/master/python/performance/accuracy.png)

Training accuracy: 85,20%

Testing accuracy: 83,79%


![Example of usage](https://github.com/weronikazak/Handy-Trash-Classifier/blob/master/python/performance/loss.png)

Training loss: 12,11%

Testing loss: 20,13%



## EXAMPLES:

![Example of usage](https://github.com/weronikazak/Handy-Trash-Classifier/blob/master/test/paper.gif)
![Example of usage](https://github.com/weronikazak/Handy-Trash-Classifier/blob/master/test/plastic.gif)


## TO DO:

[] Merge paper and cardboard images making them one category.

[] Merge plastic and metal images making them one category.

[] Add bio waste.
