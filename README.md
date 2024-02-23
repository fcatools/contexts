# Formal Contexts

This repository contains a collection of formal contexts to pursue
[Formal Concept Analysis](https://upriss.github.io/fca/fca.html).

- [Mordmethoden in Miss-Marple-Romanen](contexts/missmarple_de.ctx)
  - source: Schott, Ben (2004). Schotts Sammelsurium. Bloomsbury, Berlin
  - size: 12 objects, 6 attributes
  - language: German / English
  - description: methods of murder in Miss Marple novels (not short stories!)
- [Gewässer](contexts/gewaesser_de.ctx)
  - source: Wille, Rudolf (1984). Liniendiagramme hierarchischer
    Begriffssysteme. Studien zur Klassifikation. Indeks Verlag
  - size: 8 objects, 6 attributes
  - language: German
  - description: bodies of water and their properties
- [Gewürzplaner](contexts/gewuerzplaner_de.ctx)
  - source: Mahn, M. (2014). Gewürze: Das Standardwerk. Christian Verlag GmbH, München
  - size: 56 objects, 37 attributes
  - language: German
  - descriptions: spices and herbs together and the meals they match

The two example contexts are also described in [this YAML file](contexts.yaml).

More contexts can be found in the [ConExp-CLJ
repository](https://github.com/tomhanika/conexp-clj/tree/dev/testing-data)
and on [Uta Priss' page](https://upriss.github.io/fca/examples.html).

## How to use the contexts

You can either manually download contexts or you can access them
directly in your program code with a URL generated as follows: append
the file name of the context (e.g., `gewaesser_de.ctx`) to the prefix
`https://github.com/fcatools/contexts/raw/main/contexts/`. For
example, in Python 3 you could do:

```python
import urllib.request

url = "https://github.com/fcatools/contexts/raw/main/contexts/gewaesser_de.ctx"
context = urllib.request.urlopen(url).read().decode()
```

## How to contribute contexts

Additional formal contexts are highly welcome if they fulfil the
following criteria:

1. They should be about real things and not contain invented or random
   data.
2. They should preferrably be small, that is, have not too many
   attributes and objects (each less than 100).

If you think your context is suitable, then proceed as follows:

1. [Fork this repository](/fcatools/contexts/fork) and make the
   following changes in your fork:
   1. Add your ASCII-encoded CXT file to the [contexts](contexts)
      directory, using a meaningful name (all lowercase, with two
      letters indicating the ISO language code at the end, e.g.,
      `gewaesser_de.ctx` for the German bodies of water context).
   2. Describe your context in [contexts.yaml](contexts.yaml) following
      the example of the other contexts. Try to be concise and precise.
2. Make a pull request to merge your changes into the this
   repository.
