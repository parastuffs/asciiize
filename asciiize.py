#!/usr/bin/python

import sys

"""
Usage: ./asciiize <string to ASCII-ize>
Only lower case, spaces allowed.
https://gist.github.com/parastuffs/e497d81dd14c7daba094
"""

a = "   ###     \n" + \
    "  ## ##    \n" + \
    " ##   ##   \n" + \
    "##     ##  \n" + \
    "#########  \n" + \
    "##     ##  \n" + \
    "##     ##  "

b = "########   \n" + \
    "##     ##  \n" + \
    "##     ##  \n" + \
    "########   \n" + \
    "##     ##  \n" + \
    "##     ##  \n" + \
    "########   "

c = " #######   \n" + \
    "##     ##  \n" + \
    "##         \n" + \
    "##         \n" + \
    "##         \n" + \
    "##     ##  \n" + \
    " #######   "

d = "######     \n" + \
    "##    ##   \n" + \
    "##     ##  \n" + \
    "##     ##  \n" + \
    "##     ##  \n" + \
    "##    ##   \n" + \
    "######     "

e = "#########  \n" + \
    "##         \n" + \
    "##         \n" + \
    "######     \n" + \
    "##         \n" + \
    "##         \n" + \
    "#########  "

f = "#########  \n" + \
    "##         \n" + \
    "##         \n" + \
    "######     \n" + \
    "##         \n" + \
    "##         \n" + \
    "##         "

g = " #######   \n" + \
    "##         \n" + \
    "##         \n" + \
    "##   ####  \n" + \
    "##     ##  \n" + \
    "##     ##  \n" + \
    "########   "

h = "##     ##  \n" + \
    "##     ##  \n" + \
    "##     ##  \n" + \
    "#########  \n" + \
    "##     ##  \n" + \
    "##     ##  \n" + \
    "##     ##  "

i = "########   \n" + \
    "   ##      \n" + \
    "   ##      \n" + \
    "   ##      \n" + \
    "   ##      \n" + \
    "   ##      \n" + \
    "########   "

j = " ########  \n" + \
    "    ##     \n" + \
    "    ##     \n" + \
    "    ##     \n" + \
    "    ##     \n" + \
    "#   ##     \n" + \
    " ####      "

k = "##   ##    \n" + \
    "##  ##     \n" + \
    "## ##      \n" + \
    "####       \n" + \
    "##  ##     \n" + \
    "##   ##    \n" + \
    "##    ##   "

l = "##         \n" + \
    "##         \n" + \
    "##         \n" + \
    "##         \n" + \
    "##         \n" + \
    "##         \n" + \
    "#########  "

m = "##       ##  \n" + \
    "###     ###  \n" + \
    "## ## ## ##  \n" + \
    "##  ###  ##  \n" + \
    "##       ##  \n" + \
    "##       ##  \n" + \
    "##       ##  "

n = "##      ##  \n" + \
    "###     ##  \n" + \
    "## ##   ##  \n" + \
    "##  ##  ##  \n" + \
    "##   ## ##  \n" + \
    "##     ###  \n" + \
    "##      ##  "

o = "  #####    \n" + \
    "##     ##  \n" + \
    "##     ##  \n" + \
    "##     ##  \n" + \
    "##     ##  \n" + \
    "##     ##  \n" + \
    "  #####    "

p = "########   \n" + \
    "##     ##  \n" + \
    "##     ##  \n" + \
    "#######    \n" + \
    "##         \n" + \
    "##         \n" + \
    "##         "

q = "  #####    \n" + \
    "##     ##  \n" + \
    "##     ##  \n" + \
    "##     ##  \n" + \
    "##    # #  \n"+ \
    "  #### #   \n"+ \
    "        #  "

r = "########   \n" + \
    "##     ##  \n" + \
    "##     ##  \n" + \
    "########   \n" + \
    "##   ##    \n" + \
    "##    ##   \n" + \
    "##     ##  "

s = " #######   \n" + \
    "##     ##  \n" + \
    "##         \n" + \
    " #######   \n" + \
    "       ##  \n" + \
    "##     ##  \n" + \
    " #######   "

t = "##########  \n" + \
    "    ##      \n" + \
    "    ##      \n" + \
    "    ##      \n" + \
    "    ##      \n" + \
    "    ##      \n" + \
    "    ##      "

