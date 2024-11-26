# Formal Contexts

This repository contains a collection of formal contexts to pursue
[Formal Concept Analysis](https://upriss.github.io/fca/fca.html).

The metadata for [the
contexts](https://github.com/fcatools/contexts/tree/main/contexts) is
contained in [this YAML file](merged-contexts-metadata.yaml).

More contexts can be found in the repository for
[ConExp-CLJ](https://github.com/tomhanika/conexp-clj/tree/dev/testing-data),
the repository for the [concepts Python
module](https://github.com/xflr6/concepts/tree/master/examples), and
on [Uta Priss' page](https://upriss.github.io/fca/examples.html).

## How to use the contexts

You can either manually download contexts or you can access them
directly in your program code with a URL generated as follows: append
the file name of the context (e.g., `livingbeings_en.cxt`) to the
prefix `https://github.com/fcatools/contexts/raw/main/contexts/`. For
example, in Python 3 you could do:

```python
import urllib.request

url = "https://github.com/fcatools/contexts/raw/main/contexts/living-beings-and-water/livingbeings_en.cxt"
context = urllib.request.urlopen(url).read().decode("utf-8")
```

## How to contribute contexts

Additional formal contexts are highly welcome if they fulfil the
following criteria:

1. They should be about real things and not contain invented or random
   data.
2. They should preferrably be small, that is, have not too many
   attributes and objects (each less than 100).

If you think your context is suitable, then proceed as follows:

1. [Fork this repository](https://github.com/fcatools/contexts/fork)
   and make the following changes in your fork:
   1. Add a subfolder to the [contexts](https://github.com/fcatools/contexts/tree/main/contexts)
      directory, and add your ASCII-encoded CXT file there.
      Use a meaningful name for both (English, all lowercase, with
      two letters indicating the [ISO 639 language code](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes)
      at the end, e.g., `bodiesofwater_de.cxt` for the German bodies
      of water context).
   2. Describe your context in a metadata yaml file
      following the example of the other contexts. Try to be concise
      and precise.
   3. Optionally: Merge the metadata automatically by running the included python script
      ([scripts/merge_contexts_metadata.py](scripts/merge_contexts_metadata.py),
      requires ```pyyaml```).
2. Make a pull request to merge your changes into this repository.

## Further information

The idea for the repository has been described in

> Hanika, T., Jäschke, R.: A Repository for Formal Contexts. In:
> Cabrera, I.P., Ferré, S., and Obiedkov, S. (eds.) *Conceptual
> Knowledge Structures*. pp. 182–197. Springer Nature Switzerland,
> Cham 2024.
> doi:[10.1007/978-3-031-67868-4_13](https://doi.org/10.1007/978-3-031-67868-4_13)

The first meeting of the **working group** is scheduled for Friday,
November 22, 2024 at 15:00 CET.
