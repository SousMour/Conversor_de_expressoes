#conversor de expressões
#Etapa 1 : Tradução de palavras.

textSpeakDictionary = {
    "rs"   : "risos" ,
    "tmb"   : "também"
}

#imprima o dicionário inteiro
print( "Dicionário =" , textSpeakDictionary )

#imprime apenas o conteúdo relacionado à chave "rs"
print( "\nrs =" , textSpeakDictionary["rs"] )

#texto que pede a entrada do usuário
key = input("O que você gostaria de converter? : ")
print( key , "=" , textSpeakDictionary[key] )
