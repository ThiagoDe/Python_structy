def solution(queries):

    # queries = [
    #   ["SET", "A", "B", "E"],
    #   ["SET", "A", "C", "F"],
    #   ["GET", "A", "B"],
    #   ["GET", "A", "D"],
    #   ["DELETE", "A", "B"],
    #   ["DELETE", "A", "D"]
    # ]
    states = []
    dbState = {}

    for query in queries:

        if query[0] == "SET":
            key, field, val = query[1:]
            if key not in dbState:
                dbState[key] = {field: val}
                states.append('')
            else:
                dbState[key].update({field: val})
                states.append('')
        print(dbState)

        if query[0] == "GET":
            key, field = query[1:]
            # print(key, 'key')
            # print(field, 'f')
            if key in dbState:
                if field in dbState[key]:
                    states.append(dbState[key][field])
                else:
                    states.append('')
            else:
                states.append('')

        if query[0] == "DELETE":
            key, field = query[1:]
            print(key, 'k')
            print(field, 'f')
            if key not in dbState:
                states.append('false')
            elif field in dbState[key]:

                dbState[key].pop(field)
                states.append('true')
            else:
                states.append('false')

        if query[0] == "SCAN":
            key, s = query[1:]

            if key in dbState:
                if s == '':
                    arr = dbState[key].items()
                    res = []
                    for e in arr:
                        # print   map(stre[1:])
                        newel = ''.join((e[0])) + '(' + ','.join((e[1:])) + ')'
                        # e2 =  '(' + ', '.join((e[1:])) + ')'
                        res.append(newel)
                        # res.append(e2)
                        print(newel)

                    states.append(', '.join(res))
                else:
                    print(s)
                    res = [k for (k, v) in dbState[key].items() if s in k]
                    print(res)
                    xf = []
                    for i in res:
                        temp = dbState[key][i]
                        x = i + '(' + str(temp) + ')'
                        xf.append(x)

                    rever = xf.reverse
                    # print(rever)
                    states.append(', '.join(xf))
            else:
                pass

    print(dbState)
    return states
