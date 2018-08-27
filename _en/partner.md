---
permalink: "/en/partner/"
title: "Partnerships"
objectives:
- Explain why teachers in schools and universities do and don't
  adopt better teaching practices.
- Summarize methods that can be used to effect changes in
  educational institutions.
---

[s:community-learn-then-do](#SECTION) said that the first step in
building a community is to decide if you really need to, or whether you
would be more effective joining an existing organization. Either way,
the organization you're part of will eventually need to work with other,
more established groups: schools, community programs, churches, the
courts, and companies. This chapter presents a handful of strategies for
figuring out how to do that, and when it's worthwhile.

Unlike most of the rest of this book, this chapter is drawn more from
things I have seen than from things I have done. Most of my attempts
to get large institutions to change have been unproductive (which is
part of why I left a university position to re-start [Software
Carpentry][swc] in 2010). While contributions to any part of this book
are welcome, I would be particularly grateful to hear what you have to
say about the issues discussed below.

## Working With Schools {#s:partner-schools}

Everyone is afraid of the unknown and of embarrassing themselves. As a
result, most people would rather fail than change. For example, Lauren
Herckis looked at [why university faculty don't adopt better teaching
methods][faculty-adopt-teaching-methods].  She found that the main
reason is a fear of looking stupid in front of their students;
secondary reasons were concern that the inevitable bumps in changing
teaching methods would affect course evaluations, and a desire to
continue emulating the lecturers who had inspired them. It's pointless
to argue about whether these issues are "real" or not: faculty believe
they are, so any plan to work with faculty needs to address them.

[[Bark2015](#CITE)] did a two-part study of how computer science
educators adopt new teaching practices as individuals, organizationally,
and in society as a whole. They asked and answered three key questions:

1. *How do faculty hear about new teaching practices?* They
   intentionally seek them out because they're motivated to solve a
   problem (particularly student engagement), are made aware through
   deliberate initiatives by their institutions, pick them up from
   colleagues, or get them from expected *and unexpected* interactions
   at conferences (either teaching-related or technical).

1. *Why do they try them out?* Sometimes because of institutional
   incentives (e.g., they innovate to improve their chances of
   promotion), but there is often tension at research institutions
   where rhetoric about the importance of teaching is largely
   disbelieved. Another important reason is their own cost/benefit
   analysis: will the innovation save them time? A third is that they
   are inspired by role models---again, this largely affects innovations
   aimed to improve engagement and motivation rather than learning
   outcomes---and a fourth is trusted sources, e.g., people they meet at
   conferences who are in the same situation that they are and reported
   successful adoption.

   But faculty had concerns, and those concerns were often not
   addressed by people advocating changes. The first was Glass's Law:
   any new tool or practice initially slows you down. Another is that
   the physical layout of classrooms makes many new practices hard:
   discussion groups just don't work in theater-style seating.

   But the most telling result was this: "Despite being researchers
   themselves, the CS faculty we spoke to for the most part did not
   believe that results from educational studies were credible reasons
   to try out teaching practices." This is consistent with other
   findings: even people whose entire careers are devoted to research
   will disregard education research.

1. *Why do they keep using them?* As [[Bark2015](#CITE)] says, "Student
   feedback is critical," and is often the strongest reason to continue
   using a practice, even though we know that students' self-reports
   don't correlate strongly with learning outcomes. (Note that student
   attendance in lectures is seen as an indicator of engagement.)
   Another reason to retaining a practice is institutional
   requirements, although if this is the motivation, people will often
   drop the practice and regress to whatever they were doing before
   when the explicit incentive or monitoring is removed.

The good news is, you can tackle these problems systematically.
[[Baue2015](#CITE)] looked at adoption of new medical
techniques within the US Veterans Administration. They found that
evidence-based practices in medicine take an average of 17 years to be
incorporated into routine general practice, and that only about half
of such practices are ever widely adopted. This depressing finding and
others like it spurred the growth of [implementation
science](#g:implementation-science), which is the
scientific study of ways to get people to actually adopt better
evidence-based practices.

As [s:community](#CHAPTER) said, the starting point is to find out what
the people you're trying to help believe they need. For example,
[[Yada2016](#CITE)] summarizes feedback from K-12 teachers on the
preparation and support they want; while it may not all be applicable to
your setting, having a cup of tea with a few people and listening before
you speak can make a world of difference.

Once you know what people need, the next step is to make changes
incrementally, within institutions' own frameworks. [[Nara2018](#CITE)]
describes an intensive three-year bachelor's program based on tight-knit
cohorts and administrative support that tripled graduation rates.
Elsewhere, [[Hu2017](#CITE)] describes impact of introducing a six-month
certification program for existing high school teachers who want to
teach computing (as opposed to the older two-year/five-course program).
The number of computing teachers had been stable from 2007 to 2013, but
quadrupled after introduction of the new certification program, without
diluting quality: new-to-computing teachers seemed to be as effective as
teachers with more computing training at teaching the introductory
Exploring Computer Science course. The authors report, "How much CS
content students self-reported learning in ECS appears to be based on
how much they believed they knew before taking ECS, and appears to have
no correlation to their teacher's CS background."

More broadly, [[Borr2014](#CITE)] categorizes ways to make change happen
in higher education. The categories are defined by whether the change is
individual or to the system as a whole, and whether it is prescribed
(top-down) or emergent (bottom-up). The person trying to make the
changes---and make them stick---has a different role in each situation, and
should pursue different strategies accordingly.

The paper goes on to explain each of the methods in detail, while
[[Hend2015a](#CITE),[Hend2015b](#CITE)] present the same ideas in more actionable
form. Coming in from outside, you will probably fall into the
Individual/Emergent category to start with, since you will be
approaching teachers one by one and trying to make change happen
bottom-up. If this is the case, the strategies Borrego and Henderson
recommend center around having teachers reflect on their teaching
individually or in groups. Since they may know more about teaching than
you do, this often comes down to doing live coding sessions with them so
that they know how to program themselves, and to demonstrate whatever
curriculum you may already have.

## Working Outside Schools {#s:partner-outside}

Schools and universities aren't the only places people go to learn
programming; over the past few years, a growing number have turned to
intensive bootcamp programs. These are typically one to six months long,
run by private firms for profit, and target people who are retraining to
get into tech. Some are very high quality, but others exist primarily to
separate people (often from low-income backgrounds) from their money
[[McMi2017](#CITE)].

[[Thay2017](#CITE)] interviewed 26 alumni of such bootcamps that provide
a second chance for those who missed computing education opportunities
earlier (though the authors phrasing this as "missed earlier
opportunities" makes some pretty big assumptions when it comes to people
from underrepresented groups). Bootcamp students face great personal
costs and risks: significant time, money, and effort spent before,
during, and after bootcamps, and career change could take students a
year or more. Several interviewees felt that their certificates were
looked down on by employers; as some said, getting a job means passing
an interview, but interviewers often won't share their reasons for
rejection, so it's hard to know what to fix or what else to learn. Many
resorted to internships (paid or otherwise) and spent a lot of time
building their portfolios and networking. The three informal barriers
they most clearly identified were knowledge (or rather, jargon),
impostor syndrome, and a sense of not fitting in.

[[Burk2018](#CITE)] dug into this a bit deeper by comparing the skills
and credentials that tech industry recruiters are looking for to those
provided by 4-year degrees and bootcamps. They interviewed 15 hiring
managers from firms of various sizes and ran some focus groups, and
found that recruiters uniformly emphasized soft skills (especially
teamwork, communication, and the ability to continue learning). Many
companies required a 4-year degree (though not necessarily in computer
science), but many also praised bootcamp graduates for being older or
more mature and having more up-to-date knowledge.

If you are approaching one of these groups, your best strategy could
well be to emphasize what you know about teaching rather than what you
know about tech, since many of their founders and staff have programming
backgrounds but little or no training in education. The first few
chapters of this book have played well with this audience in the past,
and [[Lang2016](#CITE)] describes evidence-based teaching practices that
can be put in place with minimal effort and at low cost. These may not
have the most impact, but scoring a few early wins helps build support
for larger and riskier efforts.

## Final Thoughts {#s:partner-final}

It is impossible to change large institutions on your own: you need
allies, and to get allies, you need tactics. The most useful guide I
have found is [[Mann2015](#CITE)], which catalogs more than four dozen
methods you can use, and organizes them according to whether they're
best deployed early on, later, throughout the change cycle, or when you
encounter resistance. A handful of their patterns include:

Small Successes:
: To avoid becoming overwhelmed by the exercises and all the things
  you have to do when you're involved in an organizational change
  effort, celebrate even small successes.

In Your Space:
: Keep the new idea visible by placing reminders throughout the
  organization.

Token:
: To keep a new idea alive in a person's memory, hand out tokens that
  can be identified with the topic being introduced.

Champion Skeptic:
: Ask strong opinion leaders who are skeptical of your new idea to
  play the role of "official skeptic". Use their comments to improve
  your effort, even if you don't change their minds.

Conversely, [[Farm2006](#CITE)] has ten tongue-in-cheek rules for
ensuring that a new tool isn't adopted, all of which apply to new
teaching practices as well:

1. Make it optional.

1. Economize on training.

1. Don't use it in a real project.

1. Never integrate it.

1. Use it sporadically.

1. Make it part of a quality initiative.

1. Marginalize the champion.

1. Capitalize on early missteps.

1. Make a small investment.

1. Exploit fear, uncertainty, doubt, laziness, and inertia.

The most important strategy is to be willing to change your goals based
on what you learn from the people you are trying to help. It could well
be that tutorials showing them how to use a spreadsheet will help them
more quickly and more reliably than an introduction to JavaScript. I
have often made the mistake of confusing things I was passionate about
with things that other people ought to know; if you truly want to be a
partner, always remember that learning and change have to go both ways.

## Exercises {#s:partner-exercises}

### Collaborations (small groups/30)

Answer the following questions on your own, and then compare your
answers to those given by other members of your group.

1. Do you have any agreements or relationships with other groups?

1. Do you want to have relationships with any other groups?

1. How would having (or not having) collaborations help you to achieve
   your goals?

1. What are your key collaborative relationships?

1. Are these the right collaborators for achieving your goals?

1. With what groups or entities would you like your organization to
   have agreements or relationships?

### Educationalization (whole class/10)

[[Laba2008](#CITE)] explores why the United States and other countries
keep pushing the solution of social problems onto educational
institutions, and why that continues not to work. As he points out,
"[Education] has done very little to promote equality of race,
class, and gender; to enhance public health, economic productivity, and
good citizenship; or to reduce teenage sex, traffic deaths, obesity, and
environmental destruction. In fact, in many ways it has had a negative
effect on these problems by draining money and energy away from social
reforms that might have had a more substantial impact." He goes on to
write:

> So how are we to understand the success of this institution in light
> of its failure to do what we asked of it? One way of thinking about
> this is that education may not be doing what we ask, but it is doing
> what we want. We want an institution that will pursue our social goals
> in a way that is in line with the individualism at the heart of the
> liberal ideal, aiming to solve social problems by seeking to change
> the hearts, minds, and capacities of individual students. Another way
> of putting this is that we want an institution through which we can
> express our social goals without violating the principle of individual
> choice that lies at the center of the social structure, even if this
> comes at the cost of failing to achieve these goals. So education can
> serve as a point of civic pride, a showplace for our ideals, and a
> medium for engaging in uplifting but ultimately inconsequential
> disputes about alternative visions of the good life. At the same time,
> it can also serve as a convenient whipping boy that we can blame for
> its failure to achieve our highest aspirations for ourselves as a
> society.

How do efforts to teach computational thinking and digital citizenship
in schools fit into this framework?

### Institutional Adoption (whole class/15)

Re-read the list of motivations to adopt new practices given in
[s:partner-schools](#SECTION). Which of these apply to you and your
colleagues? Which are irrelevant to your context? Which do you emphasize
if and when you interact with people working in formal educational
institutions?

### Making It Fail (small groups/15)

Working in small groups, re-read the list of ways to ensure new tools
aren't adopted given in [s:partner-final](#SECTION). Which of these
have you seen done recently? Which have you done yourself? What form did
they take?

### Mentoring (whole class/15)

The Institute for African-American Mentoring in Computer Science has
published a brief set of guidelines for mentoring doctoral students,
which you can download from <http://iaamcs.org/guidelines>. Take a few
minutes to read the guidelines individually, and then go through them as
a class and rate your efforts for your own group as +1 (definitely
doing), -1 (definitely not doing), and 0 (not sure or not applicable).

{% include links.md %}
