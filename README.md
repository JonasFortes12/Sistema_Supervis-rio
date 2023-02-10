## Sistema Supervisório Para Sistemas de Controle


------------------

#### Resumo:
Um sistema supervisório é responsável por coletar e monitorar dados importantes de um determinado processo físico. Assim, este tipo de sistema é capaz de unificar todas as informações relevantes de forma clara e eficiente, possibilitando, em tempo real, a visualização de variáveis, a análise de tendências e a identificação de eventuais falhas em processos. Neste trabalho, foi desenvolvido um sistema supervisório para monitorar e simular diversos sistemas de controle, tais como um tanque de nível e um pêndulo invertido. Este sistema supervisório é composto por uma interface contendo gráficos que apresentam, em tempo real, os valores das variáveis de um determinado sistema de controle, além de possuir outras funcionalidades, tais como salvar dados coletados. Os valores das variáveis podem ser recebidos de diversas formas, como através de um documento de texto ou através de comunicação serial. A linguagem de programação utilizada para a implementação do sistema foi o Python, a qual disponibiliza várias bibliotecas de código aberto (open source). Dentre estas foram utilizadas duas: Tkinter e Matplotlib. A biblioteca Tkinter dispõe de um kit de ferramentas para a criação de interfaces gráficas, e foi utilizada para criar a interface do sistema de supervisão. Já a biblioteca Matplotlib oferece ferramentas para representar os dados por meio de gráficos, o que permite a visualização da variação, no tempo, dos dados. A integração entre essas duas bibliotecas ofereceu as ferramentas necessárias para a criação do sistema supervisório proposto. 

------------------

Atualmente, o sistema implementado está adaptado para a supervisão de um módulo didático de um tanque de nível (na branch master). 

##### Elementos do Sistema:

* Gráficos que apresentam, em tempo real, os valores das variáveis envolvidas, como o nível da água e o tempo de enchimento.

* Emissão de relatóro dos dados coletados.

##### Sistema - Tela de Visualização dos Dados:
<img src="/imgs/sistema.jpg" alt="sistem" width="400"/>
##### Módulo Didátido - Tanque de Nível:
<img src="/imgs/Tanque de nível.jpg" alt="drawing" width="200"/>




