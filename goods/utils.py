from django.db.models import Q

from goods.models import Products


# Функция поиска
def q_search(query):
    
    # По уникальному ключу
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    
    return Products.objects.filter(description__search=query)
    
    
    
    #Ручной фильтр
    # # По словам
    # keywords = [word for word in query.split() if len(word) > 2]
    
    # q_object = Q()
    
    # for token in keywords:
    #     # Поиск по описанию
    #     q_object |= Q(description__icontains=token)
    #     # Поиск по названию
    #     q_object |= Q(name__icontains=token)
    
    # return Products.objects.filter(q_object)