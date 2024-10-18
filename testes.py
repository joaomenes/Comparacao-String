from comparacaoString import solution

#Testes para corretos
fixed_tests_True = (
    ("samurai", "ai"),
    ("ninja", "ja"),
    ("sensei", "i"),
    ("abc", "abc"),
    ("abcabc", "bc"),
    ("fails", "ails"),
)

# Testes para falharem
fixed_tests_False = (
    ("sumo", "omo"),
    ("samurai", "ra"),
    ("abc", "abcd"),
    ("ails", "fails"),
    ("this", "fails"),
    ("spam", "eggs"),
)

def test_solution():
    # Retorna True
    for text, ending in fixed_tests_True:
        assert solution(text, ending) == True, f"Falhou: {text}.endswith({ending}) deveria ser True"
    
    # Retorna false
    for text, ending in fixed_tests_False:
        assert solution(text, ending) == False, f"Falhou: {text}.endswith({ending}) deveria ser False"


test_solution()
print("Todos os testes passaram!") #Caso  todos passem
