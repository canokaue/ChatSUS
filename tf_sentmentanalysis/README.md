#Analise de Sentimento

Uso: 

- git clone https://github.com/canokaue/ChatSUS.git
- cd sentanal
- pip install -r requirements

Faça o download dos seguintes arquivos e coloque-os na raíz do diretório
-modelo: https://drive.google.com/file/d/1xsXQwqJ2M7Obx0h1MtJk3PE4bTy0WGcq/view?usp=sharing
-bigramas: https://drive.google.com/file/d/13-4XJ7JPZ4mOal_PZ26G4ntXI5luZUkD/view?usp=sharing
-unigramas: https://drive.google.com/file/d/1rnbUPNk2ThSJhMcU1iYTxVqQIVngBnn3/view?usp=sharing

python eval_nn_model.py FRASE

ex: python eval_nn_model.py "Esse é um comentário ruim"

#Usar como módulo

- from eval_nn_model import *
- sentiment = sentiment_analysis(string)

- sentiment <- 1 se positivo
- sentiment <- 0 se negativo