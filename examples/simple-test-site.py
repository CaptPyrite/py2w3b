import py2w3b.Web as web
from py2w3b.Widgets import Label

website = web.NewSite()

home_page = web.NewPage(website, "__main__", 
                        title="First website!")

label1 = Label(home_page, "Hello, World!", px=50)
label1.show()

website.mainloop()
