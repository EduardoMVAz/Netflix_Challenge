from scipy.linalg import svd, diagsvd
import numpy as np


class MoviePredicter():

    def __init__(self, data, n_of_eigval=30):
        self.data = data
        self.n_of_eigval = n_of_eigval


    def predict(self, indexes:list) -> float:
        u, s, vt = svd(self.data)

        s[-(671-self.n_of_eigval):] *= 0.0

        sigma = diagsvd(s, self.data.shape[0], self.data.shape[1])

        B = u @ sigma @ vt
        
        return np.array([B[i][j] for i,j in indexes])



def main():
    import pandas as pd
    import numpy as np

    df = pd.read_csv('ratings_small.csv')
    
    data = pd.pivot_table(df, values='rating', index='userId', columns='movieId', fill_value=0)

    data = data.to_numpy()

    # Selects a random row and a random column from the data matrix
    i = np.random.randint(0, data.shape[0])
    j = np.random.randint(0, data.shape[1])

    real_score = data[i][j]

    while real_score == 0:
        i = np.random.randint(0, data.shape[0])
        j = np.random.randint(0, data.shape[1])

        real_score = data[i][j]

    # Inserts noise into the data matrix
    data[i][j] = np.random.randint(0, 5)

    mp = MoviePredicter(data)

    print(real_score)
    print(i, j)

    predicted_score = mp.predict([(i, j)])

    print(f'Real score: {real_score}')
    print(f'Predicted score: {predicted_score}')




if __name__ == '__main__':
    main()