import re
from py.code import Source

class ContextProcessor:
    
    @staticmethod
    def get_page_context(page):
        start = re.compile(r'.*?{%\s*hyde\s*(.*?)(%}|$)')
        end = re.compile(r'(.*?)(%})')
        fin = open(page,'r')
        started = False
        source_code = ''
        matcher = start
        for line in fin:
            match = matcher.match(line)
            if match:
                source_code = source_code + match.group(1)
                if started: break
                else:
                    matcher = end 
                    started = True
            elif started:
                source_code = source_code + line
        fin.close()
        page_context = {}
        source_code = "page_context.update(" + source_code + ")"
        source = Source(source_code)
        exec source.compile()
        return page_context