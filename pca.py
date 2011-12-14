import numpy as np

import sklearn
import sklearn.decomposition

def test_cluster_kmeans(repeat, runs, data, k):

    np.random.seed( int( time.time() ) )

    clocks = np.empty( ( repeat, runs ) )
    times = np.empty( ( repeat, runs ) )

    for i in xrange( repeat ):
        KMeans = sklearn.cluster.KMeans(k)
        for j in xrange( runs ):
            t1 = time.time()
            c1 = time.clock()
            KMeans.fit(data)
            c2 = time.clock()
            t2 = time.time()
            dt = t2 - t1
            dc = c2 - c1
            clocks[ i, j ] = c2 - c1
            times[ i, j ] = t2 - t1

    mean_clock = np.mean( clocks )
    std_clock = np.std( clocks )
    mean_time = np.mean( times )
    std_time = np.std( times )

    print '%d objects, %d features, %d clusters: clocks=%f +- %f, times=%f +- %f' % (data.shape[0], data.shape[1], k, mean_clock, std_clock, mean_time, std_time)
    if log_file is not None:
        print >> log_file, '%d objects, %d features, %d clusters: clocks=%f +- %f, times=%f +- %f' % (data.shape[0], data.shape[1], k, mean_clock, std_clock, mean_time, std_time)

    return mean_time, std_time, mean_clock, std_clock

import cPickle
f = open('/g/pepperkok/hepp/cell_objects_COP.pic', 'r')
up = cPickle.Unpickler(f)
original_data = up.load()
f.close()

N = 1000

#def fit_pca(N, original_data):
    #a = np.arange(original_data.shape[0])
    #np.random.shuffle(a)
    #data = original_data[a[:N]]
    #data = np.asarray(data, dtype=np.float32)

    #pca = sklearn.decomposition.PCA()
    #pca.fit(data)

    #return pca, data

#pca, data = fit_pca(N, original_data)

def fit_kpca(N, original_data, kernel='rbf'):
    a = np.arange(original_data.shape[0])
    np.random.shuffle(a)
    data = original_data[a[:N]]
    data = np.asarray(data, dtype=np.float32)

    kpca = sklearn.decomposition.KernelPCA(kernel=kernel)
    kpca.fit(data)

    return kpca, data

kpca, data = fit_kpca(N, original_data)
