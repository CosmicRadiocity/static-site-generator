from htmlnode import HTMLNode

class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("missing tag")
        
        if self.children == None:
            raise ValueError("missing children")
        
        return f"<{self.tag}>{"".join(list(map(lambda child: child.to_html(), self.children)))}</{self.tag}>"