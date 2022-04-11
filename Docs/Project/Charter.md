# Project Charter

## Business background

* Quem é o usuário, em qual ação ele pretende fazer..
* Que problemas estamos tentando resolver?


## Scope
* Quais soluções de ciência de dados estamos tentando construir?
Uma prevenção de acidente fatais e um deteminado parametro.
* O que faremos?
Criaremos um modelo de previsão de acidentes, voltado para o público feminino, que possua habilitação e vontade de dirigir em um determinado horário...
* Como será consumido pelo cliente?
O cliente colocará a sua idade e sexo, e o modelo informará os risco de acidentes naquele horário. Sebaseando nos dados históricos do mesmo período e hora.

## Personnel
* Quem está neste projeto:
	* Python:
		* Líder de projeto - Carlos Ferreira
		* PM - Carlos Ferreira
		* Cientista(s) de dados - Carlos Ferreira
		* Gerente de contas - Carlos Ferreira
	* Cliente:
		* Administrador de dados - Carlos Ferreira
		* Contato de negócios - Carlos Ferreira
	
## Metrics
* Quais são os objetivos qualitativos? (por exemplo, reduzir a rotatividade de usuários)
Reduzir a inresponsabilidade dos motoristas ao volante. 
* O que é uma métrica quantificável (por exemplo, reduzir a fração de usuários com inatividade de 4 semanas)
Reduzir o número de acidentes ou dobrar as responsabilidades dos motoristas.
* Quantificar quais melhorias nos valores das métricas são úteis para o cenário do cliente (por exemplo, reduzir a fração de usuários com inatividade de 4 semanas em 20%)
 Reduzir o número de acidentes em até 40%
* Qual é o valor da linha de base (atual) da métrica? (por exemplo, fração atual de usuários com inatividade de 4 semanas = 60%)
Atualmente o número de acidentes em até 80%
* Como vamos medir a métrica? (por exemplo, teste A/B em um subconjunto especificado por um período especificado; ou comparação de desempenho após a implementação com a linha de base)
Criaremos um modelo preeditivo e utilizaremos a idade do cliente para lhe informar os riscos.

## Plan
* Fases (marcos), cronograma, breve descrição do que faremos em cada fase.
Buscar um dataframe sobre o assunto;
Fazer uma análise exploratória;
Verificar os dados;
Verificar a estacionaridade dos dados;
Realizar a decomposição;
Verificar os modelos;
Ver os resultados Arima e Prophet;
Realizar uma cominicação com a AWS;
Guardar os dados na AWS;
Criar regras de mensageria com AWS;

## Architecture
* Dados
  * Que dados esperamos? Dados brutos nas fontes de dados do cliente (por exemplo, arquivos locais, SQL, Hadoop local etc.)
  Arquivo no formato CSV, retirados do Kegle
* Movimentação de dados do local para a AWS (Azcopy, EventHub etc.)
  Utilizamos o Visual Code
 

* Quais ferramentas e recursos de armazenamento/análise de dados serão usados ​​na solução, por exemplo,
  * HDI/Hive/R/Python para construção, agregação e amostragem de recursos

  * Como o cliente usará os resultados do modelo para tomar decisões
  Ele receberá via email, uma resposta do modelo.
  

## Communication
* Como manteremos contato? Reuniões semanais?
O contado será estabelecido através de e-mail, ou contato telefônico.
* Quem são as pessoas de contato em ambos os lados?
Carlos Ferreira
Alice Pantoja Ferreira