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

Após instalar as dependências, no arquivo `demo.ipynb`, basta rodar célula por célula, em ordem, e acompanhar a geração das predições sobre os dados em diversos cenários. Alguns comentários e explicações estão presentes pelo *notebook*, mas todos os detalhamentos se encontram nesse arquivo `README.md`.

*Atenção: alguns testes, como o `Teste (4)`, requerem grande tempo de processamento e alta capacidade computacional. Portanto, é indicado não rodar suas células novamente e apenas executar a criação do gráfico, que utiliza do arquivo `csv` gerado com antecedência em um notebook no *Google Cloud*.

---

## Modelo Matemático

O modelo matemático do projeto "Netflix Challenge" é baseado no conceito de autovetores, autovalores e SVD (Singular value decomposition), e o objetivo é utilizar esses conceitos para tentar prever qual será a avaliação de um filme por um usuário em uma plataforma de _streaming_, baseando-se em informações e avaliações de outros usuários, e utilizar essa informação para recomendar filmes que o usuário provavelmente ira gostar.

Resumidamente, a ideia é comparar os gostos de um usuário com outros usuários, de forma a encontrar a influência que seus outros gostos podem ter sobre suas preferências. Esse procedimento será melhor explicado vendo os significados dos conceitos utilizados.

### 1. Autovetores e Autovalores

Autovetores e Autovalores são componentes de uma matriz que podem ser descritos da seguinte forma:
Considerando uma transformação linear, temos que um vetor `x` é um autovetor de uma matriz `A` quando ao multiplicar esse vetor pela própria matriz o resultado é um múltiplo do próprio vetor,

$Ax = x\lambda$

Por multiplicações e inversões matriciais, conseguimos também obter a matriz somente usando seus autovetores e autovalores

$Ax = x\lambda$

* isolamos o x usando matriz inversa

$Axx^{-1} = x\lambda x^{-1}$

$A = x\lambda x^{-1}$

### 2. SVD


### 3. Aplicando os Conceitos e realizando a predição

---

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

## **Seria possível utilizar esse sistema em produção?**

