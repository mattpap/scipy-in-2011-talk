Understanding importance of automated software testing
======================================================

:author: Mateusz Paprocki <mattpap@gmail.com>

Abstract
--------

Development of scientific programs isn't much different than development
of computer programs of any other kind. One of the key characteristic of
computer programs is correctness. No matter whether we create programs
for our own purpose or for other parties, we do not want to spent hours
or days waiting for results of computations that will be flawed from the
very beginning. As long as programs consist of few lines of code, we may
be able to verify correctness of all cases in those programs manually after
every change or even try to prove their correctness. However, real life
programs consist of thousands, hundred thousands or even millions of lines
of code, and even more states. In such a setup we need tools and methods
that would allow to automate the process of software testing.

Python, a programming language with a weak dynamic type system, makes the
use of automated software testing even more important because in this case
test suites and the testing framework of choice have to accommodate for the
weaknesses of the language. Also, agile software development techniques may
intrinsically require automated testing as their core component to guarantee
effectiveness of those methods.

In this talk I will show how to do automated testing of programs written
in Python. Test automation tools will be described and common issues and
pitfalls outlined. I will also discuss the notion of code coverage with
tests and testing via examples (doctests).
