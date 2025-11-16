# 🧩 Overview
**caser** module provides you the most common cases in python & text methods simply & explicitly.

---

## cased class ⚒️
this class provides every feature of this module, from the path/case/style to repeating the text in the matter of moments.
It's all simple: make an instance of _cased_ class:
```python
from caser import cased

example: cased = cased("I love python")
```
And now you unlocked all the features, and you can do such things like:
```python
print(example.ct_vowels()) # 5
print(example.snake()) # 'I_love_python'
print(example.Pascal().swapcase()) # 'i lOVE pYTHON'
```
---

### 🔠 Cases
From the available cases are:
| case | view |
| ---- | -------- |
| snake() | snake_case |
| pascal() | PascalCase |
| kebab() | kebab-case |
| upper snake() | SCREAMING_CASE |
| train() | Capitalized-Kebab-Case |


--- 

## 🧰 Installation
Install directly from PyPi:
	
```bash
pip install caser
```

or from github:

```bash
git clone https://github.com/johnathan31/caser.git
cd caser
pip install .
```

