
#1 שימוש ב - filter עבור רשימת מספרים
# צור רשימה של 50 מספרים אקראיים בין 1-100 והדפס אותה
# כעת השתמש ב filter וב- lambda כדי לקבל מתוך הרשימה:
import random
import statistics
from operator import index

from turtledemo.penrose import start

random_list:list[int] =  [random.randint(1,100) for i in range(50)]
print(random_list)

#a. רק מספרים הגדולים מ- 50
print(list(filter(lambda x: x > 50, random_list)))

# b. רק מספרים המתחלקים ב - 7 ללא שארית
print(list(filter(lambda x: x %7== 0, random_list)))

# c. רק מספרים דו- ספרתיים )רמז: 10-99(
print(list(filter(lambda x: x > 10 or x < 99, random_list)))

# d. רק מספרים דו- ספרתיים שספרת האחדות שלהם שווה לספרת העשרות שלהם
print(list(filter(lambda x: x %10 ==0   , random_list)))

# e. רק מספרים ש - סכום הספרות שלהם הוא 9
print(list(filter(lambda x: x//10 + x%10 == 9, random_list)))

# f. רק מספרים הגדולים מהממוצע
print(list(filter(lambda x: x > statistics.mean(random_list), random_list)))

# g. רק מספרים הגדולים מחצי של המספר המקסימלי ברשימה
print(list(filter(lambda x: x > max(random_list) / 2, random_list)))



# .2 שימוש ב - filter עבור רשימת מילים
# צור רשימת מילים שתכיל את המשחקים הבאים: ,"V Auto Theft Grand ","Fortnite"
# "The Elder Scrolls V: Skyrim", "Dark Souls", "Overwatch"
# כעת השתמש ב filter וב - lambda כדי לקבל מתוך הרשימה:

games: list[str] = ["V Auto Theft Grand ","Fortnite","The Elder Scrolls V: Skyrim", "Dark Souls", "Overwatch"]

# a. רק משחקים ששמם גדול מ- 8 אותיות
print(list(filter(lambda w: len(w) > 8, games)))

# b. רק משחקים ששמם מתחיל באות F
print(list(filter(lambda w: w.startswith("F"), games)))

# c. רק משחקים ששמם מכיל בדיוק 2 מילים
print(list(filter(lambda w: len(w.split()) == 2, games)))

# d. רק משחקים ששמם מכיל את האות V
print(list(filter(lambda w: "v".upper() in w , games)))


# .3 שימוש ב - map. מקור מספר
# צור רשימה של 20 מספרים אקראיים בין מינוס 50 לבין פלוס 50 והדפס אותה
# השתמש ב map וב- lambda כדי לקבל רשימה חדשה שתכיל:
rand_list: list[int] = [random.randint(-50,50) for _ in range(20)]
print(rand_list)


# a. כל מספר בחזקת 3
print(list(map(lambda x: x**3, rand_list)))

# b. רק ספרת האחדות של כל מספר. לדוגמא המספר 42 יהפוך ל - .2 רמז % .10
print(list(map(lambda x: x%10, rand_list)))

# c. כל מספר בפרנהייט. כלומר להכפיל ב - 9/5 ולהוסיף 32
print(list(map(lambda x: f"{x * 9/5 + 32:.2f}" , rand_list)))

# d.* בונוס: כל מספר חיובי יהפוך למילה "positive "וכל מספר שלילי יהפוך למילה-
# "negative"
print(list(map(lambda x: "positive" if x >= 0 else "negative" , rand_list)))


# .4 שימוש ב - map. מקור מחרוזת
# צור רשימת מילים שתכיל את הפירות הבאים: ,"Mango ","Orange ","Banana ","Apple "
# "Strawberry", "Pineapple", "Grapes", "Watermelon"
# השתמש ב map וב- lambda כדי לקבל רשימה חדשה שתכיל:

# a. כל פרי בסדר אותיות הפוך. רמז ]-1 ::[
fruits: list[str] =  ["Mango ","Orange ","Banana ","Apple ", "Strawberry", "Pineapple", "Grapes", "Watermelon"]
print(list(map(lambda f: f[::-1], fruits)))

# b. אות ראשונה של כל פרי
print(list(map(lambda f: f[0], fruits)))

# c. הפרי כולו באותיות גדולות
print(list(map(lambda f: f.upper(), fruits)))

# d. אות אמצעית של כל פרי
print(list(map(lambda f: f[len(f) // 2] , fruits)))


# e.** בונוס: אם הפרי מסתיים באות s הוסף סימן קריאה. אחרת יישאר אותו הדבר
print(list(map(lambda f: f + "!" if f[-1] == "s" else f , fruits)))


# .5 מה המשמעות של המילה global בתוך פונקציה?
# מה החסרון בשימוש ב- global כחלק מפונקציה? מה זה ידרוש בעתיד...


# מה המשמעות של המילה global בתוך פונקציה?
# בתוך הפונקציה המילה גלובל מאפשרת לשנות את ערכו הגלובלי של משתנה כלשהו שהוגדר מחוצה לה

# מה החסרון בשימוש ב- global כחלק מפונקציה מה זה ידרוש בעתיד...?
# אם המשתנה הגלובלי לא ימצא, אז לוקלית הפונקציה תכשל כי לא יהיה לה מאיפה לקחת את הערך הגלובלי
# אם נרצה לשנות את ערכו של המשתנה הגלובלי מבחוץ זה יצור שינוי בכל הפונקציות שעושות שימוש בגלובל מה שעלול לגרום לבעיות בקוד

# מדוע כאן נקבל שגיאה-

x: int = 1
def foo():
    print(x)
    x = 4
foo()
# הפונקציה אמורה להדפיס את המשתנה x הבעיה היא שההדפסה קוראת לפני שהx הוגדר לוקלית כ x=4, ובלי הגלובל אין לנו גישה להגיע לערכו הגלובלי של x
