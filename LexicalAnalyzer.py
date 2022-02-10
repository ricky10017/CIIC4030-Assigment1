from ply import lex

tokens = ('IF', 'THEN', 'ELSE', 'MAP', 'TO', 'LET', 'IN',
          'NULL', 'TRUE', 'FALSE', 'LOWER', 'UPPER', 'QSIGN',
          'UNDER', 'NUMBER', 'ALPHA', 'ALPHAOTHER',
          'ALPHAOTHERNUMERIC', 'RPAREN', 'LPAREN',
          'RBRACKET', 'LBRACKET', 'COMMA', 'SEMICOLON',
          'PLUS', 'MINUS', 'APPROX', 'TIMES', 'DIV', 'EQUAL',
          'NOTEQUAL', 'SMALLER', 'BIGGER', 'SEQUAL', 'BEQUAL',
           'AND', 'OR', 'COLONEQUAL')

t_ignore = ' \t'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIV = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_NUMBER(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Invalid Token: ", t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()