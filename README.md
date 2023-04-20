# Netflix_Challenge
## Programming Logic and Linear Algebra Project, utilizing eigenvalue and eigenvector concepts

Developers:

* João Lucas de Moraes Barros Cadorniga [JoaoLucasMBC](https://github.com/JoaoLucasMBC)  
* Eduardo Mendes Vaz [EduardoMVaz](https://github.com/EduardoMVAz)

---
<br/>

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

Após instalar as dependências, no arquivo `demo.ipynb`, basta rodar célula por célula, em ordem, e acompanhar a geração das predições sobre os dados em diversos cenários. Alguns comentários e explicações estão presentes pelo *notebook*, mas todos os detalhamentos se encontram nesse arquivo `README.md`.

**Atenção**: alguns testes, como o `Teste (4)`, requerem grande tempo de processamento e alta capacidade computacional. Portanto, é indicado não rodar suas células novamente e apenas executar a criação do gráfico, que utiliza do arquivo `csv` gerado com antecedência em um notebook no *Google Cloud*.

---
<br/>

## Modelo Matemático

O modelo matemático do projeto "Netflix Challenge" é baseado no conceito de autovetores, autovalores e SVD (Singular Value Vecomposition), e seu objetivo é utilizar esses conceitos para tentar prever qual será a avaliação de um filme por um usuário em uma plataforma de _streaming_, baseando-se em informações e avaliações de outros usuários, e utilizar essa informação para recomendar filmes que o usuário provavelmente gostará.

Resumidamente, a ideia é interpretar os autovetores dos dados como *perfis*, isto é, tendências entre as avaliações dos usuários. Dessa maneira, podemos "comparar gostos" de um usuário com o restante das bases de forma a encontrar a influência dos perfis na hora de realizar uma predição.Esse procedimento será melhor explicado vendo os significados dos conceitos utilizados.

### 1. Autovetores e Autovalores

**Autovetores e Autovalores** são componentes de uma matriz que podem ser descritos da seguinte forma:

Considerando uma transformação linear, temos que um vetor `x` é um autovetor de uma matriz `A` quando ao multiplicar esse vetor pela própria matriz o resultado é um múltiplo do próprio vetor,

$Ax = x\lambda$

Por multiplicações e inversões matriciais, conseguimos também obter a matriz somente usando seus autovetores e autovalores

$Ax = x\lambda$

* Isolamos o x usando matriz inversa

$Axx^{-1} = x\lambda x^{-1}$

$A = x\lambda x^{-1}$

Essa formulação é a base de diversos processos de decomposição, como o **PCA** e o **SVD**, que se baseiam em separar matrizes de dados em matrizes de autovetores e autovalores, permitindo realizar manipulações e então reconstituir e aproximar as matrizes originais.

### 2. SVD

SVD é uma técnica de decomposição de matrizes em função de matrizes singulares, ou seja, dependentes de seus autovetores e autovalores. Esse tipo de decomposição é utilizado especialmente em sistemas de recomendação, já que é possível manipular os autovalores de modo a tentar "advinhar" qual é o gosto de um usuário, e também em compressões de imagens, pois possibilita a remoção de ruído e compressão com perdas.

Ela se baseia no seguinte modelo:

$$  
A = U \Sigma V^T  
$$ 

onde:

* As colunas de $U$ são os auto-vetores de $A^T A$ (matriz de covariância),
* As colunas de $V$ (e, portanto, as linhas de $V^T$) são auto-vetores de $A A^T$,
* $\Sigma$ é uma matriz onde $s_{i,i}$ é a raiz quadrada dos auto-valores de $A^T A$ ou de $A A^T$.

Para entender o impacto dessa decomposição, precisamos entender os autovetores em si. Podemos analisá-los como **combinações lineares das features** de dados, de modo a criar *perfis*. Ou seja, são vetores que "apontam" na direção que maior impacta os dados, isto é, que mais representa **tendências** nos dados.

Aplicando essa ideia no contexto do Netflix Challenge, os autovetores da matriz de uma matriz de *usuários x filmes* representam como *perfis* de gêneros cinematográficos: eles vão apontar para as tendências das notas dos usuários, já que, quanto possuem notas semelhantes para filmes semelhantes, os users criam tendências na base. Portanto, podemos usá-los para prever comportamentos.

### 3. Decomposição de imagens e remoção de ruído

O exemplo mais claro da utilidade dessa decomposição é na remoção de ruído de imagens. Aqui, as colunas e linhas representam as posições dos pixels, e os valores das matrizes como a cor RGB dos mesmos.

No entanto, em uma imagem de baixa qualidade, ou com muito ruído, diversos pixels pela imagem "fogem ao padrão", isto é, não se encaixam a construção normal da imagem. Podemos relacionar isso com seus autovetores, já que pixels "fora da média" tenderão a se relacionar com os menores autovalores, pois não se conectam com as maiores tendências da imagem final. Dessa maneira, na decomposição SVD, ao zerar autovalores na matriz $\Sigma$, podemos ignorar autovetores de menor impacto no momento de recomposição e fazer predições dos valores que deveriam estar ali baseado nos autovetores dominantes que sobraram.

Claro, essa técnica também acaba afetando pixels normais. No entanto, sabendo escolher o número certo de autovalores para a situação, é possível minimzar as perdas.

### 4. Aplicando os Conceitos no *Netflix Challenge* e realizando predições

Trazendo a mesma estratégia para o desafio, zerar baixos autovalores significa ignorar os "perfis (como uma combinação de usuários e filmes) menos relevantes", já que a probabilidade que a nota real do nosso usuário seja influenciada por eles é baixa. Assim, deixando apenas os autovetores com maiores autovalores, permitimos que a reconstrução da matriz de avaliações siga apenas os padrões mais "fortes" dos usuários.

Portanto, o que realizamos é uma maneira de mapear usuários para perfis, e então perfis para filmes, manipulando matrizes de dimensão menor, ou seja, com menor sensibildiade em relação a ruído.

Para testar o método, é necessário inserir ruído direramente na base de dados `ratings_small.csv`, que possui uma vasta combinação de usuários, filmes e as suas respectivas notas. Portanto, em uma matriz de notas como:

$$
A = \begin{bmatrix}
3 & 4 & 3 & 4 \  
5 & 2 & 2 & 3 \  
2 & 1 & 5 & 3 \  
5 & 3 & 4 & 1  
\end{bmatrix}
$$

Podemos transformar um de seus valores em uma nota aleatória (onde $R$ é um número randomizado entre 0 e 5):

$$
A = \begin{bmatrix}
3 & 4 & R & 4 \  
5 & 2 & 2 & 3 \  
2 & 1 & 5 & 3 \  
5 & 3 & 4 & 1 
\end{bmatrix}
$$

Agora, realizando a decomposição, a eliminação dos X menores autovalores e a reconstituição da matriz, obtemos:

$$
A = \begin{bmatrix}
2.649 & 2.582 & 2.779 & 2.929 \  
4.928 & 1.711 & 2.565 & 2.782 \  
2.272, & 2.103 & 2.836 & 3.833 \  
5.128 & 3.520 & 3.520 & 1.393  
\end{bmatrix}
$$

Ao escalar esse processo para matrizes com grandes bases de dados de avaliações, esse efeito de predição (no caso, foi previsto $2.779$ para a nota real $3$) se potencializa e nos permite realizar previsões de notas ainda mais precisas.

---
<br/>

## Testes

Realizamos diversos testes para comprovar a eficácia da predição do método, nos questionando, primeiramente, sobre a quantidade de autovalores que que realmente afetavam a nota dada pelo usuário, e, então, sobre como a inserção de ruído afetava a predição no sistema.

Todos os testes e seus códigos podem ser encontrados no arquivo `demo.ipynb`, assim como as imagens geradas a partir dos dados coletados. Porém, aqui oferecemos uma interpretação obtidos detalhada dos resultados, assim como uma explicação de o porquê cada teste foi realizado.

### 1. Descobrindo o número de autovalores

O primeiro passo para podermos realizar predições precisas é saber quantos autovalores devemos considerar, já que, ao realizar a decomposição SVD, foram encontrados $671$. A estratégia inicial utilizada para determinar o número de autovalores que realmente impactam a recomposição da matriz de valores foi criamos uma visualização desses valores e identificar o "cotovelo", ou seja, a maior curva entre os valores, o que seria um bom indicador de quando eles começam a impactar menos. 

![autovalores plotados](s.png)

No gráfico, é possível perceber que há uma rápida desvalorização dos autovalores, aproximadamente na marca de 30, formando esse "cotovelo". A partir dessa ideia, selecionamos inicialmente, então, para a predição somente os *30* maiores autovalores — os outros seriam zerados no processo.

Com uma primeira estimativa em mãos, realizamos um segundo teste mais preciso: a partir do valor inicial próximo de 30 valores, realizamos diversos testes de predição com 1000 inserções de ruído, ou substituições, incrementando em 10 a quantidade de autovalores. A métrica de comparação foi o erro médio absoluto ao final de cada iteração. Obtivemos resultados interessantes:

| Número de Autovalores | Erro médio absoluto do Preditor |
| --- | --- |
|10.0 |	0.873004 |
|20.0 |	0.954347 |
|30.0	| 1.067995 |
|40.0	| 1.082486 |
|50.0	| 1.152909 |

Realizamos testes até 100 autovalores, no entanto, o erro aumentou constantemente. O resultado intrigante do teste foi que, contrário à conclusão que tomamos a partir do gráfico e do "cotovelo", quando nós utilizamos somente os 10 maiores autovalores para realizar a predição, o erro médio absoluto entre a predição e o valor real da avaliação do filme pelo usuário foi o **menor** de todos. A conclusão é de que são ainda menos os autovalores realmente relevantes para a predição, em comparação com os quase 700 autovalores totais.

### 2. Testes com substituições

O objetivo dos testes é gradualmente realizar cada vez menos predições por vez, mas aumentar o número de iterações para manter as mil previsões totais. Dessa maneira, podemos observar o desempenho do preditor em diversos cenários.

#### Teste (1) - 1000 substituições

O primeiro teste com substituições realizado foi realizar uma única iteração do preditor, com inserção de 1000 valores ruído para serem previstos, utilizando 10 autovalores. 

Os resultados podem ser visualizados na seguinte imagem:


![1000subs](1000subs.png)

Com esse teste, obtivemos o erro médio absoluto de 0.8441194811185945, e o desvio padrão dos erros de 1.1072750777819045

#### Teste (2) - 100 substituições realizadas 10 vezes

O segundo teste foi realizar 10 iterações do preditor, com inserção de 100 valores ruído, novamente utilizando 10 autovalores. Mesmo com menos inserções, os resultados foram muito semelhantes ao do teste anterior.

Os resultados podem ser visualizados na seguinte imagem:


![100subs10times](100subs10times.png)

Com esse teste, obtivemos o erro médio absoluto de 0.842224701088835, e o desvio padrão dos erros de 1.0998116832025817

#### Teste (3) - 10 substituições realizadas 100 vezes

O terceiro teste foi realizar 100 iterações do preditor, com inserção de 10 valores ruído, novamente utilizando 10 autovalores. Ainda obtivémos resultados semelhantes, mas é interessante ressaltar que, com menos substituições, observamos um pequeno aumento no erro médio absoluto.

Os resultados podem ser visualizados na seguinte imagem:


![10subs100times](10subs100times.png)

Com esse teste, obtivemos o erro médio absoluto de 0.9662062630537643, e o desvio padrão dos erros de 1.235156665491315

#### Teste (4) - 1 substituição realizada 1000 vezes

Para o último teste, realizamos 1 substituição somente, porém 1000 vezes, ainda utilizando 10 autovalores. Esse foi o teste mais demorado, sendo realizado em um notebook nos servidores *Google Cloud*. Mesmo assim, seu tempo de execução foi por volta de 2 horas.

Os resultados foram os seguintes:

![1sub1000times](1sub1000times.png)

Com esse teste, obtivemos o erro médio absoluto de 0.8570620029712793, e o desvio padrão dos erros de 1.1007180289497658

## 3. Teste de Estresse

Inicialmente, consideramos que esse teste seria feito visando qual seria a quantidade de ruído que impossibilitaria o preditor de funcionar corretamente. A marca que definimos como desfuncional seria o erro médio absoluto de $2.5$. No entanto, ao realizar o teste, descobrimos algo muito interessante: **o erro médio absoluto diminuiu progressivamente a medida que aumentávamos a quantidade de ruído inserida**, ainda se estabilizando aproximadamente em 1.1, próximo do valor do **desvio padrão**.

Recapitulando, os valores vazios dos nosso dados são preenchidos com a média das avaliações, aproximadamente 3.5, e os valores a serem previstos são substituídos por um ruído, um valor aleatório entre 0-5 — as possíveis notas para os filmes. O valor previsto pelo programa é então comparado com o valor substituído pelo ruído, a fim de encontrar o erro. É importante ressaltar que no programa **os valores vazios que foram substituídos pela média não são selecionados para substituição por ruído**.

Discutindo e considernando o método utilizado, formulamos uma possível hipótese de o porquê esse fenômeno estar acontecendo. Inicialmente, não haviamos percebido a relação da estabilização do erro absoluto médio com o desvio padrão, e chegamos na seguinte conclusão: em uma distribuição aleatória, quanto maior o número de "jogadas", mais a média dos dados tende a se estabilizar na média teórica. Ou seja, quanto mais ruído inserido, mais a média dos valores se aproximam de $2.5$. Somado a isso, pelo funcionamento do nosso programa, os valores que antes eram nulos na tabela (a maioria), foram substituídos pela média dos valores válidos. 

Portanto, ao realizar a reconstituição da matriz de *ratings*, a concentração de valores que tendem a média demonstram a sua influência e "atraem" as predições também para valores médios. Por fim, **na nossa hipótese, como então os usuários tendem a avaliar os filmes com o valor médio**, minimiza a probabilidade de que a predição esteja distante do valor real, já que, por exemplo, em um caso no qual a predição é $2.5$, o maior desvio possível é de $2.5$ também. Por causa disso, a presença de mais valores médios fazia com que inevitavelmente o preditor acertasse mais, por "apostar" no valor seguro.

Após essa hipótese já formulada, percebemos ainda a questão do desvio padrão: por que o erro médio se aproximava e estabilizava ao redor do desvio padrão, a medida que aumentávamos o ruído? Dado que desvio padrão representa a distância média dos dados em relação a média, e as nossas aproximações tendem a média por causa da inserção de ruído, então faz sentido que o erro se aproxime do desvio padrão. **O erro é justamente o quanto o valor previsto está longe do valor real, sendo o valor previsto próximo da média, o erro se aproxima do desvio padrão**.

---
<br/>

## **Seria possível utilizar esse sistema em produção?**

O algoritmo como foi desenvolvido talvez seja simples demais para atuar como um recomendador de filmes nas plataformas de streaming, principalmente partindo da hipótese formulada a partir do teste de estresse em relação a aproximação da média ao desconhecermos muitos valores da matriz. Dessa maneira, seria difícil para o algoritmo selecionar filmes para recomendar, mesmo que ele tivesse uma margem de erro pequena na previsão das avaliações (por volta de $0.8$ de erro absoluto médio), pois, em uma base de filmes tão massiva quanto a da *Netflix*, determinar o gosto de um usuário para tantos filmes criaria muito ruído na matriz.

Imaginando um cenário real, onde a quantidade de dados é gigantesca, seria também custoso computacionalmente avaliar os dados para tantos filmes, sendo necessárias algumas otimizações e estratégias para diminuir a gama de filmes usada na previsão. Uma medida possível seria utilizar as categorias dos filmes para reduzir o número de autovetores obtidos com a análise de dados, já que intuitivamente alguns dados fornecem pouquíssima informação relevante para prever a avaliação possível de um filme, por exemplo, prever a avaliação de um usuário de um filme como *O Exterminador do Futuro* utilizando dados de filmes de romance ou comédia.

Concluíndo, a resposta é **não**. Apesar de o sistema ser efetivo na base de dados proposta, cumprindo seu papel em testes simples e com poucos dados como os realizados por nós, com um erro absoluto médio baixo, para utilizá-lo em escala seriam necessárias algumas alterações, já que ele é simples demais para atuar como algoritmo de recomendação. Talvez, ele poderia ser incorporado em um sistema maior com mais features, que pudesse usar os dados obtidos de forma mais complexa, tornando-o capaz de escolher entre filmes para recomendar e de ignorar grupos de filmes ao realizar a predição. No entanto, sozinho, ele provavelmente não seria o sistema mais eficiente.
