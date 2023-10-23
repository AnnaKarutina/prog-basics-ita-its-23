# Funktsioon

Funktsioone iseloomustab võtmesõna `def`. Funktsiooni loomisel tuleb peale võtmesõna def kirjutada talle nimi ja seejärel sulud.
Funktsiooni sisemus käivitub iga kord, kui funktsioon välja kutsutakse.

Samuti võib funktsioonis olla, aga ei pea, võtmesõna `return`.
Võtmesõna `return` lõpetab otsekohe funktsiooni töö ja tagastab määratud väärtuse.

Kui soovid lähemalt uurida, on meil hea dokumentatsioon PyDocis ka olemas: 
[Funktsiooni mõiste ja kasutamine PyDoc](https://pydoc.pages.taltech.ee/function/func_overview.html)

Näited:
```
def func():
    print("Hello from the function")

>>> func()
Hello from the function
```

```
def greet(name):
    print("Hello, " + name)

>>> greet('Mari')
Hello, Mari
```

```
def greet(name):
    return "Hello " + name

>>> print(greet('Mari'))
Hello, Mari
```


## 1. Inside the function
* Loo funktsioon `func()`.
* Kirjutada funktsiooni "sisemus" nii, et igakord kui funktsiooni välja kutsuda, 
prinditakse konsooli `I´m inside the function`


## 2. My name is ...
* Loo funktsioon `my_name_is(name)`.
* Funktsiooni sisendiks on `string`, mallis on muutuja nimeks `name`.
* Kirjutada funktsiooni "sisemus" nii, et igakord kui funktsiooni välja kutsuda, 
prinditakse konsooli `My name is [name]`, kus `[name]` asemel prinditakse functiooni sisendiks antud nimi.
Näiteks kui kutsutakse välja funtiooni `my_name_is("Mari")`, prinditakse konsooli `My name is Mari`


## 3. Sum six
* Loo funktsioon `sum_six(num)`.
* Funktsiooni sisendiks on `int`
* Funktsioon peab tagastama(return) number 6 ja funktiooni sisendi summa

Näited:  
`print(sum_six(1)  # --> 7`  
`print(sum_six(6)  # --> 12`  

## 4. Sum numbers
* Loo funktsioon `sum_numbers()`.
* Funktsiooni sisendiks on kaks täisarvu `int`, need võib tähistada näiteks `a` ja `b`. Mitme funktsiooni sisendu puhul
eraldatakse need sulgude sees komaga. Nt: `func(a, b)`  
* Funktsioon peab tagastama(return) sisendite summa.

Näited:  
`print(sum_numbers(5, 5)  # --> 10`  
`print(sum_numbers(0, 25)  # --> 25`  

## 5. USD to EUR
* Loo funktsioon `usd_to_eur()`.
* Funktsiooni sisendiks on täisarv `int`
* Kirjuta funktsioon nii, et kui sisendiks on rahasumma dollarites, tagastab funktsioon summa eurodes.
Funktsooni testimiseks oletame, et antud hetkel on kurss 1USD = 0.8EUR.
Näited:  
`print(usd_to_eur(100)  # --> 80`  
