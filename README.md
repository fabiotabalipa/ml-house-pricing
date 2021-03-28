# Predição de Preço de Imóveis

Repositório do Trabalho de Conclusão de Curso apresentado ao Curso de Especialização em Ciência de Dados e Big Data da PUC Minas.

## Fluxo de Trabalho

![Captura de Tela 2021-02-05 às 18 22 36](https://user-images.githubusercontent.com/37602229/107090606-3507be80-67df-11eb-9694-04b921b5e8b5.png)

> O código-fonte e resultados do fluxo de trabalho estão no notebook workflow.ipynb.

## Deploy do Modelo

![Captura de Tela 2021-02-05 às 14 05 52](https://user-images.githubusercontent.com/37602229/107090772-78622d00-67df-11eb-8460-8e3a80df60f0.png)

### Instruções para execução:

1. Instalar os módulos Python do requirements.txt

```
pip install -r requirements.txt
```

2. Executar o Flask

```
flask run
```

3. Acessar a seguinte URL com o navegador web: http://127.0.0.1:5000/ 

---

> Sugestões da banca: 1) Utilizar GridSearchCV para ajuste de hiperparâmetros; 2) Testar séries temporais.

---

**Autor**: Fábio de Oliveira Tabalipa