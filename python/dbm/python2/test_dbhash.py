#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2012 Jérémie DECOCK (http://www.jdhp.org)

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import dbhash
import whichdb

def main():
    """Main function"""

    # WRITE #######

    db = dbhash.open('foo_dbhash', 'c')

    db['one'] = 'un'
    db['two'] = 'dos'
    db['three'] = 'tres'

    db.close()

    # WHICH DBM ###

    print "whichdb:", whichdb.whichdb('foo_dbhash')
    print 

    # READ ########

    db = dbhash.open('foo_dbhash', 'r')

    # Iterate loop: first method (common to any dbm module)
    for k in db.keys():
        print k, ':', db[k]

    # Iterate loop: second method (dbhash supports db.items())
    for k, v in db.items():
        print k, ':', v

    # Iterate loop: third method (the most efficient)
    # The following code prints every key in the database db, without having to create a list in memory that contains them all.
    print db.first()
    for i in xrange(1, len(db)):
        print db.next()

    db.close()


if __name__ == '__main__':
    main()
