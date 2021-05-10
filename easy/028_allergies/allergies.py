class Allergies:

    def __init__(self, score: int):
        self.score = score

    def allergic_to(self, item: str):
        return item in self.lst

    @property
    def lst(self):
        allergies_dict = {
            128: 'cats',
            64: 'pollen',
            32: 'chocolate',
            16: 'tomatoes',
            8: 'strawberries',
            4: 'shellfish',
            2: 'peanuts',
            1 : 'eggs'
        }

        allergies = []
        iterator = len(allergies_dict)
        scores = self.score % 256

        for score, allergy in allergies_dict.items():
            if scores == 0:
                break
            if scores >= score:
                allergies.insert(0, allergy)
                scores -= score
        
        return allergies         
