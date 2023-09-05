# projeto-final-pmd-2023
Projeto final da matéria de Processamento Massivo de Dados - UFSCar Sorocaba

## Execução

Para executar os códigos, siga os seguintes passos:

Execute o comando

```
docker compose up
```

no diretório 'docker'

Quando os contêineres estiverem prontos, acesse um shell do container jupyter/pyspark-notebook e execute o comando

```
jupyter server list
```

Esse comando irá retornar o servidor jupyter em execução e seu token de acesso, assim poderá acessar os notebooks pela interface web do jupyter em localhost:8888, ou conectar o kernel diretamente no vscode (recomendado). 
O diretório work está ligado ao sistema de armazenamento do container jupyter.