# Data and Feature Definitions

Este documento fornece um hub central para as fontes de dados brutos, os dados processados/transformados e os conjuntos de recursos. Mais detalhes de cada conjunto de dados são fornecidos no relatório de resumo de dados.

Para cada dado, é fornecido um relatório individual que descreve o esquema de dados, o significado de cada campo de dados e outras informações úteis para a compreensão dos dados. Se o conjunto de dados for a saída de conjuntos de dados existentes de processamento/transformação/engenharia de recursos, os nomes dos conjuntos de dados de entrada e os links para scripts usados ​​para conduzir a operação também serão fornecidos. 

ara cada conjunto de dados, os links para os conjuntos de dados de amostra no diretório _**Data**_ também são fornecidos. 

_**For ease of modifying this report, placeholder links are included in this page, for example a link to dataset 1, but they are just placeholders pointing to a non-existent page. These should be modified to point to the actual location.**_


## Raw Data Sources


| Dataset Name | Original Location   | Destination Location  | Data Movement Tools / Scripts | Link to Report |
| ---:| ---: | ---: | ---: | -----: |
| Dataset 1 | Brief description of its orignal location | Brief description of its destination location | [script1.py](link/to/python/script/file/in/Code) | [NYC_Motor](Data\Raw)|



* Dataset1 summary. <Forneça um breve resumo dos dados, como como acessar os dados. Informações mais detalhadas devem estar no Relatório Dataset1.>

Os dados podem ser utilizado em qualquer plataforma que leia um arquivo CSV. Aqui utilizamos o Colab e utilizamos a linguagem python para a leitura do arquivo.

df_NYC_Motor = pd.read_csv('NYC_Motor.csv')
df_NYC_Motor


## Processed Data
| Processed Dataset Name | Input Dataset(s)   | Data Processing Tools/Scripts | Link to Report |
| ---:| ---: | ---: | ---: | 
| Processed Dataset 1 | [df_kill_fem](Data\Processed), [Dataset2](link/to/dataset2/report) | [Python_Script1.py](link/to/python/script/file/in/Code) | [Processed Dataset 1 Report](link/to/report1)|


* Processed Data1 summary. <Forneça um breve resumo dos dados processados, por exemplo, por que você deseja processar os dados dessa maneira. Informações mais detalhadas sobre os dados processados ​​devem estar no Relatório de Dados Processados1.>

Realizamos uma extração das colunas de interesse, para a maior precisão dos modelos.


## Feature Sets

| Feature Set Name | Input Dataset(s)   | Feature Engineering Tools/Scripts | Link to Report |
| ---:| ---: | ---: | ---: | 
| Feature Set 1 | [Dataset1](link/to/dataset1/report), [Processed Dataset2](link/to/dataset2/report) | [R_Script2.R](link/to/R/script/file/in/Code) | [Feature Set1 Report](link/to/report1)|
| Feature Set 2 | [Processed Dataset2](link/to/dataset2/report) |[SQL_Script2.sql](link/to/sql/script/file/in/Code) | [Feature Set2 Report](link/to/report2)|

* Feature Set1 summary. <Provide detailed description of the feature set, such as the meaning of each feature. More detailed information about the feature set should be in the Feature Set1 Report.>
* Feature Set2 summary. <Provide detailed description of the feature set, such as the meaning of each feature. More detailed information about the feature set should be in the Feature Set2 Report.> 
