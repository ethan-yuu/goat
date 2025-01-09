from pyexpat import ParserCreate


class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax: start_element: {} , attrs: {}'.format(name, attrs))

    def end_element(self, name):
        print('sax: end_element: {}'.format(name))

    def char_data(self, text):
        print('sax: char_data: {}'.format(text))


xml_data = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''


def sax_analysis(xml_data):
    handler = DefaultSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml_data)


if __name__ == '__main__':
    sax_analysis(xml_data)
