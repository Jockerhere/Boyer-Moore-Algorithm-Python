def indexer(main_text: str)-> dict:
    """This function utilizes the Boyer-Moore algorithm to locate the specified phrases that users are searching for."""
    alphabets_dict = {}
    for index_, char in enumerate(main_text):


        if char.isalpha() == True:
            if char.lower() not in alphabets_dict.keys():
                
                alphabets_dict[char.lower()] = []
                alphabets_dict[char.lower()].append(index_)

            else:
                alphabets_dict[char.lower()].append(index_)

        else:
            pass

    return alphabets_dict


def searchInText(main_text: str, phrase: str, alphabets_dict: dict)->list: # The "alphabets_dict" was generated by the indexer function applied to our main_text. This was established in an earlier step.
    locations = []

    for indexer_loc in alphabets_dict[phrase[0].lower()]: # Move to the indexes collected in our indexer dictionary for the first character of the phrase(phrase[0] char).
        # for counter in range(len(phrase)):
        if main_text[indexer_loc:indexer_loc + len(phrase)].lower() != phrase.lower():
            pass

        else:
             locations.append([indexer_loc, indexer_loc + len(phrase)])

    return locations


def show_in_text(main_text: str, phrase: str)-> str:
    phrase_locs = searchInText(main_text, phrase, indexer(main_text))

    main_text = main_text[:phrase_locs[0][0]] + '"' + main_text[phrase_locs[0][0]:phrase_locs[0][1]] + '"' + main_text[phrase_locs[0][1]:]
    print(len(main_text))
    for i in range(1, len(phrase_locs)):
        phrase_locs[i][0] += 2
        phrase_locs[i][1] += 2

    for i in range(1, len(phrase_locs)):
        loc = phrase_locs[i]
        main_text = main_text[:loc[0]] + '"' + main_text[loc[0]:loc[1]] + '"' + main_text[loc[1] + 1:]
        for j in range(i, len(phrase_locs)):
            phrase_locs[j][0] += 1
            phrase_locs[j][1] += 1

    return main_text
