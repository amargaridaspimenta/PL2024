# Criar em *Python* um somador *On/Off*
Tal como indica no enunciado disponibilizado na *Blackboard*, este programa, indicado para o TPC3 realiza todas estas funções:

1. O programa soma todas as sequências de dígitos que encontra num texto;
2. Sempre que encontra a string *“Off”* em qualquer combinação de maiúsculas e minúsculas, esse comportamento é desligado;
3. Sempre que encontra a string *“On”* em qualquer combinação de maiúsculas e minúsculas, esse comportamento é novamente ligado;
4. Sempre que encontra o caráter “=”, o resultado da soma é colocado na saída. 

# Como funciona?
No ficheiro `texto.md` introduzi variadas expressões, onde é possível verificar o comportamento do programa não só perante as expressões *On* e *Off* mas também quando estas se encontram dentro de palavras como *"monad"* onde encontramos na sua sequência a palavra *On*, por exemplo.

Dado isto, o programa lê o ficheiro, e através da introdução das lógicas pedidas no pontos acima, realiza com sucesso as operações.

Após isso, quando compilado, para além de exibir o *output* no terminal, este é escrito num novo ficheiro, o `output.txt`, onde é possível verificar as soluções das somas realizadas.

# Como usar?
Para compilar o programa:
*python3 tpc3_pl.py* 

Ter em conta que é necessário ter na mesma diretoria que o `tpc3_pl.py` também o ficheiro `texto.md`.
