#Problema do mosaico

Este problema consiste em preencher uma imagem original com imagens menores dado um determinado critério.
No desenvolvimento deste trabalho adotou-se como critério a média das cores em uma determinada região, de forma que está região é preenchida com a imagem que em uma média mais parecida.
Como as imagens possuem três bandas, as quais ao serem combinadas fornecem a cor de saída, utilizou-se então a distância euclidiana entre a média das regiões e a média da imagem a ser preenchida.

As imagens que são utilizadas para serem preenchidas no mosaico se encontram na pasta  "banco". Como há um custo para fazer o cálculo destas imagens - o qual cresce com o aumento de número de imagens, criou-se uma função para fazer estes cálculos a qual também armazena em um arquivo os resultados encontrados. Desta forma, pode-se fazer apenas uma vez este cálculo e depois somente ler o resultados. Entretanto, quando altera-se as imagens, como por exemplo ao adicionar novas, deve-se então refazer este cálculo.

O aumento da qualidade do mosaico depende da quantidade de imagens que são inseridas para preenche-lo. Essa quantidade é inserida através de uma variável nomeada fatorDiv. Ao inserir o valor 10 por exemplo, é criado uma imagem com 100 imagens menores, ou seja, 10x10.

A seguir estão algumas das imagens de entrada e os resultados que foram obtidos.

### Exemplo de execução:

**Lenna**

Input:

![](https://raw.githubusercontent.com/rodrigogiraldi/mosaico/master/inputs/lenna.png)

Outputs:

10x10

![](https://raw.githubusercontent.com/rodrigogiraldi/mosaico/master/outputs/lenna10.png)

20x20

![](https://raw.githubusercontent.com/rodrigogiraldi/mosaico/master/outputs/lenna20.png)

40x40

![](https://raw.githubusercontent.com/rodrigogiraldi/mosaico/master/outputs/lenna40.png)

80x80

![](https://raw.githubusercontent.com/rodrigogiraldi/mosaico/master/outputs/lenna80.png)

160x160

![](https://raw.githubusercontent.com/rodrigogiraldi/mosaico/master/outputs/lenna160.png)


**Cameraman**

Input:

![](https://raw.githubusercontent.com/rodrigogiraldi/mosaico/master/inputs/camera.bmp)

Outputs:

10x10

![](https://raw.githubusercontent.com/rodrigogiraldi/mosaico/master/outputs/camera10.bmp)

20x20

![](https://raw.githubusercontent.com/rodrigogiraldi/mosaico/master/outputs/camera20.bmp)

40x40

![](https://raw.githubusercontent.com/rodrigogiraldi/mosaico/master/outputs/camera40.bmp)

80x80

![](https://raw.githubusercontent.com/rodrigogiraldi/mosaico/master/outputs/camera80.bmp)
