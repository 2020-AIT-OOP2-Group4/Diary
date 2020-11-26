from diaries.DiarySample import DiarySample
from diaries.k19056DiaryNew import k19056DiaryNew

diaries = [DiarySample(), k19056DiaryNew(), ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()