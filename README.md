# Albert Translation Plugin

## Instalation

1. Install the latest  version of albert https://albertlauncher.github.io/docs/installing/
```
echo 'deb http://download.opensuse.org/repositories/home:/manuelschneid3r/xUbuntu_20.04/ /' | sudo tee /etc/apt/sources.list.d/home:manuelschneid3r.list
sudo wget -nv https://download.opensuse.org/repositories/home:manuelschneid3r/xUbuntu_20.04/Release.key -O "/etc/apt/trusted.gpg.d/home:manuelschneid3r.asc"
sudo apt update
sudo apt install albert
```

2. Clone this repo 
```
git clone git@github.com:ThiagoCosta360/albert-translator.git
```

3. Install the plugin
```
make install --directory=~/Projects/albert-translator/
```
 
4. Restart Albert
   
5. Open albert settings, Extensions tab, check Python, check 'My translation'

## Introducion

    The search will open a new tab with google translator with the query and output language.
    If no output language is provided, 5 main options will be shown.

* Triger string `tr`
* Language output `:lang-code`  see available language codes [here](src/languages.json) 
* Automatically detect input text language

    Examples:

```
tr  hello world!
tr :en olá mundo!
tr :ja  Bonjour le monde!
```
