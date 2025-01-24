import re

def validate_html(html: str) -> bool:
    valid_tags = {'p', 'b', 'ul', 'ol', 'li','body'}
    
    tag_pattern = re.compile(r'</?([a-zA-Z0-9]+)>')
    
    stack = []
    
    for match in tag_pattern.finditer(html):
        tag = match.group(0)
        tag_name = match.group(1)
        
        if tag.startswith('</'):  
            if not stack or stack[-1] != tag_name:
                return False  
            stack.pop()  
        else:  
            if tag_name in valid_tags:
                stack.append(tag_name)  
    
    
    return len(stack) == 0

# Test cases
html_1 = "<body> hello world </body>"
print(validate_html(html_1))  

html_2 = "<p>Hello World!</p>"
print(validate_html(html_2))  

html_3 = "<p>Hello <b>World</b>!</p>"
print(validate_html(html_3))  

html_4 = "<p>Hello <b>World</p>!</b>"
print(validate_html(html_4))  
