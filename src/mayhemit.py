#!/usr/bin/python3

import atheris
import sys

@atheris.instrument_func
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    str = fdp.ConsumeString(3)

    if str == "Bug":
        raise Exception("You got it!")

atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()