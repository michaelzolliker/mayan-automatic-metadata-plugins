import mambase
import helper

class DefaultInvoice(mambase.RegexMetaDataCheck):
    __documentclass__ = "Invoice"
    __tags__ = []
    __filter__ = lambda s, x: ("" in x)
    __meta__ = [
    ]

class DefaultContract(mambase.RegexMetaDataCheck):
    __documentclass__ = "Contract"
    __tags__ = []
    __filter__ = lambda s, x: ("" in x)
    __meta__ = [
    ]

__plugin__ = [DefaultInvoice, DefaultContract]
