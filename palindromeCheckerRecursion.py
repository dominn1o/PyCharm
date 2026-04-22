def palindrome(word):
    if len(word) <= 1:
        print("Palindrome")
        return
    elif word[0] != word[-1]:
        print("Not Palindrome")
        return
    w = word[1:-1]
    return palindrome(w)

palindrome("fdsabfisdlafslavbifysavfjdslaufgsaiyflvsaifysafsvaifvsaiyfvsdljfvsagfdsvayfvldfiuafdsgafbhsdbfkhbdsfbsfdshanjfdisbafiofisabjbguifsuaodifhisbgobusdabufiushogbuiasbidofhasghuidfsiafusogaidsbaufodfhasiubfubsuafbhvsiaufoiahsogafvidvfvidvhiusdabfvdsfi")