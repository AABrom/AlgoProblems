# rating paintings
# if Like, +1, if dislike -1
# return top K  painters

class topPainting:

    def change_score(self, participant_id, change):
        self.scores[participant_id] += change

    def __init__(self, participant_count):
        self.scores = [0]*participant_count

    def like(self, participant_id):
        self.change_score(participant_id, 1)
        
    def dislike(self, participant_id):
        self.change_score(participant_id, -1)

    def get_best_works(self, K):
        scores_ids = [(value, id) for id, value in enumerate(self.scores)]
        scores_ids.sort(reverse=True)
        return [id for _, id in scores_ids[:K]]
