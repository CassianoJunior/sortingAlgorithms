# Análise dos diferentes algoritmos de ordenação

> Este trabalho foi desenvolvido na linguagem Python com o objetivo de comparar alguns algoritmos mais conhecidos e analizá-los.
> Sendo eles: Bubble Sort, Insertion Sort, Heap Sort, Merge Sort e Quick Sort. 
> Para cada algoritmo é analizado diferentes tamanhos (100 à 200000) e tipos (vetor ordenado crescente, vetor ordenado decrescente e vetor aleatório) de entradas, 
> marcando o tempo médio e o número de comparações realizadas.
> Atividade prática feita para a disciplina de Projeto e Análise de Algoritmos do curso de Ciência da Computação da UFPI.

## Requisitos

- Python
- Biblioteca Matplotlib, utilizada para gerar os gráficos. 
  - Para instalar utilizando o pip(gerenciador de pacotes do Python), basta digitar o comando:
 
    ```
    pip install matplotlib
    ```
## Dados gerados
- Para o cálculo do tempo, foi-se utilizada a biblioteca timeit.
  - Para melhor observação e análise, todos os algoritmos executam 3 vezes e, ao final, é gerado um arquivo de texto na pasta "data" com as respectivas médias de tempo
    para cada tipo de entrada, além do número de comparações feitas.

## Dados de entrada
- Para gerar as entradas, o arquivo "numbers.txt" é usado, nele tem-se os números 0 à 199999 (dispostos um em cada linha), usado para gerar os vetores.
- Inicialmente a aplicação lê esse arquivo e organiza os números em dois vetores, um em ordem crescente e outro em ordem decrescente.
- Para gerar vetor aleatório é necessário definir o tamanho da entrada, para então realizar o embaralhamento dos números.

## Execução
Para executar e testar a aplicação basta seguir os passos:
1. Baixe o código e descompacte na pasta que desejar.
2. Na pasta do projeto, execute o arquivo "app.py" no terminal com o sequinte comando:

  ```
  python app.py
  ```
3. Você pode escolher o tamanho da amostra através da opção 6, e em seguida selecionar um dos algoritmos para executar. Ao final das 3 execuções, será criado
   um arquivo no diretório "data", onde será possível ver a média do tempo de execução para os diferentes tipos de entrada e o número de comparações feitas.
4. Pode-se também fazer o teste automático, através da opção 7, com todos os algoritmos com amostras pré-selecionadas, sendo elas:
  - 100
  - 1000
  - 5000
  - 30000
  - 50000
  - 100000
  - 150000
  - 200000
  
  e ao final, é gerado um arquivo no diretório "data" com as informações de cada algoritmo com o respectivo tamanho de amostra. Também são gerados gráficos para 
  melhor comparação do tempo e do número de comparações para cada tamanho de amostra, na qual são salvos no formato png no diretório "graphs".
  
  # Créditos
  Criado pelos alunos:
  - Abner Brito
  - José Augusto
  - José Cassiano
