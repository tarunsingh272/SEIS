# process_html.py
import stack as s
# read string HTML and parse to list of tokens and content

html = '''
<html>
   <head>
      <title>
         Example
      </title>
   <body>
   </head>
      <h1> Hello, world </h1>
   </body>
</html>
'''

tag_list = html.split()
print (tag_list)
# while True:
#     next_element = ''
#     ch = html[index]
#     if ch=='<': # start a new tag?
tag_stack = s.Stack()
for tag in tag_list:
    # starts with </ => pop and try to match
    print ("processing:", tag)
    if tag.startswith('</'):
        pushed_tag = tag_stack.pop()
        print ("popped", pushed_tag)
        if tag[2:] != pushed_tag[1:]: # do they match?
            print ("invalid HTML:")
            print (tag, "doesn't match with ", pushed_tag)
            exit(1)
        else:
            print (tag,"matches",pushed_tag)
    elif tag.startswith('<'): # new tag?
        print ("pushing", tag)
        tag_stack.push(tag)
    else:
        print (tag, "isn't a opening or closing tag.")
        pass # not an opening or closing tag, so

