import re

def parse(markdown):
    lines = markdown.split('\n')  
    result = ''  

    # Will turned to True if asterisk symbol is present in front of the line, 
    # converting it to <ul><li> .... </li> only, without the closing </ul>
    in_list = False  

    # Will turned to True if the sequence of asterisks is over, then adding the closing </ul> to the line
    in_list_append = False  
    
    for i in lines:
        # Detect and convert h6, h2, and h1
        if re.match('###### (.*)', i):
            i = '<h6>' + i[7:] + '</h6>'
        elif re.match('## (.*)', i):
            i = '<h2>' + i[3:] + '</h2>'
        elif re.match('# (.*)', i):
            i = '<h1>' + i[2:] + '</h1>'
        
        # Detect asterisk (*) symbol
        m = re.match(r'\* (.*)', i)
        if m:
            # Asterisk is detected for the first time in the line
            if not in_list:
                in_list = True
                is_bold = False
                is_italic = False
                curr = m.group(1)
                # Detect and convert bold markdown
                m1 = re.match('(.*)__(.*)__(.*)', curr)
                if m1:
                    curr = m1.group(1) + '<strong>' + \
                        m1.group(2) + '</strong>' + m1.group(3)
                    is_bold = True
                # Detect and convert italic markdown
                m1 = re.match('(.*)_(.*)_(.*)', curr)
                if m1:
                    curr = m1.group(1) + '<em>' + m1.group(2) + \
                        '</em>' + m1.group(3)
                    is_italic = True
                # Convert asterisk markdown to HTML tags without the closing </ul>, in case the next line is still the part of the list
                i = '<ul><li>' + curr + '</li>'
            # In case the next line has asterisk markdown too
            else:
                is_bold = False
                is_italic = False
                curr = m.group(1)
                # Bold markdown
                m1 = re.match('(.*)__(.*)__(.*)', curr)
                if m1:
                    curr = m1.group(1) + '<strong>' + \
                        m1.group(2) + '</strong>' + m1.group(3)
                    is_bold = True
                # Italic markdown
                m1 = re.match('(.*)_(.*)_(.*)', curr)
                if m1:
                    curr = m1.group(1) + '<em>' + m1.group(2) + \
                        '</em>' + m1.group(3)
                    is_italic = True
                # Convert asterisk markdown of this line to HTML 
                i = '<li>' + curr + '</li>'
        else:  # Asterisk is not present anymore
            if in_list:
                in_list_append = True  # Turn to True to mark that the list sequence is over
                in_list = False

        # If this line is not a header or list, then it must be a pharagraph
        m = re.match('<h|<ul|<li', i)
        if not m:
            i = '<p>' + i + '</p>'
        
        # Bold markdown
        m = re.match('(.*)__(.*)__(.*)', i)
        if m:
            i = m.group(1) + '<strong>' + m.group(2) + '</strong>' + m.group(3)
        
        # Italic markdown
        m = re.match('(.*)_(.*)_(.*)', i)
        if m:
            i = m.group(1) + '<em>' + m.group(2) + '</em>' + m.group(3)
        
        # Adding the closing </ul> to the end of list sequence
        if in_list_append:
            i = '</ul>' + i
            in_list_append = False
        
        result += i
    
    # In case a line with asterisk is last line there is
    if in_list:
        result += '</ul>'
        
    return result
