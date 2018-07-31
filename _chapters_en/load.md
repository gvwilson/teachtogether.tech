---
permalink: "/en/load/"
title: "Cognitive Load"
objectives:
- Define cognitive load and explain how consideration of it can be
  used to shape instruction.
- Explain what faded examples are and construct faded examples for
  use in programming workshops.
- Explain what Parsons Problems are and construct Parsons Problems
  for use in programming workshops.
- Explain how multimedia should and shouldn't be used in teaching
  and why.
- Describe ways instructors differ from students and what effect
  those differences have on instruction.
---

In [[Kirs2006](#CITE)], Kirschner, Sweller and Clark wrote:

> Although unguided or minimally guided instructional approaches are
> very popular and intuitively appealing...these approaches
> ignore both the structures that constitute human cognitive
> architecture and evidence from empirical studies over the past
> half-century that consistently indicate that minimally guided
> instruction is less effective and less efficient than instructional
> approaches that place a strong emphasis on guidance of the student
> learning process. The advantage of guidance begins to recede only when
> learners have sufficiently high prior knowledge to provide "internal"
> guidance.

Their paper set off a minor academic storm, because beneath the jargon
the authors were claiming that allowing learners to ask their own
questions, set their own goals, and find their own path through a
subject, as they would when solving problems in real life, isn't
effective. This approach---called
[inquiry-based learning](#g:inquiry-based-learning)---is
intuitively appealing, but the authors argued that it overloads learners
by requiring them to master a domain's factual content and its
problem-solving strategies at the same time.

More specifically, [cognitive load theory](#g:cognitive-load-theory)
posited that people have to deal with three things when they're
learning:

Intrinsic load
: is what people have to keep in mind in order to absorb new material.
  In a programming class, this might be understanding what a variable
  is, or understanding how assignment in a programming language is
  different from creating a reference to a cell in a spreadsheet.
  Intrinsic load can't be reduced except by reducing the amount of
  content being taught.

Germane load
: is the (desirable) mental effort required to link new information to
  old, which is one of the things that distinguishes learning from
  memorization. An example might be remembering that a loop variable
  is assigned a new value each time the loop executes.

Extraneous load
: is everything else in the instructional material that distracts from
  learning, such as matching the highlight colors in the instructor's
  examples to the different color scheme used by the learner's own
  editor.

Cognitive load theory holds that people have to split a fixed amount of
working memory between these three things. Our goal as instructors is to
maximize the memory available to handle germane load, which means
reducing the intrinsic load at each step and eliminating as much of the
extraneous load as possible.

For example, searching for a solution strategy is an extra burden on top
of actually applying that strategy. We can therefore accelerate learning
by giving learners worked examples that break a solution procedure down
into steps, each of which can be mastered on its own before being
combined with other steps (which is a step in its own right).

One way to do this is to give learners a series of
[faded examples](#g:faded-example). The first example
presents a nearly-complete use of the same problem-solving strategy just
demonstrated, but with a small number of blanks for the learner to fill
in. The next problem is of the same type, but has more blanks, and so on
until the learner is asked to solve the entire problem. The material
that *isn't* blank is often referred to as
[scaffolding](#g:scaffolding), since it serves the same
purpose as the scaffolding set up temporarily at a building site.

Faded examples can be used in almost every kind of teaching, from sport
and music to contract law. Someone teaching programming might use them
by first explaining how to calculate the total length of a list of
words:

    # total_length(["red", "green", "blue"]) => 12
    define total_length(list_of_words):
        total = 0
        for each word in list_of_words:
            total = total + word.length()
        return total

and then asking learners to fill in the blanks in this (which focuses
their attention on control structures):

    # word_lengths(["red", "green", "blue"]) => [3, 5, 4]
    define word_lengths(list_of_words):
        list_of_lengths = []
        for each ____ in ____:
            list_of_lengths.append(____)
        return list_of_lengths

The next problem might be this (which focuses their attention on
updating the final result):

    # join_all(["red", "green", "blue"]) => "redgreenblue"
    define join_all(list_of_words):
        joined_words = ____
        for each ____ in ____:
            ____
        return joined_words

Learners would finally be asked to write an entire function on their
own:

    # make_acronym(["red", "green", "blue"]) => "RGB"
    define make_acronym(list_of_words):
        ____

Faded examples work because they introduce the problem-solving strategy
piece by piece: at each step, learners have one new problem to tackle,
which is less intimidating than a blank screen or a blank sheet of paper
([s:classroom-practices](#SECTION)). It also encourages learners to
think about the similarities and differences between various approaches,
which helps create the linkages in their mental models that help
retrieval.

> **Efficiency vs. Extent**
> 
> Seeing worked examples accelerates learning more than having students
> write lots of code themselves [[Skud2014](#CITE)]. As we will see in
> [s:pck](#CHAPTER), deconstructing code by tracing it or debugging it
> also increases the efficiency of learning [[Grif2016](#CITE)]. However,
> this isn't the same as saying that people learn more unless they see
> additional problems.

The key to constructing a good faded example is to think about the
problem-solving strategy it is meant to teach. For example, the series
of problems are all examples of the *accumulator pattern*, in which the
results of processing items from a collection are repeatedly added to a
single variable in some way to create the final result.

Critics have sometimes argued that any result can be justified after the
fact by labelling things that hurt performance as extraneous load and
things that don't as intrinsic or germane. However, instruction based on
cognitive load theory is undeniably effective. For example,
[[Maso2016](#CITE)] redesigned a database course to remove split
attention and redundancy effects, and provide worked examples and
sub-goals. The new course reduced exam failure rate by 34% on an
identical final exam and increased student satisfaction.

A decade after the publication of [[Kirs2006](#CITE)], a growing number
of people believe that cognitive load theory and inquiry-based
approaches are compatible if viewed in the right way. [[Kaly2015](#CITE)]
argues that cognitive load theory is basically micro-management of
learning within a broader context that considers things like motivation,
while [[Kirs2018](#CITE)] extends cognitive load theory to include
collaborative aspects of learning. As with [[Mark2018](#CITE)] (discussed
in [s:individual-strategies](#SECTION)), researchers' perspectives may
differ, but the practical implementation of their theories often wind up
being the same.

> **Cognitive Apprenticeship**
> 
> An alternative model of learning and instruction that also uses
> scaffolding and fading is
> [cognitive apprenticeship](#g:cognitive-apprenticeship),
> which emphasizes the way in which a master passes on skills and
> insights to an apprentice. The master provides models of performance
> and outcomes, then coaches novices as they take their first steps by
> explaining what they're doing and why [[Coll1991](#CITE),[Casp2007](#CITE)]. The
> apprentice reflects on their own problem solving, e.g., by thinking
> aloud or critiquing their own work, and eventually explores problems
> of their own choosing.
> 
> This model tells us that instructors should present several examples
> when presenting a new idea so that learners can see what to
> generalize, and that we should vary the form of the problem to make it
> clear what are and aren't superficial features. (For a long time, I
> believed that the variable holding the value a function was going to
> return *had* to be called `result` because my instructor always used
> that name in examples.) Problems should be presented in real-world
> contexts, and we should encourage self-explanation, since it helps
> learners organize and make sense of what they have just been taught.
> This is discussed in more detail in
> [s:individual-strategies](#SECTION).

### Parsons Problems

Another kind of exercise that can be explained in terms of cognitive
load theory is called a [Parsons Problem](#g:parsons-problem)
(named after one of their creators [[Pars2006](#CITE)]). If you are
teaching someone to speak a new language, you could ask them a question,
and then give them the words they need to answer the question, but in
jumbled order. Their task is to put the words in the right order to
answer the question grammatically, which frees them from having to think
simultaneously about what to say *and* how to say it.

Similarly, when teaching people to program, you can give them the lines
of code they need to solve a problem, and ask them to put them in the
right order. This allows them to concentrate on control flow and data
dependencies, i.e., on what has to happen before what, without being
distracted by variable naming or trying to remember what functions to
call. Multiple studies have shown that Parsons Problems take less time
for learners to do, but produce equivalent educational outcomes
[[Eric2017](#CITE)].

### Labelled Subgoals

[Subgoal labelling](#g:subgoal-labelling) means giving names
to the steps in a step-by-step description of a problem-solving process.
[[Marg2016](#CITE),[Morr2016](#CITE)] all found that students with labelled
subgoals solved Parsons Problems better than students without, and the
same benefit is seen in other problem domains [[Marg2012](#CITE)].
Returning to the Python example used earlier, the subgoals in finding
the total length of a list of words or constructing an acronym are:

1. Create an empty value of the type to be returned.

1. Get the value to be added to the result from the loop variable.

1. Update the result with that value.

Labelling subgoals works because grouping related steps in a chunk
([s:memory-pattern](#SECTION)) and giving each chunk a name helps
learners distinguish between generic information and information that is
specific to the problem at hand, which reduces cognitive load. It also
helps them build a mental model of that kind of problem, so that they
can solve other problems of that kind, and gives them a natural
opportunity for self-explanation ([s:individual-strategies](#SECTION)).

## Split Attention {#s:load-split-attention}

Research by Mayer and colleagues on the
[split-attention effect](#g:split-attention-effect) is
closely related to cognitive load theory [[Maye2003](#CITE)]. Linguistic
and visual input are processed by different parts of the human brain,
and linguistic and visual memories are stored separately as well. This
means that correlating linguistic and visual streams of information
takes cognitive effort: when someone reads something while hearing it
spoken aloud, their brain can't help but check that it's getting the
same information on both channels (a topic we'll return to when
discussing dual coding in [s:individual-strategies](#SECTION)).

Learning is therefore more effective when information is presented
simultaneously in two different channels, but when that information is
complementary rather than redundant. For example, people generally find
it harder to learn from a video that has both narration and on-screen
captions than from one that has either the narration or the captions but
not both, because some of their attention has to be devoted to checking
that the narration and the captions agree with each other. Two notable
exceptions to this are people who do not yet speak the language well and
people with hearing exercises or other special needs, both of whom may
find that the extra effort is a net benefit.

This explains why it's more effective to draw a diagram piece by piece
while teaching rather than to present the whole thing at once. If parts
of the diagram appear at the same time as things are being said, the two
will be correlated in the learner's memory. Pointing at part of the
diagram later is then more likely to trigger recall of what was being
said when that part was being drawn.

The split-attention effect does *not* mean that learners shouldn't try
to reconcile multiple incoming streams of information---after all, this is
something they have to do in the real world [[Atki2000](#CITE)]. Instead,
it means that instruction shouldn't require it while people are
mastering unit skills; instead, using multiple sources of information
simultaneously should be treated as a separate learning task.

> **Not All Graphics Are Created Equal**
> 
> [[Sung2012](#CITE)] presents an elegant study that distinguishes
> *seductive* graphics (which are highly interesting but not directly
> relevant to the instructional goal), *decorative* graphics (which are
> neutral but not directly relevant to the instructional goal), and
> *instructive* graphics (directly relevant to the instructional goal).
> Students who received any kind of graphic gave significantly higher
> satisfaction ratings to material than those who didn't get graphics,
> but only students who got instructive graphics actually performed
> better.
> 
> Similarly, [[Stam2013](#CITE),[Stam2014](#CITE)] found that having more
> information can actually lower performance. They showed children
> pictures, pictures and numbers, or just numbers for two tasks:
> fraction equivalence and fraction addition. For equivalence, having
> pictures or pictures and numbers outperformed having numbers only. For
> addition, however, having pictures outperformed pictures and numbers,
> which outperformed just having numbers.

## Minimal Manuals {#s:load-minimal}

The most extreme use of cognitive load theory may be the "minimal
manual" method introduced in [[Carr1987](#CITE)]. Its starting point is
a quote from a user: "I want to do something, not learn how to do
everything." Carroll and colleagues therefore redesigned training to
present every idea as a single-page self-contained task: a title
describing what the page was about, step-by-step instructions of how to
do something really simple (like how to delete a blank line in a text
editor), and then several notes how to recognize and debug common
problems.

Carroll and colleagues found that rewriting training materials this way
made them shorter overall, and that people using them learned faster.
Later studies like [[Lazo1993](#CITE)] confirmed that this approach
outperformed the traditional approach regardless of prior experience
with computers.

Looking back, [[Carr2014](#CITE)] summarized this work by saying:

> Our "minimalist" designs sought to leverage user initiative and prior
> knowledge, instead of controlling it through warnings and ordered
> steps. It emphasized that users typically bring much expertise and
> insight to this learning, for example, knowledge about the task
> domain, and that such knowledge could be a resource to instructional
> designers. Minimalism leveraged episodes of error recognition,
> diagnosis, and recovery, instead of attempting to merely forestall
> error. It framed troubleshooting and recovery as learning
> opportunities instead of as aberrations.

He goes on to say that at the time, instruction decomposed skills into
sub-skills hierarchically and then drilled people on the sub-skills.
However, this meant context was lost: the goals weren't apparent until
people had learned the pieces. Since people want to dive in and do real
tasks, well-designed instruction should help them do that.

## Exercises {#s:load-exercises}

### Create a Faded Example (pairs/30)

It's very common for programs to count how many things fall into
different categories: for example, how many times different colors
appear in an image, or how many times different words appear in a
paragraph of text.

1. Create a short example (no more than 10 lines of code) that shows
   people how to do this, and then create a second example that solves
   a similar problem in a similar way, but has a couple of blanks for
   learners to fill in. How did you decide what to fade out? What would
   the next example in the series be?

1. Define the audience for your examples. For example, are these
   beginners who only know some basics programming concepts? Or are
   these learners with some experience in programming but not in
   Python?

1. Show your example to a partner, but do *not* tell them what level it
   is intended for. Once they have filled in the blanks, ask them what
   level they think it is for.

If there are people among the trainees who don't program at all, try to
place them in different groups, and have them play the part of learners
for those groups. Alternatively, choose a different problem domain and
develop a faded example for it.

### Classifying Load (small groups/15)

Working in groups of 3--4, choose a short lesson that one of you has
taught or taken recently, make a point-form list of the ideas,
instructions, and explanations it contains, and then classify each as
intrinsic, germane, or extraneous. (The exercise "Noticing Your Blind
Spot" in [s:memory-exercises](#SECTION) will give you an idea of how
detailed your point-form list should be.)

### Create a Parsons Problem (pairs/20)

Write five or six lines of code that does something useful, jumble them,
and ask your partner to put them in order. If you are using an
indentation-based language like Python, do not indent any of the lines;
if you are using a curly-brace language like Java, do not include any of
the curly braces. Again, if your group includes people who aren't
programmers, try using a different problem domain, such as making
guacamole.

### Minimal Manuals (individual/20)

Write a one-page guide to doing something simple that your learners
might encounter in one of your classes, such as centering text
horizontally or printing a number with a certain number of digits after
the decimal points. Try to list at least three or four incorrect
behaviors or outcomes the learner might see, and include a one- or
two-line explanation of why each happens and how to correct it (i.e., go
from symptoms to cause to fix).

### Cognitive Apprenticeship (pairs/15)

Pick a small coding problem (something you can do in two or three
minutes) and think aloud as you work through it while your partner asks
questions about what you're doing and why. As you work, do not just
comment on what you're doing, but also on why you're doing it, how you
know it's the right thing to do, and what alternatives you've considered
but discarded. When you are done, swap roles with your partner and
repeat the exercise.

### Critiquing Graphics (individual/30)

[[Maye2009](#CITE)] presents six principles for designing good diagrams
for teaching. As summarized in [[Mill2016a](#CITE)], they are:

Signalling:
: visually highlight the most important points that you want students
  to retain so that they stand out from less-critical material.

Spatial contiguity:
: if using captions or other text to accompany graphics, place them as
  close to the graphics as practical to offset the cost of shifting
  between the two. If using diagrams or animations, place captions
  right next to relative components instead of putting them in one big
  block of text.

Temporal contiguity:
: present spoken narration and graphics as close in time as
  practical---presenting both at once is better than presenting them
  one after another.

Segmenting:
: when presenting a long sequence of material or when students are
  inexperienced with the subject, break up the presentation into
  shorter segments and let students control how quickly they advance
  from one part to the next.

Pretraining:
: if students don't know the major concepts and terminology used in
  your presentation, set up a module just to teach those concepts and
  terms and make sure they complete that module beforehand.

Modality:
: students learn better from pictures plus audio narration than from
  pictures plus text, unless there are technical words or symbols, or
  the students are non-native speakers.

Choose a video of a lesson or talk online that uses slides or other
static presentations, and rate its graphics as "poor", "average", or
"good" according to these six criteria.

{% include links.md %}
