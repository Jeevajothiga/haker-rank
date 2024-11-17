def merge_the_tools(s, k):
    # Divide string into substrings of length k
    for i in range(0, len(s), k):
      substring = s[i:i+k]
      seen = set()
      result = []
      for char in substring:
        if char not in seen:
          result.append(char)
          seen.add(char)
      print("".join(result))
