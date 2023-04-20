# Netflix_Challenge
## Programming Logic and Linear Algebra Project, utilizing eigenvalue and eigenvector concepts

Developers:

* João Lucas de Moraes Barros Cadorniga [JoaoLucasMBC](https://github.com/JoaoLucasMBC)  
* Eduardo Mendes Vaz [EduardoMVaz](https://github.com/EduardoMVAz)

---

## Como Instalar

Para utilizar o projeto <em>"Netflix Challenge"</em>, você deve ter o Python instalado em seu computador e seguir os passos:

1. Clone o repositório na sua máquina na pasta de sua escolha. Utilize o comando:

`git clone https://github.com/EduardoMVAz/Netflix_Challenge.git`

2. Utilizando o terminal / a IDE de sua escolha, crie uma *Virtual Env* de Python e a ative:

`python -m venv env`

`env/Scripts/Activate.ps1` (Windows)

3. Mude para a pasta do <em>"Netflix Challenge"</em> e instale as bibliotecas requeridas:

`cd ./Netflix_Challenge`

`pip install -r requirements.txt`

4. Após a instalação, visualize as informações e demonstrações no arquivo *demo.ipynb* para ver o programa funcionando e os testes realizados por nós.

--- 

## Como Utilizar

---

## Modelo Matemático

O modelo matemático do projeto "Netflix Challenge" é baseado no conceito de autovetores, autovalores e SVD (Singular value decomposition), e o objetivo é utilizar esses conceitos para tentar prever qual será a avaliação de um filme por um usuário em uma plataforma de _streaming_, baseando-se em informações e avaliações de outros usuários, e utilizar essa informação para recomendar filmes que o usuário provavelmente ira gostar.

Resumidamente, a ideia é comparar os gostos de um usuário com outros usuários, de forma a encontrar a influência que seus outros gostos podem ter sobre suas preferências. Esse procedimento será melhor explicado vendo os significados dos conceitos utilizados.

### 1. Autovetores e Autovalores


### 2. SVD


### 3. Aplicando os Conceitos e realizando a predição

---

## Testes

Realizamos diversos testes para testar a eficácia do programa, nos perguntando qual a quantidade de autovalores que que realmente afetavam a nota dada pelo usuário e como a inserção de ruído afetava a predição.

Todos os testes e seus códigos podem ser encontrados no arquivo *demo.ipynb*, assim como as imagens geradas a partir dos dados coletados, porém aqui oferecemos uma interpretação desses resultados, assim como uma explicação do porquê o teste foi realizado.

### Descobrindo o número de autovalores

Para determinar o número de autovalores que realmente impactam a predição, nós inicialmente criamos uma visualização desses valores: 

![autovalores plotados](s.png)

Visualizando essa imagem, é possível perceber que há uma rápida desvalorização dos autovalores, aproximadamente na marca de 30, formando um "cotovelo". Essa curva representa o ponto onde os autovalores passam a ter uma importância muito pequena na predição. A partir dessa ideia, selecionamos inicialmente então para a predição somente os 30 maiores autovalores.

Porém, ao realizarmos outro teste, dessa vez, realizando 1000 inserções de ruído, ou substituições, e variando a quantidade de autovalores, obtivemos resultados interessantes:

| Número de Autovalores | Erro médio absoluto do Preditor |
| --- | --- |
|10.0 |	0.873004 |
|20.0 |	0.954347 |
|30.0	| 1.067995 |
|40.0	| 1.082486 |
|50.0	| 1.152909 |

Realizamos testes até 100 autovalores, porém o erro só aumentou. O resultado realmente interessante desse teste foi de que, contrário à conclusão que tomamos a partir do gráfico e do "cotovelo", quando nós utilizamos somente os 10 maiores autovalores para realizar a predição, o erro médio absoluto entre a predição e o valor real da avaliação do filme pelo usuário foi o **menor** de todos. A conclusão é de que os poucos são os autovalores realmente relevantes para a predição, em comparação com os quase 700 autovalores totais.

### Testes com substituições

#### Primeiro Teste - 1000 substituições

O primeiro teste com substituições realizado foi realizar uma iteração do preditor, com inserção de 1000 valores ruído para serem previstos, utilizando 10 autovalores.
Os resultados podem ser visualizados na seguinte imagem:


![1000subs](1000subs.png)

Com esse teste, obtivemos o erro médio absoluto de 0.8441194811185945, e o desvio padrão dos erros de 1.1072750777819045

#### Segundo Teste - 100 substituições realizadas 10 vezes

O segundo teste foi realizar 10 iterações do preditor, com inserção de 100 valores ruído, novamente utilizando 10 autovalores.
Os resultados podem ser visualizados na seguinte imagem:


![100subs10times](100subs10times.png)
