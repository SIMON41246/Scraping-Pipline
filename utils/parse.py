from selectolax.parser import Node



















# def parse_row_attributes(node: Node, selectors: list):
#     parsed = {}
# 
#     for s in selectors:
#         match = s.get('match')
#         type = s.get('type')
#         selector = s.get('selector')
#         name = s.get('name')
# 
#         if match == "all":
#             matched = node.css(selector)
#             if type == "text":
#                 parsed[name] = [node.text() for node in matched]
#             elif type == 'node':
#                 parsed[name] = matched
#         elif match == 'first':
#             matched = node.css_first(selector)
# 
#             if type == "text":
#                 parsed[name] = matched.text()
#             elif type == 'node':
#                 parsed[name] = matched
#     return parsed
