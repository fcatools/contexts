[![DOI](https://zenodo.org/badge/580832846.svg)](https://zenodo.org/badge/latestdoi/580832846)

# Formal Contexts

This repository contains a collection of formal contexts to pursue
[Formal Concept Analysis](https://upriss.github.io/fca/fca.html).

The metadata for [the
contexts](https://github.com/fcatools/contexts/tree/main/contexts) is
contained in [this YAML file](contexts.yaml).

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

url = "https://github.com/fcatools/contexts/raw/main/contexts/livingbeings_en.cxt"
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
   1. Add your ASCII-encoded CXT file to the
      [contexts](https://github.com/fcatools/contexts/tree/main/contexts)
      directory, using a meaningful name (English, all lowercase, with
      two letters indicating the [ISO 639 language
      code](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes)
      at the end, e.g., `bodiesofwater_de.cxt` for the German bodies
      of water context).
   2. Describe your context in [contexts.yaml](contexts.yaml)
      following the example of the other contexts. Try to be concise
      and precise.
2. Make a pull request to merge your changes into this repository.

## Working group

The repository is managed by a working group that communicates using a
[mailing
list](https://lists.cs.uni-kassel.de/postorius/lists/fca-repo.lists.cs.uni-kassel.de/).

## Recommended Citations

If you would like to reference a **single dataset** from this
repository, we suggest that you cite the source given in [the
metadata](contexts.yaml). This is typically the scholarly work where
the dataset was first used as a formal context or another publication
where it was found.

In addition, you can reference a **specific version** of a dataset
[using its versioned
URL](https://docs.github.com/en/repositories/working-with-files/using-files/getting-permanent-links-to-files).

If you would like to reference **several datasets** from this
repository or the repository itself, we suggest to (additionally) cite
the article where the idea for the repository has first been
described:

> Hanika, T., Jäschke, R.: A Repository for Formal Contexts. In:
> Cabrera, I.P., Ferré, S., and Obiedkov, S. (eds.) *Conceptual
> Knowledge Structures*. pp. 182–197. Springer Nature Switzerland,
> Cham 2024.
> doi:[10.1007/978-3-031-67868-4_13](https://doi.org/10.1007/978-3-031-67868-4_13)

You can also reference a [**specific
release**](https://github.com/fcatools/contexts/releases) of the
[repository on Zenodo](https://zenodo.org/badge/latestdoi/580832846).

Further machine-readable citation information can be found in the file
[CITATION.cff](CITATION.cff).
