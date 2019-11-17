from parsimonious.nodes import NodeVisitor


class Visitor(NodeVisitor):
    def generic_visit(self, node, visited_children):
        """ The generic visit method. """
        return visited_children or node

    def visit_expr(self, node, children):
        """ Returns the overall output. """
        s, *_ = children
        return s

    def visit_zero(self, node, children):
        _, directive, *_ = children
        return directive.text,

    def visit_one(self, node, children):
        _, directive, _, p1, *_ = children
        return directive.text, p1.text

    def visit_two(self, node, children):
        _, directive, _, p1, _, p2, *_ = children
        return directive.text, p1.text, p2.text

    def visit_comment(self, node, children):
        _, prefix, comment, *_ = children
        return prefix.text, comment.text
