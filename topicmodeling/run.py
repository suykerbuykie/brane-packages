#!/usr/bin/env python3
import os
import sys
import yaml
from utils import removeDuplicates

def tuple(input: str) -> str:
  wordlist = input.split()
  wordfreq = [wordlist.count(w) for w in wordlist]

  return str(removeDuplicates(list(zip(wordlist, wordfreq))))



if __name__ == "__main__":
  command = sys.argv[1]
  argument_input = os.environ["INPUT"]
  functions = {
    "tuple": tuple,
  }
  output = functions[command](argument_input)
  print(yaml.dump({"output": output}))
