iris_virginica = 'Iris virginica, with the common name Virginia iris, is a perennial ' \
                 'species of flowering plant, native to eastern North America. It is ' \
                 'common along the coastal plain from Florida to Georgia in the ' \
                 'Southeastern United States. It is one of the three Iris species ' \
                 'in the Iris flower data set outlined by Ronald Fisher in his 1936 ' \
                 'paper "The use of multiple measurements in taxonomic problems" ' \
                 'as an example of linear discriminant analysis.'

iris_setosa = 'Iris setosa (also known as bristle-pointed iris), is a species in the genus ' \
              'Iris, it is also in the subgenus Limniris and in the series Tripetalae. ' \
              'It is a rhizomatous perennial from a wide range across the Arctic sea, ' \
              'including Alaska, Maine, Canada (including British Columbia, Newfoundland, ' \
              'Quebec and Yukon), Russia (including Siberia), northeastern Asia, China, ' \
              'Korea and southwards to Japan. The plant has tall branching stems, mid green ' \
              'leaves and violet, purple-blue, violet-blue, blue, to lavender flowers. ' \
              'There are also plants with pink and white flowers.'

iris_versicolor = 'Iris versicolor is also commonly known as the blue flag, ' \
                  'harlequin blueflag, larger blue flag, northern blue flag, ' \
                  'and poison flag, plus other variations of these names, and ' \
                  'in Britain and Ireland as purple iris. It is a species of ' \
                  'Iris native to North America, in the Eastern United States ' \
                  'and Eastern Canada. It is common in sedge meadows, marshes, ' \
                  'and along streambanks and shores. The specific epithet ' \
                  'versicolor means "variously coloured". It is one of the ' \
                  'three Iris species in the Iris flower data set outlined by ' \
                  'Ronald Fisher in his 1936 paper "The use of multiple ' \
                  'measurements in taxonomic problems" as an example of ' \
                  'linear discriminant analysis.'


def give_description(predicted_type):
    if 'virginica' in predicted_type:
        return iris_virginica

    elif 'setosa' in predicted_type:
        return iris_setosa

    else:  # versicolor in predicted type
        return iris_versicolor
