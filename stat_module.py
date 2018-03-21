class StatModule:
    def analysis(self, today, new_d, old_d):
        #print(old_d[0][0])
        if len(old_d) < 1 or old_d[0][0] == today:
            return (new_d, False)
        else:
            #print(old_d[-1])
            i = 0
            t = 0
            while i < 50:
                if new_d[i]['game'] in old_d[-1]:
                    old_rank = old_d[-1].index(new_d[i]['game'])
                    new_rank = int(new_d[i]['rank'])
                    delta = old_rank - new_rank
                    if delta == 0:
                        new_d[i]['delta'] = '-'
                    elif delta < 0:
                        new_d[i]['delta'] = delta
                    elif delta > 0:
                        new_d[i]['delta'] = '+' + str(delta)
                else:
                    new_d[i]['delta'] = 'NEW'
                #print(new_d[i])
                i += 1

            need_save = old_d[0][0] != today

            return (new_d, need_save)
