import os

def create_aiff(s, title):
    with open(title + ".txt","w") as f:
        f.write(s);
    f.close()
    os.system("say -f " + title + ".txt -o " + title)

def html_mathjax(dir):
    return "<script src='./"+dir+"/MathJax.js?config=TeX-AMS-MML_HTMLorMML' type='text/javascript'></script>"

def html_include_audio(path):
    return "<audio controls> <source src=" + path + ".aiff> </audio>"


source_mkd = "phd_slides"
include = ["Title","Pietro FODRA (University of Paris 7)","Phd Advisor : Huyen Pham"]
mathjax_dir = "MathJax"
html = True
pdf = False

if __name__ == "__main__":
    
    with open(source_mkd + ".mkd", "r") as f:
        file = f.read().splitlines()
    f.close()
    i = 0
    slides = ""
    for inc in include:
		slides += "%" + inc + "\n"
    slides += "\n" + html_mathjax(mathjax_dir) + "\n\n"
    for line in file:
        if line.startswith("> "):
            audio_path = "audio_"+str(i)
            create_aiff(line[2:len(line)-1], audio_path)
            line = html_include_audio(audio_path)
            i += 1
        slides += line + "\n"

    with_narration = source_mkd+"_with_narration"    
    with open(with_narration+".mkd","w") as f:
        f.write(slides)
    f.close()

    if html:
        os.system("pandoc -s -i -t dzslides "+with_narration+".mkd -o index.html")
    if pdf:
        os.system("pandoc -s -i -t beamer "+with_narration+".mkd -o "+with_narration+".pdf")

    os.system("open -a Safari "+with_narration+".html")















