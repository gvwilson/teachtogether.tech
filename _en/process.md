---
permalink: "/en/process/"
title: "A Lesson Design Process"
objectives:
- Describe the steps in backward lesson design and explain why it
  generally produces better lessons than the more common forward
  development process.
- Define "teaching to the test" and explain why backward lesson
  design is *not* the same thing.
- Construct and critique five-part learner personas.
- Construct good learning objectives and critique learning
  objectives with reference to Bloom's Taxonomy and/or Fink's
  Taxonomy.
---

Most people design lessons like this:

1. Someone asks you to teach something you haven't thought about in
   years.

1. You start writing slides to explain what you know about the subject.

1. After two or three weeks, you make up an assignment based more or
   less on what you've taught so far.

1. You repeat step 3 several times.

1. You stay awake into the wee hours of the morning to create a final
   exam and promise yourself that you'll be more organized next time.

There's a better way, but to explain it, we first need to explain how
[test-driven development](#g:test-driven-development) (TDD)
is used in software development. Programmers who are using TDD don't
write software and then write tests to check that the software is
doing the right thing. Instead, they write the tests first, then write
just enough new software to make those tests pass, and then clean up a
bit.

TDD works because writing tests forces programmers to specify exactly
what they're trying to accomplish and what "done" looks like. It's
easy to be vague when using a human language like English or Korean;
it's much harder to be vague in Python or R. TDD also reduces the risk
of endless polishing, and the risk of confirmation bias: someone who
hasn't written a program is much more likely to be objective when
testing it than its original author, and someone who hasn't written a
program *yet* is more likely to test it objectively than someone who
has just put in several hours of hard work and really, really wants to
be done.

A similar backward method works very well for lesson design. This
method is something called [backward design](#g:backward-design);
developed independently in
[[Wigg2005](#CITE),[Bigg2011](#CITE),[Fink2013](#CITE)], it is
summarized in [[McTi2013](#CITE)], and in simplified form, its steps
are:

1. Brainstorm to get a rough idea of what you want to cover, how
   you're going to do it, what problems or misconceptions you expect
   to encounter, what's *not* going to be included, and so on. You may
   also want to draw some concept maps at this stage.

1. Create or recycle learner personas (discussed in the next section)
   to figure out who you are trying to teach and what will appeal to
   them. (This step can also be done first, before the brainstorming.)

1. Create formative assessments that will give the learners a chance
   to practice the things they're trying to learn and tell you and
   them whether they're making progress and where they need to focus
   their work.

1. Put the formative assessments in order based on their complexity
   and dependencies to create a course outline.

1. Write just enough to get learners from one formative assessment to
   the next. Each hour in the classroom will then consist of three or
   four such episodes.

This method helps to keep teaching focused on its objectives. It also
ensures that learners don't face anything on the final exam that the
course hasn't prepared them for. It is *not* the same thing as
"teaching to the test". When using backward design, teachers set goals
to aid in lesson design, and may never actually give the final exam
that they wrote. In many school systems, on the other hand, an
external authority defines assessment criteria for all learners,
regardless of their individual situations. The outcomes of those
summative assessments directly affect the teachers' pay and promotion,
which means teachers have an incentive to focus on having learners
pass test rather than on helping them learn.

> **Measure...And Then?**
> 
> [[Gree2014](#CITE)] argues that this focus on measurement is
> appealing to those with the power to set the tests, but unlikely to
> improve outcomes unless it is coupled with support for teachers to
> make improvements based on test outcomes. The latter is often
> missing because large organizations usually value uniformity over
> productivity [[Scot1998](#CITE)]; we will return to this topic in
> [s:performance](#CHAPTER).

It's important to note that while lesson design is *described* as a
sequence, it's almost never *done* that way: we may, for example,
change our mind about what we want to teach based on something that
occurs to us while we're writing an MCQ, or re-assess who we're trying
to help once we have a lesson outline. However, it's important that
the notes we leave behind present things in the order described above,
because that's the easier way for whoever has to use or maintain the
lesson to retrace our thinking. The same rewriting of history is
useful for the same reasons in software design and many other fields
[[Parn1986](#CITE)].

[s:v3](#APPENDIX) presents the design notes for this version of this
book. A few things have been added, dropped, or rearranged, but what
you are reading now matches the plan pretty closely.

## Learner Personas {#s:process-personas}

A key step in the lesson design process described above is figuring
out who your audience is. One way to do this is to write two or three
[learner personas](#g:learner-persona). This technique is
borrowed from user interface designers, who create short profiles of
typical users to help them think about their audience.

Learner personas have five parts:

1.  the person's general background,
2.  what they already know,
3.  what *they* think they want to do (as opposed to what someone who already
    understands the subject thinks),
4.  how the course will help them, and
5.  any special needs they might have.

The personas in [s:intro-audience](#SECTION) have the five points listed above,
rearranged to flow more readably; a learner persona for a weekend workshop aimed
at college students might be:

1. Jorge has just moved from Costa Rica to Canada to study
   agricultural engineering. He has joined the college soccer team,
   and is looking forward to learning how to play ice hockey.

1. Other than using Excel, Word, and the Internet, Jorge's most
   significant previous experience with computers is helping his
   sister build a WordPress site for the family business back home in
   Costa Rica.

1. Jorge needs to measure properties of soil from nearby farms using a
   handheld device that sends logs in a text format to his computer.
   Right now, Jorge has to open each file in Excel, crop the first and
   last points, and calculate an average.

1. This workshop will show Jorge how to write a little Python program
   to read the data, select the right values from each file, and
   calculate the required statistics.

1. Jorge can read English well, but still struggles sometimes to keep
   up with spoken conversation (especially if it involves a lot of new
   jargon).

> **A Gentle Reminder**
> 
> When designing lessons, you must always remember that *you are not
> your learners*. You may be younger (if you're teaching seniors) or
> wealthier (and therefore able to afford to download videos without
> foregoing a meal to pay for the bandwidth), but you are almost
> certainly more knowledgeable about technology. Don't assume that you
> know what they need or will understand: ask them, and pay attention
> to their answer. After all, it's only fair that learning should go
> both ways.

Rather than writing new personas for every lesson or course, it's
common for teachers to create and share a handful that cover everyone
they are likely to teach, then pick a few from that set to describe
who particular material is intended for. When personas are used this
way, they become a convenient shorthand for design issues: when
speaking with each other, teachers can say, "Would Jorge understand
why we're doing this?" or, "What installation problems would Jorge
face?"

Brainstorming the broad outlines of what you're going to teach and
then deciding who you're trying to help is one approach; it's equally
valid to pick an audience and then brainstorm their needs. Either way,
[[Guzd2016](#CITE)] offers the following guidance:

1. Connect to what learners know.

1. Keep cognitive load low.

1. Use authentic tasks (see [s:motivation-authentic](#SECTION)).

1. Be generative and productive.

1. Test your ideas rather than trusting your instincts.

Of course, one size won't fit all. [[Alha2018](#CITE)] reported
improvement in learning outcomes and student satisfaction in a course
for students from a variety of academic backgrounds which allowed them
to choose between different domain-related assignments. It's extra
work to set up and grade, but that's manageable if the projects are
open-ended (so that they can be used repeatedly) and if the load is
shared with other teachers ([s:process-maintainability](#SECTION)).
Other work has shown that building courses for science students around
topics as diverse as music, data science, and cell biology will also
improve outcomes
[[Pete2017](#CITE),[Dahl2018](#CITE),[Ritz2018](#CITE)].

## Learning Objectives {#s:process-objectives}

Formative and summative assessments help teachers figure out what
they're going to teach, but in order to communicate that to learners
and other teachers, a course description should also have [learning
objectives](#g:learning-objective). These help ensure that
everyone has the same understanding of what a lesson is supposed to
accomplish. For example, a statement like "understand Git" could mean
any of the following, each of which would be backed by a very
different lesson:

- Learners can describe three scenarios in which version control
  systems like Git are better than file-sharing tools like Dropbox,
  and two in which they are worse.

- Learners can commit a changed file to a Git repository using a
  desktop GUI tool.

- Learners can explain what a detached HEAD is and recover from it
  using command-line operations.

> **Objectives vs. Outcomes**
> 
> A learning objective is what a lesson strives to achieve. A
> [learning outcome](#g:learning-outcome) is what it actually
> achieves, i.e., what learners actually take away. The role of
> summative assessment is therefore to compare learning outcomes with
> learning objectives.

A learning objective is a single sentence describing how a learner
will demonstrate what they have learned once they have successfully
completed a lesson. More specifically, it has a *measurable or
verifiable verb* that states what the learner will do, and specifies
the *criteria for acceptable performance*. Writing these kinds of
learning objectives may initially seem restrictive or limiting, but
will make you, your fellow teachers, and your learners happier in the
long run. You will end up with clear guidelines for both your teaching
and assessment, and your learners will appreciate the clear
expectations.

One way to understand what makes for a good learning objective is to
see how a poor one can be improved:

- "The learner will be given opportunities to learn good programming
  practices." This describes the lesson's content, not the attributes
  of successful students.

- "The learner will have a better appreciation for good programming
  practices." This doesn't start with an active verb or define the
  level of learning, and the subject of learning has no context and is
  not specific.

- "The learner will understand how to program in R." While this starts
  with an active verb, it doesn't define the level of learning, and
  the subject of learning is still too vague for assessment.

- "The learner will write one-page data analysis scripts to read,
  filter, summarize, and print results for tabular data using R and
  RStudio." This starts with an active verb, defines the level of
  learning, and provides context to ensure that outcomes can be
  assessed.

When it comes to choosing verbs, many teachers use [Bloom's
taxonomy](#g:blooms-taxonomy). First published in 1956, it
was updated at the turn of the century [[Ande2001](#CITE)], and is the
most widely used framework for discussing levels of understanding. Its
most recent form has six categories; the list below defines each, and
gives a few of the verbs typically used in learning objectives written
for each:

Remembering:
: Exhibit memory of previously learned material by recalling facts,
  terms, basic concepts, and answers. *(recognize, list, describe,
  name, find)*

Understanding:
: Demonstrate understanding of facts and ideas by organizing,
  comparing, translating, interpreting, giving descriptions, and
  stating main ideas. *(interpret, summarize, paraphrase, classify,
  explain)*

Applying:
: Solve new problems by applying acquired knowledge, facts, techniques
  and rules in a different way. *(build, identify, use, plan, select)*

Analyzing:
: Examine and break information into parts by identifying motives or
  causes. Make inferences and find evidence to support
  generalizations. *(compare, contrast, simplify)*

Evaluating:
: Present and defend opinions by making judgments about information,
  validity of ideas, or quality of work based on a set of criteria.
  *(check, choose, critique, prove, rate)*

Creating:
: Compile information together in a different way by combining
  elements in a new pattern or proposing alternative solutions.
  *(design, construct, improve, adapt, maximize, solve)*

[[Masa2018](#CITE)] found that even experienced educators have trouble
agreeing on how to classify a question or idea according to Bloom's
Taxonomy, but the material in most introductory programming courses
fits into the first four of these levels; only once that material has
been mastered can learners start to think about evaluating and
creating. (As Daniel Willingham has said, people can't think without
something to think about [[Will2010](#CITE)].)

Another way to think about learning objectives comes from
[[Fink2013](#CITE)], which defines learning in terms of the change it
is meant to produce in the learner. [Fink's
Taxonomy](#g:finks-taxonomy)also has six categories, but unlike
Bloom's, they are complementary rather than hierarchical:

Foundational Knowledge:
: understanding and remembering information and ideas. *(remember,
  understand, identify)*

Application:
: skills, critical thinking, managing projects. *(use, solve,
  calculate, create)*

Integration:
: connecting ideas, learning experiences, and real life. *(connect,
  relate, compare)*

Human Dimension:
: learning about oneself and others. *(come to see themselves as,
  understand others in terms of, decide to become)*

Caring:
: developing new feelings, interests, and values. *(get excited about,
  be ready to, value)*

Learning How to Learn:
: becoming a better student. *(identify source of information for,
  frame useful questions about)*

A set of learning objectives based on this taxonomy for an
introductory course on HTML and CSS might be:

> By the end of this course, learners will be able to:
>
> - Explain the difference between markup and presentation, what CSS
>   properties are, and how CSS selectors work.
>
> - Write and style a web page using common tags and CSS properties.
>
> - Compare and contrast authoring with HTML and CSS to authoring with
>   desktop publishing tools.
>
> - Identify issues in sample web pages that would make them difficult
>   for the visually impaired to interact with and provide appropriate
>   corrections.
>
> - Explain the role that JavaScript plays in styling web pages and
>   want to learn more about how to use it.

## Maintainability {#s:process-maintainability}

It takes a lot of effort to create a good lesson, but once it has been
built, someone needs to maintain it, and doing that is a lot easier if
it has been built in a maintainable way. But what exactly does
"maintainable" mean? The short answer is that a lesson is maintainable
if it's cheaper to update it than to replace it. This equation depends
on three factors. The first is *how well documented the course's
design is.* If the person doing maintenance doesn't know (or doesn't
remember) what the lesson is supposed to accomplish or why topics are
introduced in a particular order, it will take her more time to update
it. One of the reasons to use the design process described earlier in
this chapter is to capture decisions about why each course is the way
it is.

The second factor is *how easy it is for collaborators to collaborate
technically.* Teachers usually share material by mailing PowerPoint
files to each other or putting them in a shared drive. Collaborative
writing tools like [Google Docs][google-docs] and wikis are
a big improvement, as they allow many people to update the same
document and comment on other people's updates. The version control
systems used by programmers, such as [GitHub][github], are
another big advance, since they let any number of people work
independently and then merge their changes back together in a
controlled, reviewable way.  Unfortunately, version control systems
have a long, steep learning curve, and (still) don't handle common
office document formats.

The third factor, which is the most important in practice, is *how
willing people are to collaborate.* The tools needed to build a
"Wikipedia for lessons" have been around for twenty years, but most
teachers still don't write and share lessons the way that they write
and share encyclopedia entries, even though commons-based lesson
development and maintenance actually works very well
([s:community-governance](#SECTION) and
[s:joining-contributing](#SECTION)).

[[Leak2017](#CITE)] interviewed 17 computer science teachers to find
out why they don't use resource sharing sites. They found that most of
the reasons were operational. For example, respondents said that sites
need good landing pages that ask "what is your current role?" and
"what course and grade level are you interested in?", and should
display all their resources in context, since visitors may be new
teachers who are struggling to connect the dots themselves. They also
said that sites should allow anonymous posts on discussion forums to
reduce fear of looking foolish in front of peers.

One interesting observation is that while teachers don't collaborate
at scale, they *do* remix by finding other people's materials online
or in textbooks and reworking them. That suggests that the root
problem may be a flawed analogy: rather than lesson development being
like writing a Wikipedia article or some open source software, perhaps
it's more like sampling in music.

If this is true, then lessons may be the wrong granularity for
sharing, and collaboration might be more likely to take hold if the
thing being collaborated on was smaller. This fits well with
Caulfield's theory of [choral explanations][choral-explanations]. He
argues that sites like [Stack Overflow][stack-overflow] succeed
because they provide a chorus of answers for every question, each of
which is most suitable for a slightly different questioner. If
Caulfield is right, the lessons of tomorrow may include guided tours
of community-curated Q&A repositories designed to accommodate learners
at widely different levels.

## Exercises {#s:process-exercises}

### Create Learner Personas (small groups/30)

Working in small groups, create a five-point persona that describes one
of your typical learners.

### Classify Learning Objectives (pairs/10)

Look at the example learning objectives given for an introductory course
on HTML and CSS in [s:process-objectives](#SECTION) and classify each
according to Bloom's Taxonomy. Compare your answers with those of your
partner: where did you agree and disagree, and why?

### Write Learning Objectives (pairs/20)

Write one or more learning objectives for something you currently teach
or plan to teach using Bloom's Taxonomy. Working with a partner,
critique and improve the objectives.

### Write More Learning Objectives (pairs/20)

Write one or more learning objectives for something you currently teach
or plan to teach using Fink's Taxonomy. Working with a partner, critique
and improve the objectives.

### Building Lessons by Subtracting Complexity (individual/20)

One way to build a programming lesson is to write the program you want
learners to finish with, then remove the most complex part that you want
them to write and make it the last exercise. You can then remove the
next most complex part you want them to write and make it the
penultimate exercise, and so on. Anything that's left---i.e., anything you
don't want them to write as an exercise---becomes the starter code that
you give them. This typically includes things like importing libraries
and loading data.

Take a program or web page that you want your learners to be able to
create on their own at the end of a lesson and work backward to break it
into digestible parts. How many are there? What key idea is introduced
by each one?

### Inessential Weirdness (individual/15)

Betsy Leondar-Wright coined the phrase "[inessential
weirdness][inessential-weirdness]" to describe things groups do that
aren't really necessary, but which alienate people who aren't members
of that group. Sumana Harihareswara later used this notion as the
basis for a talk on [inessential weirdnesses in open source
software][inessential-weirdness-open-source], which includes things
like making disparaging comments about Microsoft Windows, command-line
tools with cryptic names, and the command line itself. Take a few
minutes to read these articles, then make a list of inessential
weirdnesses you think your learners might encounter when you first
teach them. How many of these can you avoid with a little effort?

### PRIMM (individual/15)

One approach to introducing new ideas in computing is [PRIMM][primm]:
**P**redict a program's behavior or output, **R**un it to see what it
actually does, **I**nvestigate why it does that (e.g., by stepping
through it in a debugger or drawing the flow of control), **M**odify
it (or its inputs), and then **M**ake something similar from scratch.
Pick something you have recently taught or been taught and outline a
short lesson that follows these five steps.

### Evaluating Lessons (pairs/20)

[[Mart2017](#CITE)] specifies eight dimensions along which lessons can be
evaluated:

Closed vs. open:
: is there a well-defined path and endpoint, or are learners
  exploring?

Cultural relevance:
: how well is the task connected to things they do outside class?

Recognition:
: how easily can the learner share the product of their work?

Space to play:
: seems to overlap closed vs. open

Driver shift:
: how often are learners in control of the learning experience (tight
  cycles of "see then do" score highly)

Risk reward:
: to what extent is taking risks rewarded or recognized?

Grouping:
: is learning individual, in pairs, or in larger groups?

Session shape:
: theater-style classroom, dinner seating, free space, public space,
  etc.

Working with a partner, go through a set of lessons you have recently
taught, or have recently been taught, and rate them as "low", "medium",
"high", or "not applicable" on each of these criteria. Which two
criteria are most important to you personally as a teacher? As a
learner?

### Concrete-Representational-Abstract (pairs/15)

[Concrete-Representational-Abstract][cra] (CRA) is another approach to
introducing new ideas that is used primarily with younger
learners. The first step is the concrete stage, and involves
physically manipulating objects to solve a problem (e.g., piling
blocks to do addition). In the representational stage, images are
used to represent those objects, and in the final abstract stage, the
learner uses numbers or symbols.

1. Write each of the numbers 2, 7, 5, 10, 6 on a sticky note.

1. Simulate a loop that finds the largest value by looking at each in
   turn (concrete).

1. Sketch a diagram of the process you used, labelling each step
   (representational).

1. Write instructions that someone else could follow to go through the
   same steps you used (abstract).

1. Compare your representational and abstract materials with those of
   your partner.

{% include links.md %}
