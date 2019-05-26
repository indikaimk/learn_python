import xml.dom.minidom as minidom

def main():
  doc = minidom.parse("samplexml.xml")
  print(doc.nodeName)
  print(doc.firstChild.tagName)

  skills = doc.getElementsByTagName("skill")
  print("%d skills" % skills.length)
  for skill in skills:
    print(skill.getAttribute("name"))

  newSkill = doc.createElement("skill")
  newSkill.setAttribute("name", "Flutter")
  doc.firstChild.appendChild(newSkill)
  skills = doc.getElementsByTagName("skill")
  print("%d skills" % skills.length)
  for skill in skills:
    print(skill.getAttribute("name"))


if __name__ == "__main__":
  main()