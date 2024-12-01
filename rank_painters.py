from sortedcontainers import SortedSet
# rating paintings
# if Like, +1, if dislike -1
# return top K  painters
class TopPainting:
    def __init__(self, participant_count):
        self._scores = [0]*participant_count
        initial_frequences = [(0, id) for id in range(participant_count)]
        self._ordered_works = SortedSet(initial_frequences)

    def change_score(self, participant_id, change):
        old_participant_stat = (self._scores[participant_id], participant_id)
        self._ordered_works.remove(old_participant_stat)

        self._scores+=change 

        new_participant_stat = (self._scores[participant_id], participant_id)
        self._ordered_works.add(new_participant_stat)

    def like(self, participant_id):
        self.change_score(participant_id, 1)

        
    def dislike(self, participant_id):
        self.change_score(participant_id, -1)

    def get_best_works(self, K):
        return [id for (_, id) in self._ordered_works[-K:][::-1]]
        
