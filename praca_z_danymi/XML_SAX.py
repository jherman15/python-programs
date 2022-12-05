import xml.sax


class SaxHandler(xml.sax.ContentHandler):

    def __init__(self):
        self.current_data = ""
        self.title = ""
        self.author = ""
        self.price = 0

    def startElement(self, tag, attr):
        self.current_data = tag
        if self.current_data == "book":
            print(f"Book category: {attr['category']}")

    def characters(self, attr):
        if self.current_data == "title":
            self.title = attr
        elif self.current_data == "author":
            self.author = attr
        elif self.current_data == "price":
            self.price = attr

    def endElement(self, attr):
        if self.current_data == "title":
            print(f"Title: {self.title}")
        elif self.current_data == "author":
            print(f"Author: {self.author}")
        elif self.current_data == "price":
            print(f"Price: {self.price}")
        self.current_data = ""


# create an XMLReader
parser = xml.sax.make_parser()

# turn off namepsaces
parser.setFeature(xml.sax.handler.feature_namespaces, 0)

# override the default ContextHandler
sax_handler = SaxHandler()
parser.setContentHandler(sax_handler)
parser.parse("files/xml_file.xml")