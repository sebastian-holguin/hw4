import numpy as np

# creating base numbers
def markov_chains(n1, N1):
    n = n1
    N = N1

    # Creating the first array that'll hold numbers n x n
    P = np.random.rand(n, n)
    # Creating the second array that'll hold the initial state.
    p = np.random.rand(n)

    # .sum makes sure that the sum of the entries is equal to one, from the start to
    # the number of entries (newaxis). This is the same method I used for the previous
    # file.
    P = P/P.sum(axis=1)[:, np.newaxis]

    # Looping for N steps
    for i in range(N):
        p = P.T.dot(p)

    # Computing the eigenvector.
    eigenvector = np.linalg.eig(P.T)

    print(eigenvector)
