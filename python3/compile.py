import ast
import astunparse
import tempfile
import subprocess


class TypeHintRemover(ast.NodeTransformer):

    def visit_FunctionDef(self, node):
        # remove the return type defintion
        node.returns = None
        # remove all argument annotations
        if node.args.args:
            for arg in node.args.args:
                arg.annotation = None
        return node

    def visit_Import(self, node):
        node.names = [n for n in node.names if n.name != 'typing']
        return node if node.names else None

    def visit_ImportFrom(self, node):
        return node if node.module != 'typing' else None


def remove_type_hints(code):
    try:
        # parse the source code into an AST
        parsed_source = ast.parse(code)
        # remove all type annotations, function return type definitions
        # and import statements from 'typing'
        transformed = TypeHintRemover().visit(parsed_source)
        # convert the AST back to source code
        return astunparse.unparse(transformed)
    except Exception as e:
        print(e)
        return code


def check_syntax(code):
    code = remove_type_hints(code)

    # save code to a temp file and run it
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", suffix=".py", delete=False) as f:
        f.write(code)
        f.flush()
        result = subprocess.run(["python", f.name], capture_output=True)
        # print(result.stderr.decode())
        f.close()
        return result.returncode == 0
