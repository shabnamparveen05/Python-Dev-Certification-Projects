def add_time(start, duration,d_day=None):
    import re
    start_hm_list=re.findall('[0-9]+',start)
    post_time=re.findall('[A-Z]+',start)
    duration_hm_list = re.findall('[0-9]+', duration)

    start_hm_list[0]=int(start_hm_list[0])
    start_hm_list[1]=int(start_hm_list[1])

    duration_hm_list[0] = int(duration_hm_list[0])
    duration_hm_list[1] = int(duration_hm_list[1])
    post_time_copied=post_time.copy()
    post_time_copied02= post_time.copy()
    post_time_copied03= post_time.copy()
    # print(start_hm_list)
    # calculation
    hours=start_hm_list[0]+duration_hm_list[0]
    minutes=start_hm_list[1]+duration_hm_list[1]
    hours = hours + int(minutes / 60)

    if hours>11:
        def change(post_time):
            if post_time[0] == 'PM':
                post_time[0] = 'AM'
            else:
                post_time[0] = 'PM'
            return post_time
        # adding hour from minutes
        #if minutes>59:
        time_m=int(minutes%60)
        #hour=12*6+1, 6=factor, 1=time_h
        factor=int(hours/12)
        time_h=int(hours%12)
        #print(time_h)
        #print(time_h)
        if time_h==0:
            time_hh=time_h
            time_h=12
        else:
            time_hh=time_h
        just_after12=0

        if time_hh==0:
            if factor%2!=0:
                if time_m>0:
                    change(post_time)
                    just_after12='extra am/pm'
                else:
                    pass
            else:
                change(post_time)
        else:
            if factor % 2!= 0:
                change(post_time)
                just_after12 = 'extra am/pm'
            else:
                just_after12 = 'extra am/pm'
                pass

        def count_days():
            d = dict()
            g = 1
            while g <= factor:
                if g % 2 != 0:
                    if g!=1:
                        change(post_time_copied)
                    d[post_time_copied[0]] = d.get(post_time_copied[0], 0) + 1
                else:
                    change(post_time_copied)
                    d[post_time_copied[0]] = d.get(post_time_copied[0], 0) + 1
                g += 1
            try:
                d['AM']
            except:
                d['AM'] = 0

            if just_after12=='extra am/pm':
                change(post_time_copied)
                d[post_time_copied[0]] = d.get(post_time_copied[0], 0) + 1
            if post_time_copied03[0]=='AM':
                d['AM']=d['AM']-1
                return d['AM']
            else:
                return d['AM']
        days=count_days()

        time_m=str(time_m).zfill(2)
        if d_day is not None:
            import itertools
            list = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
            iterator = itertools.cycle(list)
            index = list.index(d_day.lower())
            for i in range(index):
                next(iterator)
            counter = 0
            for i in iterator:
                # print(i)
                counter += 1
                if counter > days:  # Arbitrary limit to prevent infinite output
                    break
            next_day = i.capitalize()
            if days==0:
                return f'{time_h}:{time_m} {post_time[0]}, {d_day}'
            elif days==1:
                return f'{time_h}:{time_m} {post_time[0]}, {next_day} (next day)'
            else:

                return f'{time_h}:{time_m} {post_time[0]}, {next_day} ({days} days later)'
        else:
            if days==0:
                return f'{time_h}:{time_m} {post_time[0]}'
            elif days==1:
                return f'{time_h}:{time_m} {post_time[0]} (next day)'
            else:
                return f'{time_h}:{time_m} {post_time[0]} ({days} days later)'

    else:
        time_m = int(minutes % 60)
        time_m=str(time_m).zfill(2)
        if d_day is not None:
            return f"{hours}:{time_m} {post_time[0]}, {d_day}"
        else:
            return f"{hours}:{time_m} {post_time[0]}"



add_time('3:30 PM', '2:12')
add_time('11:55 AM', '3:12')
add_time('2:59 AM', '24:00') #(next day)
add_time('11:59 PM', '24:05')
add_time('8:16 PM', '466:02')
add_time('3:30 PM', '2:12', 'Monday') #Monday
h=add_time('2:59 AM', '24:00', 'saturDay')# sunday(nextday)
add_time('11:59 PM', '24:05', 'Wednesday')
add_time('8:16 PM', '466:02', 'tuesday') #102s
print(h)
