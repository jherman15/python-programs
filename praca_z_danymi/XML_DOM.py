import xml.dom.minidom

xml_file_handler = xml.dom.minidom.parse("files/xml_file.xml")
book = xml_file_handler.documentElement.getElementsByTagName('book')

book_title = book[0].getElementsByTagName('title')[0].childNodes[0].data
book_author = book[0].getElementsByTagName('author')[0].childNodes[0].data
book_price = book[0].getElementsByTagName('price')[0].childNodes[0].data

print(f"Book: {book_title} {book_author} {book_price}")

# change book attributes
book[0].getElementsByTagName('title')[0].childNodes[0].data = 'This is a new book title!'
book[0].getElementsByTagName('author')[0].childNodes[0].data = 'This is a new book author!'
book[0].getElementsByTagName('price')[0].childNodes[0].data = 'This is a new book price!'
with open('files/xml_file_changed.xml', 'w+') as changed_file:
    changed_file.write(xml_file_handler.toxml())