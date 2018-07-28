---
permalink: "/en/theory/"
title: "A Little Bit of Theory"
---

One of the exercises in educational research is deciding what we mean
by "learning", which turns out to be pretty complicated once you start
looking beyond the standardized Western classroom. Within the broad
scope of [educational psychology](#g:educational-psychology), two
specific perspectives have primarily influenced my teaching. The first
is [cognitivism](#g:cognitivism), which focuses on things like pattern
recognition, memory formation, and recall. It is good at answering
low-level questions, but generally ignores larger issues like, "What
do we mean by 'learning'?" and, "Who gets to decide?" The second is
[situated learning](#g:situated-learning), which focuses on bringing
people into a community, and recognizes that teaching and learning are
always rooted in who we are and who we aspire to be. We will discuss
it in more detail in [s:community](#CHAPTER).

The [Learning Theories website][learning-theories] and
[[Wibu2016](#CITE)] have good summaries of these and other
perspectives.  Besides cognitivism, those encountered most frequently
include [behaviorism](#g:behaviorism) (which treats education as
stimulus/response conditioning), [constructivism](#g:constructivism)
(which considers learning an active process during which learners
construct knowledge for themselves), and
[connectivism](#g:connectivism) (which holds that knowledge is
distributed, that learning is the process of navigating, growing, and
pruning connections, and which emphasizes the social aspects of
learning made possible by the Internet). It would help if their names
were less similar, but setting that aside, none of them can tell us
how to teach on their own because in real life, several different
teaching methods might be consistent with what we currently know about
how learning works. We therefore have to try those methods in the
class, with actual learners, in order to find out how well they
balance the different forces in play.

Doing this is called [instructional design](#g:instructional-design).
If educational psychology is the science, instructional design is the
engineering. For example, there are good reasons to believe that
children will learn how to read best by starting with the sounds of
letters and working up to words. However, there are equally good
reasons to believe that children will learn best if they are taught to
recognize entire simple words like "open" and "stop", so that they can
start using their knowledge sooner.

The first approach is called "phonics", and the second, "whole
language". The whole language approach may seem upside down, but more
than a billion people have learned to read and write Chinese and similar
ideogrammatic languages in exactly this way. The only way to tell which
approach works best for most children, most of the time, is to try them
both out. These studies have to be done carefully, because so many other
variables can have an impact on rules. For example, the teacher's
enthusiasm for the teaching method may matter more than the method
itself, since children will model their teacher's excitement for a
subject. (With all of that taken into account, phonics does seem to be
better than other approaches [[Foor1998](#CITE)].)

As frustrating as the maybes and howevers in education research are,
this kind of painstaking work is essential to dispel myths that can
get in the way of better teaching. One [well-known
myth][learning-modalities] is that people are visual, auditory, or
kinesthetic learners, and that teaching is more effective when lessons
are designed according to whether they like to see things, hear
things, or do things. This idea is easy to understand, but as
[[DeBr2015](#CITE)] explains, it is almost certainly
false. Unfortunately, that hasn't stopped companies from marketing
products based on it to parents, school boards, and the general
public.

Similarly, the learning pyramid that shows we remember 10% of what we
read, 20% of what we hear, and so on?  [Myth][learning-pyramid].  The
idea that "brain games" can improve our intelligence, or at least slow
its decline in old age? Also a myth, as are the claims that the
Internet is making us dumber or that young people read less than they
used to. Just as we need to clear away our learners' misconceptions in
order to help them learn, we need to clear away our own about teaching
if we are to teach more effectively.

## Notional Machines

The term [computational thinking](#g:computational-thinking) is
bandied about a lot, in part because people can agree it's important
while meaning very different things by it. I find it more useful to
think in terms of getting learners to understand a [notional
machine](#g:notional-machine). The term was introduced in
[[DuBo1986](#CITE)], and means abstraction of the structure and
behavior of a computational device. According to [[Sorv2013](#CITE)],
a notional machine:

- is an idealized abstraction of computer hardware and other aspects
  of the runtime environment of programs;

- serves the purpose of understanding what happens during program
  execution;

- is associated with one or more programming paradigms or languages,
  and possibly with a particular programming environment;

- enables the semantics of program code written in those paradigms or
  languages (or subsets thereof) to be described;

- gives a particular perspective to the execution of programs; and

- correctly reflects what programs do when executed.

For example, my notional machine for Python is:

1. Running programs live in memory, which is divided between a call
   stack and a heap.

1. Memory for data is always allocated from the heap.

1. Every piece of data is stored in a two-part structure: the first
   part says what type the data is, and the second part is the actual
   value.

1. Atomic data like Booleans, numbers, and character strings are stored
   directly in the second part. These values are never modified after
   they are created.

1. The scaffolding for collections like lists and sets are also stored
   in the second part, but they store references to other data rather
   than storing those values directly. The scaffolding may be modified
   after it is created, e.g., a list may be extended or new key/value
   pairs may be added to a dictionary.

1. When code is loaded into memory, Python parses it and converts it to
   a sequence of instructions that are stored like any other data.
   (This is why it's possible to alias functions and pass them as
   parameters.)

1. When code is executed, Python steps through the instructions, doing
   what each tells it to in turn.

1. Some instructions make Python read data, operate on it, and create
   new data.

1. Other instructions make Python jump to other instructions instead of
   executing the next one in sequence; this is how conditionals and
   loops work.

1. Yet another instruction tells Python to call a function, which means
   temporarily switching from one blob of instructions to another.

1. When a function is called, a new stack frame is pushed on the call
   stack.

1. Each stack frame stores variables' names and references to data.
   (Function parameters are just another kind of variable.)

1. When a variable is used, Python looks for it in the top stack frame.
   If it isn't there, it looks in the bottom (global) frame.

1. When the function finishes, Python erases its stack frame and
   switches from its blob of instructions back to the blob that called
   it. If there isn't a "beforehand", the program has finished.

I don't try to explain all of this at once, but I draw on this mental
model over and over again as I draw pictures, trace execution, and so
on. After about 25 hours of class and 100 hours of work on their own
time, I expect adult learners to be able to understand most of it.

{% include links.md %}
