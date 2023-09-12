from flask import Flask, request, Response, jsonify


application = Flask("Get Letter Counts")

"""
URL parameters: base/page/?name=chris&othervar=yes

This is the only way to add extra parameters to a GET request
"""


@application.route("/", methods=["GET"])
def get_counts() -> Response:
    r = request.args
    try:
        phrase = r["phrase"]
    except KeyError:
        return jsonify({"Error": "You must provide a phrase."})

    result: dict[str, int] = get_letter_counts_in_phrase(phrase)
    return jsonify(result)


def get_letter_counts_in_phrase(phrase: str) -> dict[str, int]:
    # Create an empty dictionary for counts
    counts_dict: dict[str, int] = {}
    # Loop through each character in the phrase
    for char in phrase:
        # If not in dict, add key = 1
        if char not in counts_dict:
            counts_dict[char] = 1
        else:
            # If already in dict, key += 1
            counts_dict[char] += 1

    return counts_dict
