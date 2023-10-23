Selles ülesandes tutvume funktsiooni mõistega. Me võime mõelda nii, et funktsioon on nimega alamprogramm, mida saame parameetritega juhtida. Aga mida see tähendab?

Me loome funktsiooni, millele anname nime. Sinna funktsiooni sisse (lähtekoodis funktsiooni definitsiooni alla ridadele) kirjutame koodi. Nüüd iga kord, kui meil on neid koodiridu vaja kasutada, saame pöörduda funktsiooni poole.

Funktsiooni kirjeldamiseks defineerimse selle nii:

```python
def function_name():
```

See loob funktsiooni, mille nimi on `function_name`. Sulud on vajalikud. Sinna sisse saab lisada parameetreid.

Funktsiooni sisu kirjutatakse funktsiooni definitsiooni alla. Oluline on järgida, et kogu funktsiooni sisu on taandega (4 või enam tühikut on ees). Vastasel juhul ei ole koodirida enam osa funktsioonist:

```python
def my_awesome_function():
    print("I'm in function")
    print("Me too!")
print("I'm out already :(")
```

Eelmises näites kaks print-korraldust on funktsiooni sisu, kolmas print-korraldus on juba funktsioonist väljas.

Selleks, et oma funktsiooni välja kutsuda, tuleb seda nimepidi välja kutsuda:

```python
my_awesome_function()
```

Siin on jälle oluline sulud märkida nime taha. Sulgude sisse saab anda kaasa argumente (need siis antakse funktsiooni definitsioonis kirjeldatud parameetritesse). Täpsemalt saate juba lugeda viidetest allpool.

Siin ülesandes tuleb lahendada alamülesanded. Mõistlik on neid lahendada ükshaaval.

Lugemist:

- [Funktsiooni mõiste ja kasutamine](https://pydoc.pages.taltech.ee/function/func_overview.html "function overview")
- [Funktsioon, selle argumendid ning parameetrid](https://pydoc.pages.taltech.ee/function/func.html "function")

---

Kirjuta funktsioon `print_hello()`, mis prindib ekraanile "Hello". Funktsioonil parameetreid pole.

---

Kirjuta funktsioon `get_hello()`, mis tagastab sõne "Hello". Parameetrid puuduvad.

---

Realiseeri funktsioon `ask_name_and_greet_user`, millel ei ole parameetreid ja mis ei tagasta midagi, 
vaid küsib kasutaja nime (küsimuse tekst ei ole oluline) ning prindib konsooli järgmise sõnumi: `Hi, *capitalized_name*. Would you like to have a Hamburger?`. 
Kus `*capitalized_name*` on kasutaja nimi, millele on rakendatud funktsioon `capitalize` (teeb esimese tähe suureks ja ülejaanud väikesteks).

Kui nimi on `Thanos` (tõstutundetu), siis prindi ilusa sõnumi asemel konsooli `Get out of here, Thanos! Nobody wants to play with you!`

Lugemist:

[Funktsiooni mõiste ja kasutamine](https://pydoc.pages.taltech.ee/function/func_overview.html "function")

---

Realiseeri funktsioon `calculate_hypotenuse_length`, mis saab sisendiks kahe kaateti täisarvulised pikkused
ja arvutab ning tagastab hüpotenuusi pikkuse. Tagastatav pikkus võib olla ujukoma arv.

Realiseeri funktsioon `calculate_cathetus_length`, mis saab sisendiks kaateti ja hüpotenuusi täisarvulised pikkused
ja arvutab ning tagastab teise kaateti pikkuse. Tagastatav pikkus võib olla ujukoma arv.

Võid eeldada, et sisend on alati positiivne täisarv (ehk seda kontrollima ei pea). Teise funktsiooni puhul võid ka eeldada,
et hüpotenuusi pikkus on alati suurem kui kaateti pikkus.

Lugemist:

- [Funktsiooni mõiste ja kasutamine](https://pydoc.pages.taltech.ee/function/func_overview.html "function")
- [Funktsioon, selle argumendid ning parameetrid](https://pydoc.pages.taltech.ee/function/func.html "func_params")
