import re, bisect
books = {} 
shelve = []
end_ = re.compile('END')
while True:
    line = input()
    if re.match(end_, line): break
    title, author = re.findall('"(.*)" by (.*$)', line)[0]
    books[title] = (author, title)
    bisect.insort(shelve, (author, title))
returned = []
shelve_ = re.compile('SHELVE')
fmt = 'Put "{}" after "{}"'
while True:
    line = input()
    if re.match(end_, line): break
    if re.match(shelve_, line):
        for book in returned:
            pos = bisect.bisect(shelve, book)
            if not pos:
                print('Put "{}" first'.format(book[1]))
            else:
                print(fmt.format(book[1], shelve[pos-1][1]))
            bisect.insort(shelve, book)
        returned.clear()
        print('END')
        continue
    command, title = re.findall('(\w*) "(.*)"', line)[0]
    if command == 'BORROW':
        pos = bisect.bisect(shelve, books[title])
        shelve.pop(pos-1)
        continue
    if command == 'RETURN':
        bisect.insort(returned, books[title])


