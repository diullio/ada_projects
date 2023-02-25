# %% [markdown]
# ### Crie um banco de palavras; Crie uma função que le uma palavra aleatoria do banco e jogue forca com ela

# %%
import random as random

# %%
jogo = " JOGO DA FORCA "
print("{:-^50}".format(jogo))
print("\n")
print("Selecione o nível:")
nivel = int(input("Digite 1 para fácil ou 2 para difícil: "))
print("{:-^50}".format(""))

bd = []
if nivel == 1:
    with open("forca.csv", "r", encoding="utf-8") as arquivo:
        x = arquivo.readlines()

    for i in range(len(x)):
        bd.append(x[i].strip().lower())
else:
    with open("hard.csv", "r", encoding="utf-8") as arquivo:
        x = arquivo.readlines()

    for i in range(len(x)):
        bd.append(x[i].strip().lower())


# %%
# interface

palavra = random.choice(bd).strip().lower()
print(f"""
 ______
|      | 
|
|
|
  {"__ " * len(palavra)}
""")

mostrar = []
allchutes = []

for i in range(len(palavra)):
    mostrar.append("___")

tentativas = 0
substituidosmax = int(len(palavra))
substituidos = 0
erromax = 6


# %%


# %%
while tentativas < erromax and substituidosmax != substituidos:
    letra = input("Digite uma letra: ").strip().lower()
    
    if letra in palavra and letra not in allchutes:
        for i in range(len(palavra)):
            if palavra[i] in letra:
                mostrar[i] = letra
                substituidos += 1
            
        if tentativas == 0:
            print(f"""
             ______
            |      | 
            |
            |
            |
            
            {mostrar}
            """)
        elif tentativas == 1:
            print(f"""
             ______
            |      | 
            |     ( )
            |
            |
            
            {mostrar}
            """)

        elif tentativas == 2:
            print(f"""
             ______
            |      | 
            |     ( )
            |      |
            |
            
            {mostrar}
            """)
        elif tentativas == 3:
            print(f"""
             ______
            |      | 
            |     ( )
            |      |
            |     /
            
            {mostrar}
            """)
        elif tentativas == 4:
            print(f"""
             ______
            |      | 
            |     ( )
            |      |
            |     / \\
            
            {mostrar}
            """)
        elif tentativas == 5:
            print(f"""
             ______
            |      | 
            |     ( )
            |      |\\
            |     / \\
            
            {mostrar}
            """)

    else:
        tentativas +=1
        if tentativas == 1:
            print(f"""
             ______
            |      | 
            |     ( )
            |
            |
            
            {mostrar}
            """)

        elif tentativas == 2:
            print(f"""
             ______
            |      | 
            |     ( )
            |      |
            |
            
            {mostrar}
            """)
        elif tentativas == 3:
            print(f"""
             ______
            |      | 
            |     ( )
            |      |
            |     /
            
            {mostrar}
            """)
        elif tentativas == 4:
            print(f"""
             ______
            |      | 
            |     ( )
            |      |
            |     / \\
            
            {mostrar}
            """)
        elif tentativas == 5:
            print(f"""
             ______
            |      | 
            |     ( )
            |      |\\
            |     / \\
            
            {mostrar}
            """)
        elif tentativas == 6:
            print(f"""
             ______
            |      | 
            |     ( )
            |     /|\\
            |     / \\
         
            """)
    allchutes.append(letra)
    print("{:-^50}".format(""))
    print(f"Chutes: {allchutes}")
    print("{:-^50}".format(""))
    print("\n")

if substituidos == substituidosmax:
    print("{:#^50}".format(" VOCÊ GANHOU! PARABÉNS! "))
    print("""
        ___________    
       '._==_==_=_.'   
       .-\\:      /-.  
      | (|:.     |) |  
       '-|:.     |-'   
         \\::.    /    
          '::. .'      
            ) (        
          _.' '._      
         '-------'     
    """)
elif tentativas == erromax:
    print("{:#^50}".format(" VOCÊ PERDEU! TENTE NOVAMENTE! "))
    print(f"A palavra era: {palavra}")
    print("""
        _______________        
      /                 \      
    //                   \/\  
    \|   XXXX     XXXX   | /   
     |   XXXX     XXXX   |/    
     |   XXX       XXX   |     
     \__      XXX      __/     
       |\     XXX     /|       
       | |           | |       
       | I I I I I I I |       
       |_ I I I I I I _|       
         \_         _/         
           \_______/           
    """)

# %%



