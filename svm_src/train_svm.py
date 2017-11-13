from svm_lib.svmutil import *
y, x = svm_read_problem('train.1.txt')
yt, xt = svm_read_problem('test.1.txt')
m = svm_train(y, x)
svm_predict(yt, xt, m)
