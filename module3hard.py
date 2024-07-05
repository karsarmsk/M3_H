data_structure = [
    [1, 2, 3],
   {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
   ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(args):
  s =0

  for i in args:
    if type(i) != None:
      print(type(i))
      if isinstance(i, int):
         s += i
      if isinstance(i, list):
        for j in i:
          if isinstance(j, int):
            s += j
          else:
            s += calculate_structure_sum(j)
      elif isinstance(i, dict):
        for k, v in i.items():
          s = s + v + len(k)
      elif isinstance(i, str):
        s += len(i)
      elif isinstance(i, tuple):
        s = s + calculate_structure_sum(i)
    else: break
  return s

result = calculate_structure_sum(data_structure)
print(result)
