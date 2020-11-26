from diaries.DiarySample import DiarySample
from diaries.K19096DiaryNew import K19096DiaryNew


diaries = [DiarySample(), K19096DiaryNew(),]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()