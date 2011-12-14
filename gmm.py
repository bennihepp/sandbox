import numpy as np

import sklearn
import sklearn.mixture
import sklearn.decomposition

import cPickle
f = open('/g/pepperkok/hepp/cell_objects_COP.pic', 'r')
up = cPickle.Unpickler(f)
original_data = up.load()
f.close()

N = 1000

#def fit_gmm(N, original_data, **kwargs):
    #a = np.arange(original_data.shape[0])
    #np.random.shuffle(a)
    #data = original_data[a[:N]]
    #data = np.asarray(data, dtype=np.float32)

    #gmm = sklearn.mixture.GMM(10, 'full')
    #gmm.fit(data)

    #return gmm, data

#gmm, gmm_data = fit_gmm(N, original_data)

def fit_pca(N, original_data, n_components):
    a = np.arange(original_data.shape[0])
    np.random.shuffle(a)
    data = original_data[a[:N]]
    data = np.asarray(data, dtype=np.float32)

    pca = sklearn.decomposition.PCA(n_components)
    pca.fit(data)

    return pca, data

def fit_dpgmm(N, original_data, **kwargs):
    a = np.arange(original_data.shape[0])
    np.random.shuffle(a)
    data = original_data[a[:N]]
    data = np.asarray(data, dtype=np.float32)

    pca, data = fit_pca(N, original_data, 2)
    data = pca.transform(data)
    print 'pca:', data.shape

    dpgmm = sklearn.mixture.DPGMM(10, cvtype='full', alpha=10000)
    dpgmm.fit(data, n_iter=100)

    Y = dpgmm.predict(data)

    count = 0
    for i,w in enumerate(dpgmm.weights):
        if np.any(Y == i):
            count += 1
            print 'i=%d' % i
    print 'count:', count

    return dpgmm, data, Y

dpgmm, dpgmm_data, Y = fit_dpgmm(N, original_data)
