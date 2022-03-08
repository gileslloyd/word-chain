## The Goal
Create a console application that finds the shortest chain between 2 words changing one letter at a time.
Each intermediary word must be in the given dictionary and the result must be written to the provided file path.

## The solution
My solution was to create a graph of all of the words in the given dictionary. Using the words themselves
as the nodes and adding edges connecting each word to every other that it has just 1 letter difference to.

Once the graph is created it is then easy to find the shortest path between 2 nodes giving the chain of words.

One drawback to this approach is that creating the graph is fairly slow. However the graph could potentially be cached
or stored as an edgelist or adjacency matrix once created making subsequent queries much faster.

## Areas for improvement
 - The unit test coverage is low,
 - More examples of expected paths would be beneficial for the word chain service test,
 - I've not included any integration tests,
 - I was intending to provide a docker file and makefile with recipes to run the app within a container, however I ran out of time,

## Running the application
The `wordchain` entry point configured to use a virtual environment called `venv` so you must create this first:
`python -m venv venv`

Activate the environment and install the requirements from the requirements file. Then you can run the app like so:

```
usage: wordchain [-h] -d DICTIONARYFILE -s STARTWORD -e ENDWORD -r RESULTFILE

optional arguments:
  -h, --help            show this help message and exit
  -d DICTIONARYFILE, --DictionaryFile DICTIONARYFILE
                        The path to the input dictionary file
  -s STARTWORD, --StartWord STARTWORD
                        A four letter word from the dictionary to start
  -e ENDWORD, --EndWord ENDWORD
                        A four letter word from the dictionary to end
  -r RESULTFILE, --ResultFile RESULTFILE
                        The target file to write the result to
```

E.g.

`./wordchain --DictionaryFile=./data/words-english.txt --StartWord=Spin --EndWord=Spot --ResultFile=results/result.txt`
