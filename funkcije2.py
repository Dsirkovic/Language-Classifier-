
def freq_distr(sequence):
    dictionary={}
    for event in sequence:
        dictionary[event]=dictionary.get(event,0)+1
    return dictionary

def sort_distr(dictionary):
    return sorted(dictionary.items(),key=lambda x:-x[1])


def prob_distr(distr):
      event_number=float(sum(distr.values()))
      for event in distr:
        distr[event]/=event_number
      return distr

def sequence_probability(sequence,prob_distr):
      from math import log
      probability=0.0
      for event in sequence:
        if event in prob_distr:
          probability+=log(prob_distr[event])
      return probability

def smoothen(model):
    all_events=set()
    for word_class in model:
        for event in model[word_class]:
            all_events.add(event)
    for word_class in model:
        for event in all_events:
            model[word_class][event]=model[word_class].get(event,0)+1
        model[word_class]=prob_distr(model[word_class])
    return model

def classify(sequence,model):
    prob={}
    for word_class in model:
        prob[word_class]=sequence_probability(sequence,model[word_class])
    return sort_distr(prob)[0][0]



