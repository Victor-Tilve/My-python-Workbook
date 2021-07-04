import xml.dom.minidom


dom = xml.dom.minidom.parse('config2.xml')


def handleSlideshow(slideshow):
    print("<html>")
    handleSlideshowTitle(slideshow.getElementsByTagName("title")[0])
    slides = slideshow.getElementsByTagName("slide")
    handleToc(slides)
    handleSlides(slides)
    print("</html>")

def handleSlideshowTitle(title):
    print("<title>%s</title>" % getText(title.childNodes))


def handleToc(slides):
    for slide in slides:
        title = slide.getElementsByTagName("title")[0]
        print("<p>%s</p>" % getText(title.childNodes))

def handleSlides(slides):
    for slide in slides:
        handleSlide(slide)


def handleSlide(slide):
    handleSlideTitle(slide.getElementsByTagName("title")[0])
    handlePoints(slide.getElementsByTagName("point"))

def handleSlideTitle(title):
    print("<h2>%s</h2>" % getText(title.childNodes))

def handlePoints(points):
    print("<ul>")
    for point in points:
        handlePoint(point)
    print("</ul>")

def handlePoint(point):
    print("<li>%s</li>" % getText(point.childNodes))

def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)





if __name__ == '__main__':
    # handleSlideshow(dom)
    # print(getText(dom.getElementsByTagName("title")[0].childNodes))
    slides = dom.getElementsByTagName("slide")
    for slide in slides:
        title = slide.getElementsByTagName("title")[0]
        print("%s" % getText(title.childNodes))
    
    print(getText(dom.getElementsByTagName("slide")[0].getElementsByTagName("title")[0].childNodes))