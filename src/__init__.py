"""Translates a string to English or a specified language,
auto-detecting the source language with the Cloud Translate API.

Usage: tr [to:<lang-code>] <text to translate>"""

import os
import json
import configparser
from albertv0 import *
from urllib.parse import quote as quote_url

__iid__ = "PythonInterface/v0.2"
__author__ = "Thiago Costa"
__prettyname__ = "My Translation"
__version__ = "1.0.0"
__trigger__ = "tr "
__dependencies__ = []

iconPath = os.path.dirname(__file__) + "/icon.png"
client = None

source = "auto"
targets = ["pt", "en", "ja", "fr", "it"]


def handleQuery(query):
    if not query.isTriggered:
        return

    str = query.string.strip()
    items = []

    if str == "":
        return makeItem(query, subtext="Usage: `tr [:lang-code] [string to translate]`")

    if (str[0] == ":"):
        target = str.split(' ')[0][1:]
        str = ' '.join(str.split(' ')[1:])
        if lang.has(target):
            item = translatorItem(query, source, target, str)
        else:
            item = badLanguageItem(query, target)
        items.append(item)

    else:
        for target in targets:
            item = translatorItem(query, source, target, str)
            items.append(item)

    return items


def translatorItem(query, source, target, str):
    item = makeItem(
        query, "View in Google Translate to {}".format(
            lang.toName(target)),
        "https://translate.google.com/#{}/{}/{}".format(
            source, target, quote_url(str, safe='')
        ))
    item.addAction(UrlAction(
        "View in Google Translate",
        "https://translate.google.com/#{}/{}/{}".format(
            source, target, quote_url(str, safe=''))
    ))
    return item


def badLanguageItem(query, lang):
    item = makeItem(query, "Translation failed",
                    "{} is not a valid language.".format(lang))
    item.addAction(UrlAction("Open list of support languages",
                             "https://cloud.google.com/translate/docs/languages"))
    return item


def makeItem(query=None, text=__prettyname__, subtext=""):
    return Item(
        id=__prettyname__,
        icon=iconPath,
        text=text,
        subtext=subtext,
        completion=query.rawString
    )


class Lang:
    langPath = os.path.dirname(__file__) + "/languages.json"
    languages = dict()

    def __init__(self):
        if os.path.exists(self.langPath):
            debug("Loading support languages from " + self.langPath)
            with open(self.langPath) as langJson:
                self.languages = json.load(langJson)

    def has(self, code):
        return code in self.languages

    def toCode(self, name):
        return self.languages.keys()[languages.values().index(name)]

    def toName(self, code):
        return self.languages.get(code)


lang = Lang()
