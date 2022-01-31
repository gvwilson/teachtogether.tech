#!/usr/bin/env python

import re
import sys


def appref(m):
    return f'<a section="{m.group(1)}"/>'
appref.pat = re.compile(r"\\appref\{(.+?)\}")


def chapref(m):
    return f'<a section="{m.group(1)}"/>'
chapref.pat = re.compile(r"\\chapref\{(.+?)\}")


def chapter(m):
    return ""
chapter.pat = re.compile(r"\\chapter\{.+?\}\\label\{.+?\}")


def cite(m):
    return f"<cite>{m.group(1)}</cite>"
cite.pat = re.compile(r"\\cite\{(.+?)\}")


def dotspace(m):
    return ". "
dotspace.pat = re.compile(r"\.\\ ")


def doublequotes(m):
    return f'"{m.group(1)}"'
doublequotes.pat = re.compile(r"``(.+?)''")


def emph(m):
    return f"*{m.group(1)}*"
emph.pat = re.compile(r"\\emph\{(.+?)\}")


def exercise(m):
    return f"### {m.group(1)} ({m.group(2)}/{m.group(3)}) {{.exercise}}"
exercise.pat = re.compile(r"\\exercise\{(.+?)\}\{(.+?)\}\{(.+?)\}")


def figure(m):
    return "\n".join([
        f'<figure id="{m.group(4)}">',
        f'  <img src="{m.group(2)}" alt="{m.group(3)}"/>',
        f'  <figcaption>{m.group(3)}</figcaption>',
        f'</figure>'
    ])
figure.pat = re.compile(r"\\fig(img|pdf|pdfhere)?\{figures/(.+?)\}\{(.+?)\}\{(.+?)\}\{(.*?)\}")


def figref(m):
    return f'<a figure="{m.group(1)}"/>'
figref.pat = re.compile(r"\\figref\{(.+?)\}")


def footnote(m):
    return f"<sub>{m.group(1)}</sub>"
footnote.pat = re.compile(r"\\footnote\{(.+?)\}", re.DOTALL)


def gref(m):
    return f'<span g="{m.group(1)}">{m.group(2)}</span>'
gref.pat = re.compile(r"\\gref\{(.+?)\}\{(.+?)\}", re.DOTALL)


def grefdex(m):
    return f'<span g="{m.group(1)}" i="{m.group(3)}">{m.group(2)}</span>'
grefdex.pat = re.compile(r"\\grefdex\{(.+?)\}\{(.+?)\}\{(.+?)\}", re.DOTALL)


def ldots(m):
    return "…"
ldots.pat = re.compile(r"\{\\ldots\}")


def percent(m):
    return "%"
percent.pat = re.compile(r"\\%")


def pre_end(m):
    return f"```"
pre_end.pat = re.compile(r'\\end\{minted\}')


def pre_start(m):
    return f"```{m.group(1)}"
pre_start.pat = re.compile(r'\\begin\{minted\}\{(.+?)\}')


def seclbl(m):
    return f"## {m.group(1)} {{#{m.group(2)}}}"
seclbl.pat = re.compile(r"\\seclbl\{(.+?)\}\{(.+?)\}")


def secref(m):
    return f'<a section="{m.group(1)}"/>'
secref.pat = re.compile(r"\\secref\{(.+?)\}")


def secstar(m):
    return f"## {m.group(1)}"
secstar.pat = re.compile(r"\\section\*\{(.+?)\}")


def subsec(m):
    return f"### {m.group(1)}"
subsec.pat = re.compile(r"\\subsection\*\{(.+?)\}")


def texttt(m):
    return f"`{m.group(1)}`"
texttt.pat = re.compile(r"\\texttt\{(.+?)\}")


def tilde(m):
    return f" "
tilde.pat = re.compile(r"~")


handlers = (
    # Inner
    dotspace, doublequotes, emph, ldots, percent, texttt,
    # Outer
    appref, chapref, chapter, cite, exercise,
    figref, figure, footnote, gref, grefdex,
    pre_end, pre_start,
    seclbl, secref, secstar, subsec, tilde
)


def main():
    for src in sys.argv[1:]:
        with open(src, "r") as reader:
            text = reader.read()

        for func in handlers:
            text = func.pat.sub(func, text)

        dst = src.replace(".tex", ".md")
        with open(dst, "w") as writer:
            writer.write(text)


if __name__ == "__main__":
    main()
