def fetch_children_by_trait(obj, name, trait_func):
    return [x for x in obj.canvas.after.children\
            if str(type(x)).find(name) != -1 and trait_func(x)]

def apply_if_trait(obj, name, trait_func, trait, set_trait):
    for elem in fetch_children_by_trait(obj, name, trait_func):
        setattr(elem, trait, set_trait(elem))
        print("Setting property")
    #return elem

def debug_color_bg(obj, color, opacity):
    trait_func = lambda x, c=color: (list(x.rgba)[:3] == list(c))
    set_trait = lambda x, o=opacity: tuple(list(x.rgba)[:3], o)
    print(trait_func(obj))
    apply_if_trait(obj, 'Color', trait_func, 'rgba', set_trait)

