from cases import cased

def test_classCased():
     assert cased("hello world").mocking() == 'HELLO world'
     
     assert cased("hello world").mocking(True) == 'HeLlO WoRlD'
     
     
     assert cased("get element by id").camel() == 'getElementById'
     
     assert cased("get element by id").camel(True) == 'get Element By Id'
     
     
     assert cased("the kings valley").Pascal(spaced=False) == 'TheKingsValley'
     
     assert cased("the prisoner of zenda").Pascal() == 'The Prisoner Of Zenda'
     
     
     assert cased("input user answer").snake() == 'input_user_answer'
     
     
     assert cased("clear cache post run").kebab() == 'clear-cache-post-run'
     
     
     assert cased("data data colab terminal localStorage").path() == 'data/data/colab/terminal/localStorage'
     
     
     assert cased("max speed limit").upper_snake() == 'MAX_SPEED_LIMIT'
     
     
     assert cased("auto checked out").train() == 'Auto-Checked-Out'
     
     
     assert cased("index html txt").dot() == 'index.html.txt'
     
     
     assert cased("Hello").swapcase() == 'hELLO'
     
     
     assert cased("python").reverse(True) == 'nohtyp'
     
     
     assert cased("¥out¢ub£").to_ascii() == 'outub'
     
     
     assert cased("Java").rm_vowels() == 'Jv'
     
     
     assert cased("row ").repeat(4) == 'row row row row '
     
     assert cased("kotlin").ct_constants() == 4
     
     assert cased("kotlin").ct_vowels() == 2
     
     