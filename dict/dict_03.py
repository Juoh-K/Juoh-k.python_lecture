# dict 만들기

foods = {"떡볶이":"오뎅",
         "짜장면":"단무지",
         "라면":"김치",
         "피자":"피클",
         "맥주":"땅콩",
         "치킨":"치킨무",
         "삼겹살":"상추",
        };

food_list = list(zip(foods.keys(), foods.values()))
print(food_list)

# for i , data in list(foods) :
#     print(i)