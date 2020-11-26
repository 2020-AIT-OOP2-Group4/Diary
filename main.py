from diaries.DiarySample import DiarySample
from diaries.takamotoDiaryNew import TakamotoDiaryNew
from diaries.k19056DiaryNew import k19056DiaryNew
from diaries.K19096DiaryNew import K19096DiaryNew


diaries = [DiarySample(), k19056DiaryNew(), TakamotoDiaryNew(), K19096DiaryNew(),]
for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()