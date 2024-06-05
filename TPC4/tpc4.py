import ply.lex as lex

# Lista de tokens
tokens = (
    'SELECT',
    'FROM',
    'WHERE',
    'ATRIBUTO',
    'NUMBER',
    'COMMA',
    'GREATER_EQUAL',
)

# Definição das expressões regulares para cada token
t_SELECT = r'SELECT'
t_FROM = r'FROM'
t_WHERE = r'WHERE'
t_ATRIBUTO = r'\w+'
t_NUMBER = r'\d+'
t_COMMA = r','
t_GREATER_EQUAL = r'>='

# Ignorar espaços em branco
t_ignore = ' \t\n'

# Tratamento de erro para caracteres desconhecidos
def t_error(t):
    print(f"Caracter ilegal {t.value[0]}")
    t.lexer.skip(1)

# Criando o analisador léxico
lexer = lex.lex()

# Teste
query = "SELECT id, nome, salario FROM empregados WHERE salario >= 820"
lexer.input(query)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
