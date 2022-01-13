def stable_matching(hospitals,hospitals_rank, candidates_rank):
    stable_matching = {}
    candidates = list(candidates_rank.keys())
    offers = list(hospitals.keys())
    tentative_matches = {k:[] for k in candidates}
    while len(offers) > 0:
        hospital = offers[0]
        if len(hospitals_rank[hospital]) > 0:
            candidate = hospitals_rank[hospital][0]
            hospitals_rank[hospital].pop(0)
            if tentative_matches[candidate] == []:
                index_current_hospital = hospitals[hospital]
                if len(candidates_rank[candidate]) > index_current_hospital:
                    tentative_matches[candidate].append(hospital)
                offers.pop(0)
            else:
                offers.pop(0)
                index_current_hospital = hospitals[hospital]
                index_hospital_in_current_tentative_match = hospitals[tentative_matches[candidate][0]]
                if len(candidates_rank[candidate]) > index_current_hospital and len(candidates_rank[candidate]) > index_hospital_in_current_tentative_match:
                    hospital_rank_of_current_candidate = candidates_rank[candidate][index_current_hospital]
                    hospital_rank_of_current_tentative_match = candidates_rank[candidate][index_hospital_in_current_tentative_match]
                    if hospital_rank_of_current_tentative_match > hospital_rank_of_current_candidate:
                        offers.append(tentative_matches[candidate][0])
                        tentative_matches[candidate].pop(0)
                        tentative_matches[candidate].append(hospital)
                    else:
                        offers.append(hospital)
        else:
            offers.pop(0)
    return tentative_matches

if __name__ == '__main__':
    hospitals = {
        'A': 0,
        'B': 1,
        'C': 2,
    }
    hospitals_rank = {
        'A': ['Q','P'],
        'B': ['Q','R','P'],
        'C': ['R','Q'],
    }
    candidates_rank = {
        'P': [3,2,1],
        'Q': [1,2],
        'R': [2,1],
    }
    stable_matching = stable_matching(hospitals,hospitals_rank, candidates_rank)
    print(stable_matching)