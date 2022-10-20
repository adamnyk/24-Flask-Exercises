"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, id, title, words, text):
        """Create story with words and template text."""

        self.id = id
        self.title = title
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story = Story(
    1,
    "Once upon a time...",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
        large {adjective} {noun}. It loved to {verb} {plural_noun}.""",
)

story2 = Story(
    2,
    "Adventure!",
    ["place", "adjective", "noun", "verb", "plural_noun", "adjective"],
    """One day I will travel to {place} to explore and find the {adjective} {noun} that lives there. If the legends are true, maybe I will even be able to {verb} the secret {plural_noun} and become {adjective}""",
)

story3 = Story(
    3,
    "My pet",
    ["name", "adjective", "noun", "verb", "plural_noun", "place"],
    """My pet {name} is a {adjective} {noun}. It's faviorite thing to do is to {verb} in the {plural_noun} and go to {place}""",
)

stories = {story.id: story for story in [story, story2, story3]}
