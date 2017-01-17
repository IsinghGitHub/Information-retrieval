import csv
import random
import numpy as np
from sklearn import svm
from sklearn.cluster import KMeans
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report


# data attributes
buying_numeralization 	= {"low"	: 0	, "med" : 1	, "high" : 2	, "vhigh" : 3}
maint_numeralization 	= {"low"	: 0	, "med" : 1	, "high" : 2	, "vhigh" : 3}
doors_numeralization 	= {"2" 		: 2	, "3" 	: 3	, "4" 	 : 4	, "5more" : 5}
persons_numeralization 	= {"2" 		: 2	, "4" 	: 4	, "more" : 5}
lug_boot_numeralization = {"small" 	: 0	, "med"	: 1	, "big"  : 2}
safety_numeralization 	= {"low" 	: 0	, "med"	: 1	, "high" : 2}
# class
class_numeralization 	= {"unacc" 	: 0	, "acc" : 1	, "good" : 2	, "vgood" : 3}
# data and predict target
data 	= []
target 	= []

# Read Data and Preprocess
with open('car.data.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		# Numeralization
		row['buying'] 	= buying_numeralization[row['buying']]
		row['maint'] 	= maint_numeralization[row['maint']]
		row['doors'] 	= doors_numeralization[row['doors']]
		row['persons'] 	= persons_numeralization[row['persons']]
		row['lug_boot'] = lug_boot_numeralization[row['lug_boot']]
		row['safety'] 	= safety_numeralization[row['safety']]
		row['class'] 	= class_numeralization[row['class']]
		
		# print(row['buying'], row['maint'], row['doors'], row['persons'], row['lug_boot'], row['safety'])
		
		data.append([row['buying'], row['maint'], row['doors'], row['persons'], row['lug_boot'], row['safety']])
		target.append(row['class'])
# shuffle
combine_shuffle = list(zip(data, target))
random.shuffle(combine_shuffle)
data, target	= zip(*combine_shuffle)

# Split Data into Train and Test
SPLIT_THRESHOLD = len(data) * 6 / 10
x_train, x_test	= data	[0 : SPLIT_THRESHOLD], data	 [SPLIT_THRESHOLD:]
y_train, y_test	= target[0 : SPLIT_THRESHOLD], target[SPLIT_THRESHOLD:]

print "AdaBoast"
# AdaBoast
clf = GradientBoostingClassifier(n_estimators=100, 
								learning_rate=0.01,
								max_depth=1, 
								random_state=0).fit(x_train, y_train)
								
print mean_squared_error(y_test, clf.predict(x_test)) 				
print accuracy_score(y_test, clf.predict(x_test))
print confusion_matrix(y_test, clf.predict(x_test))
print classification_report(y_test, clf.predict(x_test))

print "SVM"
# SVM
clf = svm.SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
			decision_function_shape='ovo', degree=3, gamma='auto', kernel='rbf',
			max_iter=-1, probability=False, random_state=False, shrinking=True,
			tol=0.001, verbose=False)
clf.fit(x_train, y_train) 
								
print mean_squared_error(y_test, clf.predict(x_test)) 							
print accuracy_score(y_test, clf.predict(x_test))
print confusion_matrix(y_test, clf.predict(x_test))
print classification_report(y_test, clf.predict(x_test))


print "KMeans"
kmeans = KMeans(n_clusters=4, random_state=0).fit(x_train + x_test)
print kmeans.labels_
print kmeans.cluster_centers_