from learning import *

#tree = DecisionTreeLearner(iris)


#tree.display()

#dataset = SyntheticRestaurant(200)
#tree = BinaryDecisionTreeLearner(dataset)

print "OURS"
newtree1 = BinaryDecisionTreeLearner(ecoli)
newtree1.display()

print cross_validation(BinaryDecisionTreeLearner, ecoli)

#print "REGULAR"
#newtree2 = DecisionTreeLearner(ecoli)
#newtree2.display()

print cross_validation(DecisionTreeLearner, ecoli)

#newtree = DecisionTreeLearner(abalone)
#newtree.display()
#print cross_validation(DecisionTreeLearner, abalone)

#compare()