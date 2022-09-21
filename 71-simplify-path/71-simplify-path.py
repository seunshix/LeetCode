class Solution:
    def simplifyPath(self, path: str) -> str:
        if path is None:
            return "Error"

        path_names = []
        if path[0] == '/':
            path_names.append('/')
        print(path.split('/'))
        for token in (i for i in path.split('/') if i not in ['.', '']):
            if token == '..':
                if not path_names or path_names[-1] == ['..']:
                    path_names.append(token)
                    print(path_names)
                else:
                    if path_names[-1] == '/':
                        continue
                    path_names.pop()
                    print(path_names)
            else:
                path_names.append(token)
                print(path_names)

        result = '/'.join(path_names)
        return result[result.startswith('//'):]

        