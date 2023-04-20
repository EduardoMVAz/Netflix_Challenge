from scipy.linalg import svd, diagsvd
import numpy as np


class MoviePredictor():

    def __init__(self, data, n_of_eigval=30):
        '''
        O número de autovalores utilizado pode ser alterado, como um hiperparâmetro a ser otimizado.
        '''
        self.data = data
        self.n_of_eigval = n_of_eigval


    def predict(self, indexes:list) -> float:
        '''
        Recebe uma lista de tuplas, onde cada tupla representa uma linha e uma coluna da matriz de dados onde vamos realizar
        a predição.

        Retorna uma lista com as predições para cada tupla correspondente.
        '''

        # Aplica a SVD na matriz de dados
        u, s, vt = svd(self.data)

        # Seleciona os n_of_eigval autovalores maiores
        s[-(671-self.n_of_eigval):] *= 0.0

        # Constroi a matriz diagonal com os autovalores
        sigma = diagsvd(s, self.data.shape[0], self.data.shape[1])

        # Reconstroi a matriz de dados
        B = u @ sigma @ vt
        
        # Retorna a predição para cada tupla
        return np.array([B[i][j] for i,j in indexes])



def main():
    '''
    Faz um teste básico realizadno uma predição aleatória na matriz de dados.
    '''
    import pandas as pd
    import numpy as np

    df = pd.read_csv('ratings_small.csv')
    
    # Aqui é testado um fill_value de 0
    data = pd.pivot_table(df, values='rating', index='userId', columns='movieId', fill_value=0)

    data = data.to_numpy()

    # Seleciona uma linha e uma coluna aleatória da matriz de dados
    i = np.random.randint(0, data.shape[0])
    j = np.random.randint(0, data.shape[1])

    real_score = data[i][j]

    while real_score == 0:
        i = np.random.randint(0, data.shape[0])
        j = np.random.randint(0, data.shape[1])

        real_score = data[i][j]

    # Insere um valor aleatório na posição selecionada
    data[i][j] = np.random.randint(0, 5)

    mp = MoviePredictor(data, 10)

    print(real_score)
    print(i, j)

    predicted_score = mp.predict([(i, j)])

    print(f'Real score: {real_score}')
    print(f'Predicted score: {predicted_score}')



if __name__ == '__main__':
    main()