import re
from operator import itemgetter  # for sorting the dictionaries


# Attention: The length of the scope includes the begining and end brackets
def get_scope_len(scope_data):
  pattern_open = re.compile(r"\{")
  pattern_close = re.compile(r"\}")

  index = 0
  level = 0
  scope_size = 1

  while (True):
    line = scope_data[index]
    num_open_brackets = len(pattern_open.findall(line))
    num_close_brackets = len(pattern_close.findall(line))
        level = level + num_open_brackets - num_close_brackets  # better to add condition, should do it
        if level != 0:
          scope_size += 1
          index += 1
        else:
          break

          return scope_size

'''
def find_matching_if_for_else(scope_data):
    pattern_open = re.compile(r"\{")
    pattern_close = re.compile(r"\}")

    index = 0
    level = 0
    scope_size = -1   # Starting from the end of the scope

    while (True):
        line = scope_data[index]
        num_open_brackets = len(pattern_open.findall(line))
        num_close_brackets = len(pattern_close.findall(line))
        level = level - num_open_brackets + num_close_brackets  # better to add condition, should do it
        if level != 0:
            scope_size += 1
            index -= 1
        else:
            break

    return scope[index-1]
    '''

###################################################################

# Test1:
code_input = '''for (i=5;i<22;i++)
{
if ( c <= 1 )
{
next = c;
gfh
gfdh
h
}
else
{
next = first + second;
first = second;
second = next;
}
}
printf("%d",next);
'''
## Test2:
code_input = '''print(bla)
for (i=1;i<12;i++)
{
for (j=1;j+1;j++)
{
print
}
}
'''
## Test3:
code_input = '''print(bla)
for (i=1;i<12;i++)
{
print()
}
print
'''

# Test4:
code_input='''print
print
for (i=1;i<5;i++)
{
for (j=0;j<9;j++)
{
print
print
}
}
print
'''
# Test5:
code_input='''if (a>b)
{
if (c<d)
{
for (i=0;i<9;i++)
{
print(grab)
print(great)
}
print
for (i=0;i<9;i++)
{
print(grab)
print(great)
}
}
}
'''
# Test6:
code_input='''for ( c = 0 ; c < n ; c++ )
{
if ( c <= 1 )
{
next = c;
}
else
{
next = first + second;
first = second;
second = next;
}
printf("%d",next);
}
'''

code_input='''for (i=5;i<22;i++)
{
if(c<=1)
{
next = c;
gfh
gfdh
h
for (j=2;j<10;j++)
{
print("gil")
print("gil2")
}
}
else
{
next = first + second;
first = second;
second = next;
}
}
printf("%d",next);'''


content = '[\w>.=!*\\+-\[\]><!\']*'  # For retrieving the data

c_keywords_specification = [
('IF', '(if\()(?P<IF_PREDICATE>' + content + ')(\))'),
('WHILE', '(while\()(?P<WHILE_PREDICATE>' + content + ')(\))'),
('DO', 'do'),
('FOR', '(for\()(?P<FOR_INIT>' + content + ');(?P<FOR_PREDICATE>' + content + ');(?P<FOR_INC>' + content + ')(\))'),
('GOTO', '(goto[ ]*)(?P<GOTO_LABEL_NAME>\w*)(;)'),
('ELSE_INLINE', 'else\{*(?P<ELSE_INLINE_BLOCK>[\w>.=!*\\+-><!\(\)\"]*\))\}*'),
('ELSE', 'else'),
('OPEN_BRACKETS', '{'),
('CLOSE_BRACKETS', '}'),
('SIMPLE_STATEMENT', '.*')
]

tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in c_keywords_specification)

regex_collection = re.compile(tok_regex)

code_line_by_line = code_input.splitlines()

line_number = 0

collection_of_segments = []

collection_of_segments.append({'start'      : -1,
 'end'        : len(code_line_by_line),
 'strict_type': 'st',
 'type'       : 'start',
 'level'      :  0,
 'text'       : 'no-text'})

collection_of_segments.append({'start'      : len(code_line_by_line),
 'end'        : len(code_line_by_line),
 'strict_type': 'e',
 'type'       : 'end',
 'level'      : 1,
 'text'       : 'no-text'})

# Writing down the cond number, and operation number of the whole program:
cond_num = 0
op_num = 0
else_num = 0

my_conds_ops_collection = {}
line_number = 0
level = 0
for line in code_line_by_line:
  line = line.replace(" ", "")
  regex_result = regex_collection.search(line)
  if regex_result == None:
    print("Couldn't find any match in the whole collection")
  else:
    keyword_type = regex_result.lastgroup
    if (keyword_type == "SIMPLE_STATEMENT"):
      op_num += 1
      current_op = "op" + str(op_num)
      my_conds_ops_collection.update({line_number: current_op})
      if (keyword_type == "IF") or (keyword_type == "FOR") or (keyword_type == "WHILE"):
        cond_num += 1
        current_cond = "cond" + str(cond_num)
        my_conds_ops_collection.update({line_number: current_cond})
        if (keyword_type == "ELSE"):
          else_num += 1
          current_else = "else_cond" + str(cond_num)
          my_conds_ops_collection.update({line_number: current_else})
          line_number += 1


          line_number = 0
          for line in code_line_by_line:
            line = line.replace(" ", "")
            regex_result = regex_collection.search(line)

            if regex_result == None:
              print("Couldn't find any match in the whole collection")
            else:
              keyword_type = regex_result.lastgroup
              print(str(line_number) + ")keyword_type: " + keyword_type)
              if (keyword_type == "SIMPLE_STATEMENT"):
                new_element = {'start'      : line_number,
                'end'        : line_number,
                'strict_type': my_conds_ops_collection[line_number],
                'type'       : 'SIMPLE_STATEMENT',
                'level'      : level+1,
                'text'       : line}

                collection_of_segments.append(new_element)

                if (keyword_type == "IF") or (keyword_type == "FOR") or (keyword_type == "WHILE"):
                  end_scope = line_number + get_scope_len(code_line_by_line[line_number + 1:])
                  new_element = {'start'      : line_number + 1,
                  'end'        : end_scope,
                  'strict_type': my_conds_ops_collection[line_number],
                  'type'       : keyword_type,
                  'level'      : level+1,
                  'text'       : 'no-text'}

                  collection_of_segments.append(new_element)

                  if (keyword_type == "ELSE"):
                    end_scope = line_number + get_scope_len(code_line_by_line[line_number + 1:])
                    new_element = {'start'      : line_number + 1,
                    'end'        : end_scope,
                    'strict_type': my_conds_ops_collection[line_number],
                    'type'       : keyword_type,
                    'level'      : level + 1,
                    'text'       : 'no-text'}
                    collection_of_segments.append(new_element)

                    if (keyword_type == "OPEN_BRACKETS"):
                      level+=1
                    elif (keyword_type == "CLOSE_BRACKETS"):
                      level-=1

                      line_number += 1

                      collection_of_segments_sorted = sorted(collection_of_segments, key=itemgetter('start'))

                      print("THE END - OK!!")
