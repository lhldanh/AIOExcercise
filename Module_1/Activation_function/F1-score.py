def f1_score(tp, fp, fn):

    if (tp <= 0 or fp <= 0 or fn <= 0):
        str = 'tp ' * (tp <= 0)  + 'fp ' * (fp <= 0) +  'fn ' * (fn <= 0) + 'must be greater than 0'
        print(str)
        return None 
    
    if (not (isinstance(tp, int) and isinstance(fp, int) and isinstance(fn, int))):
        str = 'tp ' * (not isinstance(tp, int))  + 'fp ' * (not isinstance(fp, int)) + 'fn ' * (not isinstance(fn, int)) + 'must be int'
        print(str)
        return None
    
    prescision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * prescision * recall / (prescision + recall)

    return (prescision, recall, f1_score)

print(f1_score(tp = 0, fp = 3, fn = 4))
        