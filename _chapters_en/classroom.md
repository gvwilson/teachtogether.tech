---
permalink: "/en/classroom/"
title: "In the Classroom"
objectives:
- Describe how to handle a Code of Conduct violation.
- Explain the benefits and drawbacks of co-teaching.
- Explain why teachers should *not* introduce new pedagogical
  practices in a short workshop.
- Name, describe, and enact four teaching practices that are
  appropriate to use in programming workshops for adults, and give a
  pedagogical justification for each.
---

The previous chapter described how to practice in-class teaching and
described one method---live coding---that allows teachers to adapt to their
learners' pace and interests. This chapter describes other practices
that have proven helpful in programming classes.

Before describing these practices, it's worth pausing for a moment to
set expectations. The best teaching method we know is individual
tutoring: [[Bloo1984](#CITE)] found that students taught one-to-one using
mastery learning techniques performed two standard deviations better
than those who learned through conventional lecture, i.e., that
individually-tutored students did better than 98% of students who were
lectured to. However, hiring one teacher for every student is impossibly
expensive (and despite the hype, artificial intelligence isn't going to
take the place of human instructors any time soon). Every method is
essentially an attempt to get as much of the value of individual
attention as possible, but at scale.

## Enforce the Code of Conduct {#s:classroom-enforce}

[s:intro](#CHAPTER) said that every workshop should have and enforce a
Code of Conduct like the one in [s:conduct](#APPENDIX). If you are a
teacher, and believe that someone has violated it, you may warn them,
ask them to apologize, and/or expel them, depending on the severity of
the violation and whether or not you believe it was intentional.
Whatever you do:

Do it in front of witnesses.
: Most people will tone down their language and hostility in front of
  an audience, and having someone else present ensures that later
  discussion doesn't degenerate into conflicting claims about who said
  what.

If you expel someone, say so to the rest of the class and explain why.
: This helps prevent exaggerated rumors from taking hold, and
  also signals very clearly to everyone that you're serious about
  making your class safe and respectful for them.

Contact the host of your class
: as soon as you can and describe what happened.

A Code of Conduct is meaningless without procedures for reporting
violations and enforcing its rules. However much you don't enjoy doing
the latter, remember that the former can be a much greater burden for
people who have been targets.

## Peer Instruction {#s:classroom-peer}

No matter how good a teacher is, she can only say one thing at a time.
How then can she clear up many different misconceptions in a reasonable
time? The best solution developed so far is a technique called
[peer instruction](#g:peer-instruction). Originally created
by Eric Mazur at Harvard [[Mazu1996](#CITE)], it has been studied
extensively in a wide variety of contexts, including programming
[[Crou2001](#CITE),[Port2013](#CITE)], and [[Port2016](#CITE)] found that students
value peer instruction even at first contact.

Peer instruction is essentially a way to provide one-to-one mentorship
in a scalable way. It interleaves formative assessment with student
discussion as follows:

1. Give a brief introduction to the topic.

1. Give students a multiple choice question that probes for
   misconceptions (rather than simple factual knowledge).

1. Have all the students vote on their answers to the MCQ.

   - If the students all have the right answer, move on.

   - If they all have the same wrong answer, address that specific
     misconception.

   - If they have a mix of right and wrong answers, give them several
     minutes to discuss those answers with one another in small
     groups (typically 2--4 students) and then reconvene and vote
     again.

As [this video from Avanti's learning center in
Kanpur][video-peer-instruction] shows, group discussion significantly
improves students' understanding because it forces them to clarify
their thinking, which can be enough to call out gaps in
reasoning. Re-polling the class then lets the teacher know if they can
move on, or if further explanation is necessary. A final round of
additional explanation and discussion after the correct answer is
presented gives students one more chance to solidify their
understanding.

But could this be a false positive? Are results improving because of
increased understanding during discussion, or simply from a
follow-the-leader effect ("vote like Jane, she's always right")?
[[Smit2009](#CITE)] tested this by following the first question with a
second one that students answer individually. Sure enough, peer
discussion actually does enhance understanding, even when none of the
students in a discussion group originally knew the correct answer.

> **Taking a Stand**
> 
> It is important to have learners vote publicly so that they can't
> change their minds afterward and rationalize it by making excuses to
> themselves like "I just misread the question". Much of the value of
> peer instruction comes from the hypercorrection of having their answer
> be wrong and having to think through the reasons why
> ([s:individual-strategies](#SECTION)).

## Teach Together {#s:classroom-together}

[Co-teaching](#g:co-teaching) describes any situation in
which two teachers work together in the same classroom.
[[Frie2016](#CITE)] describes several ways to do this:

Team teaching:
: Both teachers deliver a single stream of content in tandem, taking
  turns the way that musicians taking solos would.

Teach and assist:
: Teacher A teaches while Teacher B moves around the classroom to help
  struggling students.

Alternative teaching:
: Teacher A provides a small set of students with more intensive or
  specialized instruction while Teacher B delivers a general lesson to
  the main group.

Teach and observe:
: Teacher A teaches while Teacher B observes the students, collecting
  data on their understanding to help plan future lessons.

Parallel teaching:
: The class is divided into two equal groups and the teachers present
  the same material simultaneously to each.

Station teaching:
: The students are divided into several small groups that rotate from
  one station or activity to the next while both teachers supervise
  where needed.

All of these models create more opportunities for lateral knowledge
transfer than teaching alone. Team teaching is particularly beneficial
in day-long workshops: not only does it give each teacher's voice a
chance to rest, it reduces the risk that they will be so tired by the
end of the day that they will start snapping at their students or
fumbling at their keyboard.

> **Helping**
> 
> Many people who aren't comfortable teaching are still willing and able
> to provide in-class technical support. They can help learners with
> setup and installation, answer technical questions during exercises,
> monitor the room to spot people who may need help, or keep an eye on
> the shared notes ([s:classroom-notetaking](#SECTION)) and either
> answer questions there or remind the instructor to do so during
> breaks.
> 
> Helpers are sometimes people training to become teachers (i.e.,
> they're Teacher B in the teach and assist model), but they can also
> be members of the host institution's technical support staff, alumni,
> or advanced learners who already know the material well. Using the
> latter as helpers is doubly effective: not only are they more likely
> to understand the problems their peers are having, it also stops them
> from getting bored.

If you and a partner are co-teaching, try to follow these rules:

- Take 2--3 minutes before the start of each class to confirm who's
  teaching what with your partner. (If you have time to do some
  advance preparation, try drawing a concept map together.)

- Use that time to work out a couple of hand signals as well. "You're
  going too fast", "speak up", "that learner needs help", and, "It's
  time for a bathroom break" are all useful.

- Each person should teach for at least 10--15 minutes at a stretch,
  since students may be distracted by more frequent interleaving.

- The person who *isn't* teaching shouldn't interrupt, offer
  corrections, elaborations, or amusing personal anecdotes, or do
  anything else to distract from what the person teaching at the time
  is doing or saying. The one exception is that it's sometimes helpful
  to ask leading questions, particularly if the learners seem unsure
  of themselves.

- Each person should take a couple of minutes before they start
  teaching to see what their partner is going to teach after they're
  done, and then *not* present any of that material.

- The person who isn't teaching should stay engaged with the class,
  not catch up on their email. Monitor the shared notes
  ([s:classroom-notetaking](#SECTION)), keep an eye on the students
  to see who's struggling, jot down some feedback to give your
  teaching partner at the next break---anything that contributes to the
  lesson is better than anything that doesn't.

Most importantly, take a few minutes when the class is over to either
congratulate or commiserate with each other. In teaching as in life,
shared misery is lessened and shared joy increased: no one will
understand how pleased you are that you helped someone understand loops
better than the person you just taught with.

## Assess Prior Knowledge {#s:classroom-prior}

The more you know about your learners before you start teaching, the
more you will be able to help them. If you're working inside a formal
school system, you can probably infer their incoming knowledge by
looking at what's (actually) covered in the prerequisites to your
course. If you're in a free-range setting, though, your learners may be
much more diverse, so you may want to give them a short survey or
questionnaire in advance of your class to find out what they do and
don't already know.

But doing this is risky. School trains people to treat all assessment as
summative, i.e., to believe that anything that looks like an exam is
something they have to pass, rather than a chance to shape instruction.
If they answer "I don't know" to even a handful of questions on your
preassessment, they might conclude that your class is too advanced for
them. In short, you might scare off many of the people you most want to
help.

And self-assessment is unreliable because of the [Dunning-Kruger
effect][dunning-kruger] [[Krug1999](#CITE)]: the less people know
about a subject, the less accurate their estimate of their knowledge
is. Conversely, people who are competent may underrate their skills
because they regard their level of competence as normal.

Rather than asking people to rate their knowledge from 1 to 5, you
should therefore try to ask them how easily they could complete some
specific tasks, but that still runs the risk of scaring them away.
[s:preassess](#APPENDIX) presents a short preassessment questionnaire
that most potential learners are unlikely to find intimidating; if you
use it or anything like it, please be sure to follow up with people who
*don't* respond to find out why not.

## Plan for Mixed Abilities {#s:classroom-mixed}

If your learners have widely varying levels of prior knowledge, then you
can easily wind up in a situation where a third of your class is lost
and a third is bored. That's unsatisfying for everyone, but there are
some strategies you can use to manage the situation:

- Before running a workshop, communicate its level clearly to everyone
  who's thinking of signing up by listing the topics that will be
  covered and showing a few examples of exercises that they will be
  asked to complete.

- Provide extra self-paced exercises so that more advanced learners
  don't finish early and get bored.

- Ask more advanced learners to help people next to them. They'll
  learn from answering their peers' questions (since it will force
  them to think about things in new ways).

- Keep an eye out for learners who are falling behind and intervene
  early so that they don't become frustrated and give up.

The most important thing is to accept that no single lesson can possibly
meet everyone's individual needs. If you slow down to accommodate two
people who are struggling, the other 38 are not being well served.
Equally, if you spend a few minutes talking about an advanced topic to a
learner who is bored, the rest of the class will feel left out.

> **False Beginners**
> 
> A [false beginner](#g:false-beginner) is someone who has
> studied a language before but is learning it again. False beginners
> may be indistinguishable from
> [absolute beginners](#g:absolute-beginner) on preassessment
> tests, but are able to move much more quickly through the material
> once they start---in mathematical terms, their intercept is the same,
> but their slope is very different. False beginners are common in
> free-range programming classes: for example, a child may have taken a
> Scratch class a couple of years ago and built a mental model of loops
> and conditionals, but do poorly on a pre-test because the material
> isn't fresh in their mind. All of the strategies described above can
> be used in classes with false beginners.
> 
> Being a false beginner is an example of
> [preparatory privilege](#g:preparatory-privilege)
> [[Marg2010](#CITE)]. In many cases, it's a result of coming from a home
> that's secure enough and affluent enough to have several computers and
> parents who are familiar with how to use them. Whether or not this is
> fair depends on what you choose to include in your assessment.

## Pair Programming {#s:classroom-pair}

[Pair programming](#g:pair-programming) is a software development
practice in which two programmers share one computer. One person (the
driver) does the typing, while the other (the navigator) offers
comments and suggestions. The two switch roles several times per hour;
[this video][video-pair-programming] is a quick explanation and
demonstration.

Pair programming is an effective practice in professional work
[[Hann2009](#CITE)], and is also a good way to teach: benefits include
increased success rate in introductory courses, better software, and
higher student confidence in their solutions; there is also evidence
that students from underrepresented groups benefit even more than
others
[[McDo2006](#CITE),[Hank2011](#CITE),[Port2013](#CITE),[Cele2018](#CITE)].
Partners can not only help each other out during the practical, but
can also clarify each other's misconceptions when the solution is
presented, and discuss common research interests during breaks. I have
found it particularly helpful with mixed-ability classes, since pairs
are likely to be more homogeneous than individuals.

When you use pairing, put *everyone* in pairs, not just learners who are
struggling, so that no one feels singled out. It's also useful to have
people sit in new places (and hence pair with different partners) on a
regular basis, and to have people switch roles within each pair three or
four times per hour, so that the stronger personality in each pair
doesn't dominate the session.

To facilitate pairing, use a flat (dinner-style) seating rather than
banked (theater-style) seating; this also makes it easier for helpers to
reach learners who need assistance. And take a few minutes to
demonstrate what it actually looks like so that they understand the
person who doesn't have their hands on the keyboard isn't supposed to
just sit and watch. Finally, tell them about [[Lewi2015](#CITE)], who
studied pair programming in a Grade 6 classroom, and found that pairs
that focused on trying to complete the task as quickly as possible were
less fair in their sharing.

> **Switching Partners**
> 
> Teachers have mixed opinions on whether people should be required to
> change partners at regular intervals. On the one hand, it gives
> everyone a chance to gain new insights and make new friends. On the
> other, moving computers and power adapters to new desks several times
> a day is disruptive, and pairing can be uncomfortable for introverts.
> That said, [[Hann2010](#CITE)] found weak correlation between the "Big
> Five" personality traits and performance in pair programming, although
> an earlier study [[Wall2009](#CITE)] found that pairs whose members had
> differing levels of personality traits communicated more often.

## Take Notes...Together? {#s:classroom-notetaking}

Many studies have shown that taking notes while learning improves
retention [[Aike1975](#CITE),[Boha2011](#CITE)]. Taking notes is essentially a
form of real-time elaboration ([s:individual-strategies](#SECTION)): it
forces you to organize and reflect on material as it's coming in, which
in turn increases the likelihood that you will transfer it to long-term
memory in a usable way.

Our experience, and some recent research findings, lead us to believe
that taking notes *collaboratively* can is also effective,
[[Ornd2015](#CITE),[Yang2015](#CITE)], even though taking notes on a
computer is generally less effective than taking notes using pen and
paper [[Muel2014](#CITE)].

The first time students encounter the practice, they sometimes report
that they find it distracting, as it's one more thing they have to keep
an eye on. Some of the arguments in favor of doing it are:

- It allows people to compare what they think they're hearing with
  what other people are hearing, which helps them fill in gaps and
  correct misconceptions right away.

- It gives the more advanced learners in the class something useful to
  do. Rather than getting bored and checking Twitter during class,
  they can take the lead in recording what's being said, which keeps
  them engaged, and allows less advanced learners to focus more of
  their attention on new material. Keeping the more advanced learners
  busy also helps the whole class stay engaged because boredom is
  infectious: if a handful of people start updating their Facebook
  profiles, the people around them will start checking out too.

- The notes the learners take are usually more helpful *to them* than
  those the teacher would prepare in advance, since the learners are
  more likely to write down what they actually found new, rather than
  what the teacher predicted would be new.

- Glancing at the notes as they're being taken helps the teacher
  discover that the class didn't hear something important, or
  misunderstood it.

We usually use [Etherpad][etherpad] or [Google Docs][google-docs] for
taking shared notes. The former makes it easy to see who's written
what, while the latter scales better and allows people to add images
to the notes. Whichever is chosen, classes also use it to share
snippets of code and small datasets, and as a way for learners to show
teachers their work (by copying and pasting it in).

If you are going to have a group take notes together, make a list of
everyone's name and paste it into the document each time you want every
person to answer a question or contribute an exercise solution. This
prevents the situation in which everyone is trying to edit the same
couple of lines at the same time.

In my experience, the benefits of shared note-taking outweigh the costs.
If you are only working with a particular group once, though, please
heed the advice in [s:classroom-innovate](#SECTION) and stick to
whatever they are used to.

## Sticky Notes {#s:classroom-sticky-notes}

Sticky notes are one of my favorite teaching tools, and judging from
[[Ward2015](#CITE)], I'm not alone in loving their versatility,
portability, stickability, foldability, and subtle yet alluring aroma.

### As Status Flags {#s:classroom-status-flags}

Give each learner two sticky notes of different colors, e.g., orange and
green. These can be held up for voting, but their real use is as status
flags. If someone has completed an exercise and wants it checked, they
put the green sticky note on their laptop; if they run into a problem
and need help, they put up the orange one. This is better than having
people raise their hands because it's more discreet (which means they're
more likely to actually do it), they can keep working while their flag
is raised, and the teacher can quickly see from the front of the room
what state the class is in.

### To Distribute Attention {#s:classroom-attention}

Sticky notes can also be used to ensure the teacher's attention is
fairly distributed. Have each learner write their name on a sticky note
and put it on their laptop. Each time the teacher calls on them or
answers one of their questions, their sticky note comes down. Once all
the sticky notes are down, everyone puts theirs up again.

This technique makes it easy for the teacher to see who they haven't
spoken with recently, which in turn helps them avoid the unconscious
trap of only interacting with the most extroverted of their learners. It
also shows learners that attention is being distributed fairly, so that
when they *are* called on, they won't feel like they're being picked on.

### As Minute Cards {#s:classroom-minute-cards}

You can use sticky notes as [minute cards](#g:minute-cards).
Before each break, learners take a minute to write one positive thing on
the green sticky note (e.g., one thing they've learned that they think
will be useful), and one thing they found too fast, too slow, confusing,
or irrelevant on the red one. They can use the red sticky note for
questions that hasn't yet been answered or something that they're still
confused about. While they are enjoying their coffee or lunch, the
teachers review and cluster these to find patterns. It only takes a few
minutes to see what learners are enjoying, what they still find
confusing, what problems they're having, and what questions are still
unanswered.

## Never a Blank Page {#s:classroom-blank}

Programming workshops (and other kinds of classes) can be built around a
set of independent exercises, develop a single extended example in
stages, or use a mixed strategy. The main advantages of independent
exercises are that people who fall behind can easily re-synchronize, and
that lesson developers can add, remove, and rearrange material at will.
A single extended example, on the other hand, will show learners how the
bits and pieces they're learning fit together: in educational parlance,
it provides more opportunity for them to integrate their knowledge.

Whichever approach you take, novices should never start doing exercises
with a blank page (or screen), since they often find this intimidating
or bewildering. If they have been following along as you do live coding,
you can ask them either to add a few more lines or to modify the example
you have built up. Alternatively, if there is a shared note-taking
space, you can paste in a few lines of starter code for them to extend
or modify.

Modifying existing code instead of writing new code from scratch doesn't
just give learners structure: it is also closer to what they will do in
real life. Keep in mind, however, that starter code may increase
cognitive load, since learners can be distracted by trying to understand
it all before they start their own work. Java's `public static void
main()` or a handful of `import` statements at the top of a Python
program may make sense to you, but is extraneous load to them
([s:load](#CHAPTER)).

## Setting Up Your Learners {#s:classroom-setup}

Adult learners tell us that it is important to them to leave programming
classes with their own computers set up to do real work. We therefore
strongly recommend that teachers be prepared to teach on all three major
platforms (Linux, Mac OS, and Windows), even though it would be simpler
to require learners to use just one.

To do this, put detailed setup instructions for all three platforms on
your class website, and email learners a couple of days before the
workshop starts to remind them to do the setup. Even with this, a few
people will always show up without the right software, either because
their other commitments didn't allow them to go through the setup or
because they ran into problems. To detect this, have everyone run some
simple command as soon as they arrive and show the teachers the result,
and then have helpers and other learners assist people who have run into
trouble.

> **Common Denominators**
> 
> If you have participants using several different operating systems,
> avoid using features which are OS-specific, and point out any that you
> *do* use. For example, some shell commands take different options on
> Mac OS than on Linux, while the "minimize window" controls and
> behavior on Windows are different from those on other platforms.

You can try using tools like [Docker][docker] to put virtual machines
on learners' computers to reduce installation problems, but those
introduce problems of their own. Older or smaller machines simply
aren't fast enough to run them, learners often struggle to switch back
and forth between two different sets of keyboard shortcuts for things
like copying and pasting, and even competent practitioners will become
confused about what exactly is happening where.

All of this is so complicated that many teachers now use browser-based
tools instead. This solves the installation issues, but makes the
class dependent on institutional WiFi (which can be of highly variable
quality). It also doesn't satisfy adult learners' desire to leave with
their own machines ready for real-world use, but as cloud-native
development tools like [Glitch][glitch] enter widespread use, that is
less and less important.

## Other Teaching Practices {#s:classroom-practices}

None of the smaller practices described below are essential, but all
will improve lesson delivery. As with chess and marriage, success in
teaching is often a matter of slow, steady progress.

### Start With Introductions

To begin your class, the teachers should give a brief introduction that
will convey their capacity to teach the material, accessibility and
approachability, desire for student success, and enthusiasm. Tailor your
introduction to the students' skill level so that you convey competence
(without seeming too advanced) and demonstrate that you can relate to
the students. Throughout the workshop, continually demonstrate that you
are interested in student progress and that you are enthusiastic about
the topics.

Students should also introduce themselves (preferably verbally). At the
very least, everyone should add their name to the shared notes, but it's
also good for everyone at a given site to know who all is in the group.
(This can be done while setting up before the start of the class.)

### Set Up Your Own Environment

Setting up your environment is just as important as setting up your
learners', but more involved. As well as having all the software that
they need, and network access to the tool they're using to take notes,
you should also have a glass of water, or a cup of tea or coffee. This
helps keep your throat lubricated, but its real purpose is to give you
an excuse to pause for a couple of seconds and think when someone asks a
hard question or you lose track of what you were going to say next. You
will probably also want some whiteboard pens and a few of the other
things described in the travel kit checklist in [s:events](#APPENDIX).

### Avoid Homework in All-Day Formats

Learners who have spent an entire day programming will be tired. If you
give them homework to do after hours, they'll start the next day tired
as well, so don't do this.

### Don't Touch the Learner's Keyboard

It's often tempting to fix things for learners, but when you do, it can
easily seem like magic (even if you narrate every step). Instead, talk
your learners through whatever they need to do. It will take longer, but
it's more likely to stick.

### Repeat the Question

Whenever someone asks a question in class, repeat it back to them before
answering it to check that you've understood it, and to give people who
might not have heard it a chance to do so. This is particularly
important when presentations are being recorded or broadcast, since your
microphone will usually not pick up what other people are saying.
Repeating questions back also gives you a chance to redirect the
question to something you're more comfortable answering if need
be...

### One Up, One Down

We frequently ask for summary feedback at the end of each day. The
teachers ask the learners to alternately give one positive and one
negative point about the day, without repeating anything that has
already been said. This requirement forces people to say things they
otherwise might not: once all the "safe" feedback has been given,
participants will start saying what they really think.

Minute cards are anonymous; the alternating up-and-down feedback is not.
Each mode has its strengths and weaknesses, and by providing both, we
hope to get the best of both worlds.

### Have Learners Make Predictions

Research has shown that people learn more from demonstrations if they
are asked to predict what's going to happen [[Mill2013](#CITE)]. Doing
this fits naturally into live coding: after adding or changing a few
lines of a program, ask someone what is going to happen when it's run.

### Setting Up Tables

You may not have any control over the layout of the desks or tables in
the room in which your programming workshop takes place, but if you do,
we find it's best to have flat (dinner-style) seating rather than banked
(theater-style) seating, so that you can reach learners who need help
more easily, and so that learners can pair with one another
([s:classroom-mixed](#SECTION)). In-floor power outlets so that you
don't have to run power cords across the floor make life easier as
well as safer, but are still the exception.

Whatever layout you have, try to make sure the seats have good back
support, since people are going to be in them for an extended period,
and check that every seat has an unobstructed view of the screen.

### Cough Drops

If you talk all day to a room full of people, your throat gets raw
because you are irritating the epithelial cells in your larynx and
pharynx. This doesn't just make you hoarse---it also makes you more
vulnerable to infection (which is part of the reason people often come
down with colds after teaching).

The best way to protect yourself against this is to keep your throat
lined, and the best way to do that is to use cough drops early and
often. Good ones will also mask the onset of coffee breath, for which
your learners will probably be grateful.

### Think-Pair-Share

[Think-pair-share](#g:think-pair-share) is a lightweight technique
that helps people refine their ideas and compare them with
others'. Each person starts by thinking individually about a question
or problem and jotting down a few notes. Participants are then paired
to explain their ideas to each another, and possibly to merge them or
select the more interesting ones.  Finally, a few pairs present their
ideas to the whole group.

Think-pair-share works because, to paraphrase Oscar Wilde's Lady
Windermere, people often can't know what they're thinking until they've
heard themselves say it. Pairing gives people new insight into their own
thinking, and forces them to think through and resolve any gaps or
contradictions *before* exposing their ideas to a larger group.

### Morning, Noon, and Night

[[Smar2018](#CITE)] found that if students' classes and other work is
scheduled at times that don't line up with their natural body clocks,
they do less well---i.e., that if a morning person takes night classes or
vice versa, their grades suffer. It's usually not possible to
accommodate this in small groups, but larger ones should try to stagger
start times. This can also help people with childcare responsibilities
and other constraints on their time.

### Humor

Humor should be used sparingly when teaching: most jokes are less funny
when written down, and become even less funny with each re-reading.
Being spontaneously funny while teaching usually works better, but can
easily go wrong: what's a joke to your circle of friends may turn out to
be a serious political issue to your audience. If you do make jokes when
teaching, don't make them at the expense of any group, or of anyone
except possibly yourself.

## Limit Innovation {#s:classroom-innovate}

Each of the techniques presented in this chapter will make your classes
better, but you shouldn't try to adopt them all at once. In fact, it may
be best for your students if you don't use *any* of them, particularly
in situations where you and the students are only together for brief
periods. The reason is that every new practice increases the student's
cognitive load: as well as absorbing what you're trying to teach them
about programming, they're also having to learn a new way to learn. If
you are working with them repeatedly, you can introduce one new
technique every few lessons; if you only have them for a one-day
workshop, it's probably best to be conservative in your approach.

## Exercises {#s:classroom-exercises}

### Create a Questionnaire (individual/20)

Using the questionnaire in [s:preassess](#APPENDIX) as a template,
create a short questionnaire you could give learners before teaching a
class of your own. What do you most want to know about their background?

### One of Your Own (whole class/15)

Think of one teaching practice that hasn't been described so far.
Present your idea to a partner, listen to theirs, and select one to
present to the group as a whole. (This exercise is an example of
think-pair-share.)

### May I Drive? (pairs/10)

Swap computers with a partner (preferably one who uses a different
operating system than you) and work through a simple programming
exercise. How frustrating is it? How much insight does it give you into
what novices have to go through all the time?

### Pairing (pairs/15)

Watch [this video][video-pair-programming] of pair programming, then
practice doing it with a partner. Remember to switch roles between
driver and navigator every few minutes. How long does it take you to
fall into a working rhythm?

### Compare Notes (small groups/15)

From groups of 3--4 people and compare the notes that each person has
taken while reading this material or following along with it in class.
What did you think was noteworthy that your peers missed and vice versa?
What did you understand differently?

### Credibility (individual/15)

[[Fink2013](#CITE)] describes three things that make teachers credible in
their learners' eyes:

Competence:
: knowledge of the subject as shown by the ability to explain complex
  ideas or reference the work of others.

Trustworthiness:
: having the student's best interests in mind. This can be shown by
  giving individualized feedback, offering a rational explanation for
  grading decisions, and treating all students the same.

Dynamism:
: excitement about the subject ([s:performance](#CHAPTER)).

Describe one thing you do when teaching that fits into each category,
and then describe one thing you *don't* do but should for each category
as well.

### Measuring Effectiveness (individual/15)

[[Kirk1994](#CITE)] defines four levels at which to evaluate training:

Reaction:
: how did the learners feel about the training?

Learning:
: how much did they actually learn?

Behavior:
: how much have they changed their behavior as a result?

Results:
: how have those changes in behavior affected their output or the
  output of their group?

What are you doing at each level to evaluate what and how you teach?
What could you do that you're not doing?

### Objections and Counter-Objections (think-pair-share/15)

You have decided not to ask your learners if your class was useful,
because you know that there is no correlation between their answers and
how much they actually learn ([s:pck-now](#SECTION)). Instead, you have
put forward four proposals, each of which your colleagues have shot
down:

See if they recommend the class to friends.
: Why would this be any more meaningful than asking them how they feel
  about the class?

Give them an exam at the end.
: But how much learners know at the end of the day is a poor predictor
  of how much they will remember two or three months later, and any
  kind of final exam will change the feel of the class, because school
  has conditioned learners to believe that exams are always
  high-stakes affairs.

Give them an exam two or three months later.
: But that's practically impossible with free-range learners, and the
  people who didn't get anything out of the workshop are probably less
  likely to take part in follow-up, so feedback gathered this way will
  be skewed.

See if they keep using what they learned.
: Again, since installing spyware on learners' computers is frowned
  upon, how will this be implemented?

Working on your own, come up with answers to these objections, then swap
responses with a partner and discuss the approaches you have come up
with. When you are done, share your best counter-argument with the
entire class.

{% include links.md %}
