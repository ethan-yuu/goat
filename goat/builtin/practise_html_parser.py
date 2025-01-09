from html.parser import HTMLParser


class DefaultHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('handle_starttag -- > tag: {}, attrs: {}'.format(tag, attrs))

    def handle_endtag(self, tag):
        print('handle_endtag --> tag: {}'.format(tag))

    def handle_startendtag(self, tag, attrs):
        print('handle_startendtag --> tag: {}, attrs: {}'.format(tag, attrs))

    def handle_data(self, data):
        print('handle_data --> date: {}'.format(data))

    def handle_comment(self, data):
        print('handle_comment --> comment: {}'.format(data))

    def handle_entityref(self, name):
        print('handle_entityref --> name: {}'.format(name))

    def handle_charref(self, name):
        print('handle_charref --> name: {}'.format(name))


def parser_html():
    parser = DefaultHTMLParser()
    parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')


if __name__ == '__main__':
    parser_html()
