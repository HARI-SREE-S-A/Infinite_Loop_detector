import ast

class loop_tracker:
    def __init__(self):
        self.loopcount = 0
    def test_for(self,node):
        self.loopcount += 1
        self.generic_visit(node)
    def test_while(self,node):
        self.loopcount += 1
        self.generic_visit(node)
    def infinite_loop(code):
        tree = ast.parse(code)
        tracker = loop_tracker()
        tracker.visit(tree)
        for_loop_count = tracker.loopcount
        tracker.loopcount = 0
        tracker.visit(tree)
        while_loop_count = tracker.loopcount
        total = for_loop_count + while_loop_count

        if total > 10000:
            return True

