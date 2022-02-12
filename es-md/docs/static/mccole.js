// Defaults.
DEFAULT_LANG = "en"
TERMS = {
  "footnotes": {
    "en": "Footnotes",
    "es": "Notas al pie"
  }
}

// Move footnote text to the bottom of the page.
const fixFootnotes = (lang) => {
  const list = document.createElement('ol')
  list.classList.add('footnotes')
  Array.from(document.querySelectorAll('sup')).forEach((sup, i) => {
    backref = `backref.${i+1}`
    footnote = `footnote.${i+1}`
    const text = sup.innerHTML
    sup.id = backref
    sup.innerHTML = `<a href="#${footnote}">${i+1}</a>`
    const item = document.createElement('li')
    item.id = footnote
    item.innerHTML = `${text} <a href="#${backref}">&#x21F1;</a>`
    list.appendChild(item)
  })
  if (list.children.length > 0) {
    main = document.querySelector('main')
    heading = document.createElement('h2')
    heading.textContent = TERMS["footnotes"][lang]
    main.appendChild(heading)
    main.appendChild(list)
  }
}

// Find the document language.
const getLang = () => {
  node = document.querySelector('html')
  return node.getAttribute("lang") || DEFAULT_LANG
}

// Do all fixes.
const fixPage = () => {
  lang = getLang()
  fixFootnotes(lang)
}
