#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import cppclasses

x = cppclasses.MuttableDouble(0.0)

foo = cppclasses.Foo(x)
foo.increment()
foo.increment()

print x.value

#help(cppclasses)
