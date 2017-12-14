allergy_map = {
    'eggs': 1,
    'peanuts': 2,
    'shellfish': 4,
    'strawberries': 8,
    'tomatoes': 16,
    'chocolate': 32,
    'pollen': 64,
    'cats': 128,
}


class Allergies(object):

    def __init__(self, score):
        self.score = score

    def is_allergic_to(self, item):
        return bool(self.score & allergy_map[item.lower()])

    @property
    def lst(self):
        return [key for key in allergy_map.keys() if self.is_allergic_to(key)]
