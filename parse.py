import ast

with open("lek_med_ast.py") as file:
    root_node = ast.parse(file.read())

    for node in ast.walk(root_node):
        if isinstance(node, ast.FunctionDef) and node.name == "main":
            main_node = node

    for node in ast.walk(root_node):
        print(ast.dump(node))
        if isinstance(node, ast.Import):
            for module in  node.names:
                print(module.name)
        if isinstance(node, ast.ImportFrom):
            print(node.module)
            for fun in node.names:
                print(("fun", fun.name))
        print("")

    print(ast.dump(root_node))
    print("")

    print(ast.dump(main_node))
    print("")
