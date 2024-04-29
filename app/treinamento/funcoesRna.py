import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt





def treinamento(X, y, descricaoX, descricaoY, nomeImagem, titulo="Titulo Gráfico", tipo='linha'):
    #buscando dados
    # Dividindo os dados em conjuntos de treinamento e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Treinando o modelo de regressão linear
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Fazendo previsões
    y_pred = model.predict(X_test)
    

    if tipo == 'linha':
        plt.scatter(X_test, y_test, color='orange')
        plt.plot(X_test, y_pred, color='green', linewidth=3)
  
    if tipo == 'barras':
        arrayX = []
        arrayY = []
        for dadosX in X_test:
            #convertendo os números em limite de 100
            arrayX.append(dadosX[0]%100)
        for dadosY in y_pred:
            #convertendo os números em limite de 100
            arrayY.append(dadosY[0]%100)
        cor = ['#2971CA','#D6B56A']
        plt.bar(arrayX,arrayY,color=cor)

    plt.xlabel(descricaoX)
    plt.ylabel(descricaoY)
    plt.title(titulo)
    plt.savefig(nomeImagem)
    plt.clf()
    return 0




def graficoComPrevisao(dadosA, dadosB, descricaoA, descricaoB,descricaoX, nomeImagem, titulo, descricaoVertical, descricaoHorizontal):

	##### Primeira série de dados
	# Converter para DataFrame do Pandas
	df = pd.DataFrame(dadosA, columns=[descricaoA])
	# Calcular a média móvel
	janela = 3  # Tamanho da janela da média móvel
	df['Media_Movel'] = df[descricaoA].rolling(window=janela).mean()

	# Prever os próximos 'n' valores usando a última média móvel
	n = 3  # Número de valores a prever
	ultima_media_movel = df['Media_Movel'].iloc[-1]
	previsao = [ultima_media_movel] * n

	# Adicionar as previsões ao DataFrame
	indices_previsao = [df.index[-1] + i + 1 for i in range(n)]
	df_previsao = pd.DataFrame(previsao, index=indices_previsao, columns=['Previsao'])
	df = pd.concat([df, df_previsao])



	#####################################################################################
	##### Segunda série de dados
	# Converter para DataFrame do Pandas
	dfB = pd.DataFrame(dadosB, columns=[descricaoB])
	# Calcular a média móvel
	janela = 3  # Tamanho da janela da média móvel
	dfB['Media_Movel'] = dfB[descricaoB].rolling(window=janela).mean()

	# Prever os próximos 'n' valores usando a última média móvel
	n = 3  # Número de valores a prever
	ultima_media_movel = dfB['Media_Movel'].iloc[-1]
	previsao = [ultima_media_movel] * n

	# Adicionar as previsões ao DataFrame
	indices_previsao = [dfB.index[-1] + i + 1 for i in range(n)]
	dfB_previsao = pd.DataFrame(previsao, index=indices_previsao, columns=['Previsao'])
	dfB = pd.concat([dfB, df_previsao])




	#####################################################################################
	# Plotar os dados originais e as previsões
	#Primeira série
	plt.plot(df[descricaoA], label=descricaoA)
	plt.plot(df['Media_Movel'], label='Média Móvel', linestyle='--')
	plt.plot(df['Previsao'], label='Previsão', linestyle=':')
	#segunda série
	plt.plot(dfB[descricaoB], label=descricaoB)
	plt.plot(dfB['Media_Movel'], label='Média Móvel', linestyle='--')
	plt.plot(dfB['Previsao'], label='Previsão', linestyle=':')

	plt.xlabel(descricaoHorizontal)
	plt.ylabel(descricaoVertical)
	
	plt.title(titulo)
	plt.legend()
	plt.savefig(nomeImagem)
	plt.clf()
     
