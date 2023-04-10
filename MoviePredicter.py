from scipy.linalg import svd, diagsvd


class MoviePredicter():

    def __init__(self, data):
        self.data = data


    def predict(self, i:int, j:int) -> float:
        u, s, vt = svd(self.data)

        s[-641:] *= 0.0

        sigma = diagsvd(s, self.data.shape[0], self.data.shape[1])

        B = u @ sigma @ vt
        
        return B[i][j]



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

    mp = MoviePredicter(data)

    print(real_score)
    print(i, j)
    # Inserts noise into the data matrix
    data[i][j] = np.random.randint(0, 5)

    predicted_score = mp.predict(i, j)

    print(f'Real score: {real_score}')
    print(f'Predicted score: {predicted_score}')



if __name__ == '__main__':
    main()