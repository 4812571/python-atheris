#!/usr/bin/python3

import atheris
import sys

def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    my_str = fdp.ConsumeString(3)

    if my_str == "bug":
        raise Exception("You got it!")

atheris.instrument_all()
atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()