u = "##     ##  \n" + \
    "##     ##  \n" + \
    "##     ##  \n" + \
    "##     ##  \n" + \
    "##     ##  \n" + \
    "##     ##  \n" + \
    " #######   "

v = "##     ##  \n" + \
    "##     ##  \n" + \
    "##     ##  \n" + \
    "##     ##  \n" + \
    " ##   ##   \n" + \
    "  ## ##    \n" + \
    "   ###     "

w = "##           ##  \n" + \
    "##           ##  \n" + \
    "##           ##  \n" + \
    "##           ##  \n" + \
    " ##   ###   ##   \n" + \
    "  ## ## ## ##    \n" + \
    "   ###   ###     "

x = "##    ##   \n" + \
    " ##  ##    \n" + \
    "  ####     \n" + \
    "   ##      \n" + \
    "  ####     \n" + \
    " ##  ##    \n" + \
    "##    ##   "

y = "##    ##   \n" + \
    " ##  ##    \n" + \
    "  ####     \n" + \
    "   ##      \n" + \
    "   ##      \n" + \
    "   ##      \n" + \
    "   ##      "

z = "#########  \n" + \
    "      ##   \n" + \
    "    ###    \n" + \
    "  ###      \n" + \
    " ##        \n" + \
    "#########  "

space = "       \n" + \
        "       \n" + \
        "       \n" + \
        "       \n" + \
        "       \n" + \
        "       \n" + \
        "       "


underscore = "        \n" + \
             "        \n" + \
             "        \n" + \
             "        \n" + \
             "        \n" + \
             "        \n" + \
             "####### "


hyphen = "        \n" + \
             "        \n" + \
             "        \n" + \
             "  ####  \n" + \
             "        \n" + \
             "        \n" + \
             "        "


asciiAlphabet = list()
asciiAlphabet.append(a)
asciiAlphabet.append(b)
asciiAlphabet.append(c)
asciiAlphabet.append(d)
asciiAlphabet.append(e)
asciiAlphabet.append(f)
asciiAlphabet.append(g)
asciiAlphabet.append(h)
asciiAlphabet.append(i)
asciiAlphabet.append(j)
asciiAlphabet.append(k)
asciiAlphabet.append(l)
asciiAlphabet.append(m)
asciiAlphabet.append(n)
asciiAlphabet.append(o)
asciiAlphabet.append(p)
asciiAlphabet.append(q)
asciiAlphabet.append(r)
asciiAlphabet.append(s)
asciiAlphabet.append(t)
asciiAlphabet.append(u)
asciiAlphabet.append(v)
asciiAlphabet.append(w)
asciiAlphabet.append(x)
asciiAlphabet.append(y)
asciiAlphabet.append(z)
asciiAlphabet.append(space)
asciiAlphabet.append(underscore)
asciiAlphabet.append(hyphen)

romanAlphabet = list()
romanAlphabet.append('a')
romanAlphabet.append('b')
romanAlphabet.append('c')
romanAlphabet.append('d')
romanAlphabet.append('e')
romanAlphabet.append('f')
romanAlphabet.append('g')
romanAlphabet.append('h')
romanAlphabet.append('i')
romanAlphabet.append('j')
romanAlphabet.append('k')
romanAlphabet.append('l')
romanAlphabet.append('m')
romanAlphabet.append('n')
romanAlphabet.append('o')
romanAlphabet.append('p')
romanAlphabet.append('q')
romanAlphabet.append('r')
romanAlphabet.append('s')
romanAlphabet.append('t')
romanAlphabet.append('u')
romanAlphabet.append('v')
romanAlphabet.append('w')
romanAlphabet.append('x')
romanAlphabet.append('y')
romanAlphabet.append('z')
romanAlphabet.append(' ')
romanAlphabet.append('_')
romanAlphabet.append('-')


entry = sys.argv[1]
# TODO Check if there is an argument
# TODO print help
# TODO parse the argument to check if there isn't forbidden chars
entryChars = list()
for char in entry:
    entryChars.append(char)

myString = ""
for row in xrange(0, space.split('\n').__len__()):
    for char in entryChars:
        myString += asciiAlphabet[romanAlphabet.index(char)].split('\n')[row]
    myString += "\n"

print myString
