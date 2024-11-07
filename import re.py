import re

class Scanner:
    def __init__(self):
        self.keywords = {
            "int": ("keyword", "INT"),
            "float": ("keyword", "FLOAT"),
            "long": ("keyword", "LONG"),
            "double": ("keyword", "DOUBLE"),
            "char": ("keyword", "CHAR"),
            "string": ("keyword", "STRING"),
            "if": ("keyword", "IF"),
            "else": ("keyword", "ELSE"),
            "for": ("keyword", "FOR"),
            "const": ("keyword", "CONST"),
            "bool": ("keyword", "BOOL"),
            "return": ("keyword", "RETURN"),
            "auto": ("keyword", "AUTO"),
            "break": ("keyword", "BREAK"),
            "case": ("keyword", "CASE"),
            "continue": ("keyword", "CONTINUE"),
            "default": ("keyword", "DEFAULT"),
            "do": ("keyword", "DO"),
            "goto": ("keyword", "GOTO"),
            "short": ("keyword", "SHORT"),
            "signed": ("keyword", "SIGNED"),
            "sizeof": ("keyword", "SIZEOF"),
            "static": ("keyword", "STATIC"),
            "struct": ("keyword", "STRUCT"),
            "switch": ("keyword", "SWITCH"),
            "typedef": ("keyword", "TYPEDEF"),
            "unsigned": ("keyword", "UNSIGNED"),
            "void": ("keyword", "VOID"),
            "while": ("keyword", "WHILE")
        }

        self.operators = {
            "=": ("operator", "ASSIGN"),
            "+": ("operator", "PLUS"),
            "-": ("operator", "MINUS"),
            "*": ("operator", "MULT"),
            "/": ("operator", "DIV"),
            "++": ("operator", "PLUSPLUS"),
            "--": ("operator", "MINUSMINUS"),
            "==": ("operator", "EQ"),
            "<=": ("operator", "LESS_EQ"),
            ">=": ("operator", "GREATER_EQ"),
            "!=": ("operator", "NEQ"),
            "<": ("operator", "LESS_THAN"),
            ">": ("operator", "GREATER_THAN"),
            "||": ("operator", "OR"),
            "!": ("operator", "NOT"),
            "&&": ("operator", "AND")
        }

        self.special_chars = {
            "(": ("specialChar", "LPAREN"),
            ")": ("specialChar", "RPAREN"),
            "{": ("specialChar", "LQURLY"),
            "}": ("specialChar", "RQURLY"),
            ";": ("specialChar", "SEMICOLON")
        }

        self.numeric_const_pattern = re.compile(r"-?\d+(\.\d*)?")
        self.identifier_pattern = re.compile(r"[a-zA-Z_][a-zA-Z0-9_]*")
        self.string_pattern = re.compile(r"\".*?\"")
        self.comment_pattern = re.compile(r"//.*|/\*[\s\S]*?\*/")

    def extract_lexems(self, input_string):
        lexems = []
        comments = self.comment_pattern.findall(input_string)
        for comment in comments:
            lexems.append((comment, "comment", "COMMENT"))
            input_string = input_string.replace(comment, '')
        # Split tokens
        tokens = re.split(r'(\s+|[();,{}]|==|<=|>=|!=|&&|\|\||\+{1,2}|-{1,2}|[*\/=!<>]|=)', input_string)

        for token in tokens:
            token = token.strip()
            if not token:
                continue
            if token in self.keywords:
                lexems.append((token, *self.keywords[token]))
            elif token in self.operators:
                lexems.append((token, *self.operators[token]))
            elif token in self.special_chars:
                lexems.append((token, *self.special_chars[token]))
            elif self.string_pattern.fullmatch(token):
                lexems.append((token, "String", "STRING"))
            elif self.numeric_const_pattern.fullmatch(token):
                lexems.append((token, "NumericConst", "NUMCONST"))
            elif self.identifier_pattern.fullmatch(token):
                lexems.append((token, "Identifier", "ID"))

        return lexems

# Create an instance of Scanner
scanner = Scanner()

# Get user input for code
print("Enter the code to be scanned:")
input_string = input()

# Extract lexemes
lexems = scanner.extract_lexems(input_string)

# Print lexemes
for lexem in lexems:
    print(f"Lexeme: {lexem[0]}, Type: {lexem[1]}, Class: {lexem[2]}")
