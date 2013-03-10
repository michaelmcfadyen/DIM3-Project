from bfb_app.models import Genre,Artist,Venue

g = Genre(genre='Alternative Music').save()

g = Genre(genre='Blues')
g.save()

g = Genre(genre='Classical Music')
g.save()

g = Genre(genre='Country Music')
g.save()

g = Genre(genre='Dance Music')
g.save()

g = Genre(genre='Easy Listening')
g.save()

g = Genre(genre='Electronic Music')
g.save()

g = Genre(genre='European Music (Folk / Pop)')
g.save()
 
g = Genre(genre='Hip Hop / Rap')
g.save()

g = Genre(genre='Indie Pop')
g.save()

g = Genre(genre='Inspirational (incl. Gospel)')
g.save()

g = Genre(genre='Asian Pop (J-Pop, K-pop)')
g.save()

g = Genre(genre='Jazz')
g.save()

g = Genre(genre='Latin Music')
g.save()


g = Genre(genre='New Age')
g.save()
g = Genre(genre='Opera')
g.save()
g = Genre(genre='Pop (Popular music)')
g.save()
g = Genre(genre='R&B / Soul')
g.save()
g = Genre(genre='Reggae')
g.save()
g = Genre(genre='Rock')
g.save()
g = Genre(genre='Singer / Songwriter (inc; Folk)')
g.save()
g = Genre(genre='World Music / Beats')
g.save()
    

venue = Venue(name="Oran Mor", address="Byres Rd  Glasgow G12 8QX",website="http://oran-mor.co.uk/")
venue.save()
venue = Venue(name="02 ABC" , address = "300 Sauchiehall St  Glasgow, Lanarkshire G2 3JA",website = "http://www.o2abcglasgow.co.uk/")
venue.save()
venue = Venue(name ="Box",address ="431 Sauchiehall St  Glasgow G2 3LG", website="http://boxglasgow.co.uk/")
venue.save()
venue = Venue(name="Stereo",address="22-28 Renfield Ln  Glasgow G2 6PH", website="http://www.stereocafebar.com/")
venue.save()
venue = Venue(name="Pivo Pivo", address="15 Waterloo St  Glasgow G2 6AY", website="https://plus.google.com/110023145115812766440/about?gl=uk&hl=en")
venue.save

    
    
    
    
    
    
    
    
    
    
    

