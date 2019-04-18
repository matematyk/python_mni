Parser wyrażeń matematycznych: 



```gramatyka:
 E = S (('+'|'-') S)*      # wyrazenie (+,-) (- binarny)
 S = C (('*'|'/') C)*      # skladnik (*,/)
 C = N | '-'C | '('E')'    # czynnik  (- unitarny)
 N = n                     # liczba
 ```
