import numpy as np

from sklearn import svm, metrics, cross_validation
import matplotlib

N = 2000
K = 100
D = 3

def create_dataset(N, D, labels=None):
    if labels == None:
        labels = [0, 1, 2]
    alpha = [0.3, 0.7, 0.0]
    mu_1 = np.array([0.0] * D)
    mu_2 = np.array([20.0] * D)
    mu_3 = np.array([-2.0] * D)
    sigma_1 = 1.0 * np.identity(D)
    sigma_2 = 1.0 * np.identity(D)
    sigma_3 = 1.0 * np.identity(D)
    X1 = np.random.multivariate_normal(mu_1, sigma_1, int(np.round(N * alpha[0])))
    X2 = np.random.multivariate_normal(mu_2, sigma_2, int(np.round(N * alpha[1])))
    X3 = np.random.multivariate_normal(mu_3, sigma_3, int(np.round(N * alpha[2])))
    Y1 = labels[0] * np.ones((X1.shape[0],), dtype=int)
    Y2 = labels[1] * np.ones((X2.shape[0],), dtype=int)
    Y3 = labels[2] * np.ones((X3.shape[0],), dtype=int)
    X = np.vstack([X1, X2, X3])
    Y = np.hstack([Y1, Y2, Y3])
    return X, Y, (X1, X2, X3), (Y1, Y2, X3)

svm = svm.SVC(kernel='linear')

data, labels, (X1, X2, X3), (Y1, Y2, Y3) = create_dataset(N, D, labels=[0,1,2])
#indices = np.arange(data.shape[0], dtype=int)
#np.random.shuffle(indices)
#train_X, train_Y = data[indices[:K]], labels[indices[:K]]
#test_X, test_Y = data[indices[K:]], labels[indices[K:]]

#svm.fit(train_X, train_Y)

#print svm.score(X2, Y2)

#bs = cross_validation.Bootstrap(X1.shape[0], 9)
#scores = cross_validation.cross_val_score(
    #svm, X1, Y1, cv=bs)#, score_func=metrics.f1_score)

#print 'score: %f +- %f' % (scores.mean(), scores.std())

#pred_Y = svm.predict(test_X)

#print metrics.precision_score(test_Y, pred_Y)
#print metrics.recall_score(test_Y, pred_Y)
#print metrics.f1_score(test_Y, pred_Y)

#pred_Y = svm.predict(X1)

#print metrics.precision_score(Y1, pred_Y)
#print metrics.recall_score(Y1, pred_Y)
#print metrics.f1_score(Y1, pred_Y)

alpha_arr = []
for label in np.unique(labels):
    n = np.sum(labels == label)
    alpha_arr.append(n / float(labels.shape[0]))
alpha_arr = np.array(alpha_arr)
alpha = np.max(alpha_arr)
print alpha

bs = cross_validation.Bootstrap(data.shape[0], 3)
for train_indices, test_indices in bs:
    svm.fit(data[train_indices], labels[train_indices])
    score = svm.score(data[test_indices], labels[test_indices])
    print score, (score - alpha) / (1 - alpha)
    #pred = svm.predict(data[test_indices])
