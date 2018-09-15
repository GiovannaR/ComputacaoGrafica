# ComputacaoGrafica

## Configurações

Para que o algoritmo funcione no seu computador é necessário a instalação do Python3 e do Tkinter (biblioteca do Python3).

Códigos para instalação em sistema Linux:

<code>
  apt-get install python3
  
  apt-get install python3-tk
</code>

Links que auxiliam ao baixar o Python3 e o Tkinter no Windows:

Python3: https://cadernoscicomp.com.br/instalar-python-3-no-windows/
Tkinter: https://tkdocs.com/tutorial/install.html

Para executar o código é necessário digitar a linha de comando:
<code>
  python3 cg.py 
</code>

## Estrutura

  O código no arquivo <b><i>cg.py</i></b> é composto de duas classes chamadas <i>Aplication1</i> e <i>Aplication2<i/>, que contêm os componentes de suas respectivas telas (botões, caixa de texto, Canvas, divisão de componentes), e algoritmos relacionados à computação gráfica. Na primeira, estão presente os seguintes métodos, sendo cada um referente ao algoritmo de seu nome:
    <ul>
      <li> Algoritmo_DDA
      <li> Algoritmo_Bresenham
      <li> Algoritmo_Bresenham_Circulo
    </ul>
  
  Na classe <i>Aplication1</i>, além desses métodos, também possui um método cuja finalidade é apagar todas as informações presentes no Canvas(espaço destinado ao desenho) chamado “Apagar”.
  
  Na segunda, está presente os seguintes métodos, também referentes aos algoritmos de seus respectivos nomes:
  <ul>
    <li> Reflexao_x
    <li> Reflexao_y	
    <li> Reflexao_origem
    <li> Cisalhamento_x
    <li> Cisalhamento_y
    <li> Translacao
    <li> Rotacao
    <li> Escala
  </ul>
  
  Além desses, a classe Aplication2 também possui um método para apagar todas as informações presentes no Canvas(espaço destinado ao desenho) chamado “Apagar”, e a sua própria versão do Algoritmo_DDA para auxiliar na construção das retas necessárias em outros algoritmos. 
  
  Observação: Nos comentários abaixo das duas classes existe uma terceira classe (<i>Aplication3</i>) que representa uma tentativa de implementação do algoritmo de recorte de janela: Cohen-Sutherland.
  
## Maneira de usar
  Quando o programma se inicializa, duas janelas  se abrem com diversas caixas de textos, botões, e um espaço em branco. As informações do ponto final e inicial das retas, do ângulo, força, raio e translação que são necessárias ao funcionamento do algoritmo são preenchidas pelo usuário por meio dessas entradas de texto. Existe em cada página, o botão dos algoritmos de sua respectiva classe (<i>Aplication1</i> ou <i>Aplication2</i>). Após a execução de cada algoritmo, o resultado é desenhado no espaço em branco. 
  
  Para mais informações consultar o arquivo <i>Manual_do_usuario_cg.pdf</i>.
  
  Para ver o algoritmo funcionando, executar o vídeo . 
  
  
  

  
